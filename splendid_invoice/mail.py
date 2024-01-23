"""
splendid-invoice
Copyright (C) 2022-2024  schnusch

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import argparse
import csv
import email
import email.policy
import imaplib
import os.path
import re
import shlex
import subprocess
import sys
import threading
from collections.abc import Iterable
from datetime import datetime, timezone
from email.message import Message
from email.utils import mktime_tz, parsedate_tz
from queue import Queue
from tempfile import NamedTemporaryFile
from types import TracebackType
from typing import (
    Any,
    BinaryIO,
    Iterator,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    cast,
)

import popplerqt5  # type: ignore

from . import (
    CSVStdout,
    csv_from_pdf,
)
from .base import Invoice  # noqa: F401
from .base import CSVOutput, DummyInvoice
from .splendid import (
    MonospaceInvoice,
    NewInvoice,
)
from .zugferd_1p0 import Zugferd1p0Invoice


def filter_by_sender(msg: Message) -> bool:
    addr = email.header.decode_header(msg["From"])[0][0]
    if isinstance(addr, bytes):
        senderaddr = addr.decode("iso-8859-1")
    else:
        assert isinstance(addr, str)
        senderaddr = addr
    return (
        re.match(
            r".*@(getraenke-pfeifer\.de|splendid-drinks\.com|gustav-mueller\.de)>?$",
            senderaddr,
        )
        is not None
    )


def get_message_date(msg: Message) -> Optional[datetime]:
    if msg["Date"] is None:
        return None
    date_header = email.header.decode_header(msg["Date"])[0][0]
    if isinstance(date_header, bytes):
        date = parsedate_tz(date_header.decode("iso-8859-1"))
    else:
        assert isinstance(date_header, str)
        date = parsedate_tz(date_header)
    if date is None:
        return None
    return datetime.fromtimestamp(mktime_tz(date), timezone.utc)


def filter_by_date(msg: Message, after: Optional[datetime]) -> bool:
    if after is None:
        return True
    date = get_message_date(msg)
    if date is None:
        return False
    return date > after


def iter_pdfs(
    mbox: imaplib.IMAP4,
    message_ids: List[str],
    max_count: Optional[int] = None,
    after: Optional[datetime] = None,
) -> Iterator[Tuple[Message, str, bytes]]:
    for message_id in message_ids:
        res, data = mbox.fetch(message_id, "(RFC822.HEADER)")
        assert res == "OK"
        assert isinstance(data[0], tuple) and isinstance(data[0][1], bytes)
        msg = email.message_from_bytes(data[0][1], policy=email.policy.default)

        if not filter_by_sender(msg) or not filter_by_date(msg, after):
            continue

        if max_count is not None:
            if max_count <= 0:
                return
            max_count -= 1

        res, data = mbox.fetch(message_id, "(RFC822)")
        assert res == "OK"
        assert isinstance(data[0], tuple) and isinstance(data[0][1], bytes)
        msg = email.message_from_bytes(data[0][1], policy=email.policy.default)
        for part in msg.walk():
            name = part.get_filename()
            if (
                part.get_content_maintype() != "multipart"
                and part.get("Content-Disposition") is not None
                and (
                    part.get_content_type() == "application/pdf"
                    or (name is not None and name.endswith(".pdf"))
                )
            ):
                if name is None:
                    name = "attachment.pdf"
                payload = part.get_payload(decode=True)
                assert isinstance(payload, bytes)
                yield (msg, name, payload)


def fetch_pdfs(
    host: str,
    login: str,
    password: str,
    mailbox: Optional[str] = None,
    max_count: Optional[int] = None,
    after: Optional[datetime] = None,
) -> Iterator[Tuple[Message, str, bytes]]:
    with imaplib.IMAP4_SSL(host) as mbox:
        mbox.login(login, password)
        if mailbox is not None:
            mbox.select(mailbox)
        res, data = mbox.search(None, "ALL")
        assert res == "OK"

        message_ids = data[0].split()

        queue = Queue(2)  # type: Queue[Optional[Tuple[Message, str, bytes]]]

        def thread_proc() -> None:
            try:
                for x in iter_pdfs(mbox, message_ids, max_count, after):
                    queue.put(x)
            finally:
                queue.put(None)

        t = threading.Thread(target=thread_proc, daemon=True)
        t.start()

        yield from iter(queue.get, None)

        t.join()


def open_noexist(name: str) -> BinaryIO:
    try:
        return open(name, "rb")
    except FileNotFoundError:
        return open(os.path.devnull, "rb")


T = TypeVar("T", bound="GitCSVOutput")


class GitCSVOutput(CSVOutput):
    @staticmethod
    def get_rotate_filename(base: str, i: int, ext: str) -> str:
        assert i >= 0
        name = base
        if i > 0:
            name += "-%d" % i
        name += ext
        return name

    @staticmethod
    def copy_all(src: BinaryIO, dst: BinaryIO, force_eol: bool = False) -> None:
        b = None  # type: Optional[bytes]
        for b in iter(lambda: src.read(4096), b""):
            assert dst.write(b) == len(b)
        if force_eol and b is not None:
            if b.endswith(b"\r"):
                dst.write(b"\n")
            elif not b.endswith(b"\n"):
                dst.write(b"\r\n")

    def __init__(
        self,
        path: str,
        message: Message,
        pdfname: str,
        max_size: Optional[int] = None,
        verbose: bool = False,
    ):
        self.path = path
        self.message = message
        self.pdfname = pdfname
        self.max_size = max_size
        self.verbose = verbose

        self.directory = os.path.dirname(self.path) or os.path.curdir
        self.basename = os.path.basename(self.path)
        assert self.basename

        self.empty = True
        self.buffered_headers = []  # type: List[Iterable[Any]]
        self.inp = open_noexist(self.path)
        try:
            self.out = NamedTemporaryFile(
                dir=os.path.dirname(self.path) or os.path.curdir,
                mode="w+b",
            )
            try:
                super().__init__(self)
            except BaseException:
                self.out.close()
                raise
        except BaseException:
            self.inp.close()
            raise

    # csv.reader/.writer compatibility methods

    @staticmethod
    def try_decode_utf8(b: bytes) -> str:
        try:
            return b.decode("utf-8")
        except UnicodeDecodeError:
            return b.decode("iso-8859-1")

    def readline(self) -> bytes:
        # readline reads up to the next b"\n", but only want to the next b"\r",
        # b"\n", or b"\r\n", so we seek backwards.
        lf_line = self.inp.readline()
        if not lf_line:
            return lf_line
        any_line = lf_line.splitlines(keepends=True)[0]
        off = len(lf_line) - len(any_line)
        if off > 0:
            self.inp.seek(-off, os.SEEK_CUR)
        return any_line

    def __iter__(self: T) -> T:
        return self

    def __next__(self) -> str:
        line = self.readline()
        if not line:
            raise StopIteration
        return self.try_decode_utf8(line)

    def write(self, s: str) -> None:
        b = s.encode("utf-8")
        assert self.out.write(b) == len(b)

    def __exit__(
        self,
        type: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        try:
            # do nothing on exception
            if type is not None:
                return super().__exit__(type, value, traceback)

            self.copy_tail()

            os.replace(self.out.name, self.path)
        finally:
            # close open files
            try:
                self.out.close()
            except FileNotFoundError:
                pass
            finally:
                self.inp.close()
        self.commit()
        return super().__exit__(type, value, traceback)

    # CSVOutput methods

    def writeheaders(self, headers: Iterable[Any]) -> None:
        self.buffered_headers.append(headers)

    def write_buffered_headers(self) -> None:
        for header in self.buffered_headers:
            super().writeheaders(header)
        self.buffered_headers = []

    def writerow(self, row: Iterable[Any]) -> None:
        if self.empty:
            self.empty = False
            if not self.copy_head():
                self.write_buffered_headers()
        super().writerow(row)

    def copy_head(self) -> bool:
        """Copy leading lines from self.inp to self.out. Return True if
        anything was written.
        """
        return False

    def copy_tail(self) -> None:
        """Copy trailing lines from self.inp to self.out."""
        pass

    def run_git(
        self,
        *args: str,
        input: Optional[bytes] = None,
        stdout: Optional[int] = None,
        check: bool = True,
    ) -> subprocess.CompletedProcess:
        cmd = ["git", "-C", self.directory, *args]
        if self.verbose:
            print("$", *map(shlex.quote, cmd), file=sys.stderr)
        return subprocess.run(
            cmd,
            input=input,
            stdin=subprocess.DEVNULL if input is None else None,
            stdout=stdout,
            check=check,
        )

    def _rotate_file(self, base: str, i: int, ext: str) -> Tuple[str, int]:
        src = self.get_rotate_filename(base, i, ext)
        n = i
        if os.path.exists(os.path.join(self.directory, src)):
            dest, n = self._rotate_file(base, i + 1, ext)
            assert not os.path.exists(dest)
            self.run_git("mv", "--", src, dest)
            self.run_git("commit", "-m", f"rotate {src} ({n - i}/{n})")
        return (src, n)

    def rotate_file(self) -> None:
        p = self.run_git("rev-parse", "HEAD", stdout=subprocess.PIPE, check=False)
        old_head = os.fsdecode(p.stdout.strip()) if p.returncode == 0 else None

        base, ext = os.path.splitext(self.basename)
        _, n = self._rotate_file(base, 0, ext)

        if n > 1 and old_head is not None:
            merge = os.fsdecode(
                self.run_git(
                    "commit-tree",
                    "-p",
                    old_head,
                    "-p",
                    "HEAD",
                    "-m",
                    f"rotate {self.basename}",
                    "HEAD^{tree}",
                    stdout=subprocess.PIPE,
                ).stdout.strip()
            )

            p = self.run_git(
                "symbolic-ref",
                "HEAD",
                stdout=subprocess.PIPE,
                check=False,
            )
            branch = os.fsdecode(p.stdout.strip()) if p.returncode == 0 else None

            self.run_git("update-ref", "HEAD" if branch is None else branch, merge)

        # `self.path` is untracked after git-mv
        open(self.path, "ab").close()
        self.run_git("add", "--intent-to-add", "--", self.basename)

    def commit(self) -> None:
        p = self.run_git("diff", "--quiet", "HEAD", "--", self.basename, check=False)
        if p.returncode == 0:
            return

        self.run_git("add", "--", self.basename)

        cmd = ["commit", "-F", "-"]
        date = get_message_date(self.message)
        if date:
            cmd.append("--date=" + date.strftime("%Y-%m-%dT%H:%M:%S%z"))
        if self.verbose:
            cmd.append("--verbose")
        cmd.append("--")
        cmd.append(self.basename)
        message = [f"add {self.pdfname}", ""]
        for header in ("Subject", "From", "Date"):
            if header in self.message:
                for value, _ in email.header.decode_header(
                    self.message.get(header, "")
                ):
                    assert isinstance(value, str)
                    message.append(f"{header}: {value}")
        self.run_git(*cmd, input="\n".join(message).encode("utf-8"))


class GitCSVOutputAppend(GitCSVOutput):
    @staticmethod
    def move_left(fp: BinaryIO, dest: int, src: int) -> None:
        if src == dest:
            # nothing to do
            return
        assert src > dest, f"dest={dest} is not before src={src}"
        bufsize = min(4096, src - dest)
        while True:
            fp.seek(src)
            buf = fp.read(bufsize)
            fp.seek(dest)
            if not buf:
                break
            assert fp.write(buf) == len(buf)
            src += len(buf)
            dest += len(buf)

    def __init__(
        self,
        path: str,
        message: Message,
        pdfname: str,
        max_size: Optional[int] = None,
        verbose: bool = False,
    ):
        self.old_size = 0
        super().__init__(path, message, pdfname, max_size, verbose)

    def copy_head(self) -> bool:
        # prepend old lines
        self.copy_all(self.inp, cast(BinaryIO, self.out), force_eol=True)
        self.old_size = self.out.tell()
        return self.old_size > 0

    def copy_tail(self) -> None:
        if (
            self.max_size is not None
            and self.old_size > 0  # self.inp is not empty
            and self.out.tell() > self.max_size
        ):
            self.out.seek(0)
            self.write_buffered_headers()
            src = self.out.tell()
            assert (
                src <= self.old_size
            ), f"buffered headers overwrote part of the new rows (self.out.tell() = {src}, self.old_size = {self.old_size})"
            self.move_left(cast(BinaryIO, self.out), src, self.old_size)
            self.out.truncate()

            self.rotate_file()


class GitCSVOutputPrepend(GitCSVOutput):
    def copy_head(self) -> bool:
        # skip header in self.inp
        reader = csv.reader(self, delimiter=self.delimiter)
        try:
            next(iter(reader))
        except StopIteration:
            pass
        return False

    def copy_tail(self) -> None:
        if (
            self.max_size is None
            # old_size + new_size <= max_size
            or os.stat(self.inp.fileno()).st_size + self.out.tell() <= self.max_size
        ):
            self.copy_all(self.inp, cast(BinaryIO, self.out))
        else:
            self.rotate_file()


def parse_datetime(dt: str) -> datetime:
    return datetime.strptime(dt, "%Y-%m-%d %H:%M:%S%z")


def git_get_author_time(path: str, verbose: bool) -> Optional[datetime]:
    cmd = [
        "git",
        "-C",
        os.path.dirname(path) or os.path.curdir,
        "log",
        "--format=format:%aI",  # ISO-8601 author date
        "--max-count=1",
        "--",
        os.path.basename(path) or os.path.curdir,
    ]
    if verbose:
        print("$", *map(shlex.quote, cmd), file=sys.stderr)
    proc = subprocess.run(
        cmd,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if proc.returncode == 0 and proc.stdout:
        return datetime.strptime(
            proc.stdout.strip().decode("utf-8"),
            "%Y-%m-%dT%H:%M:%S%z",
        )
    else:
        return None


def print_mail_info(msg: Message, name: str) -> None:
    sys.stderr.write("\x1b[33m")
    try:
        for header in ("Subject", "From", "Date"):
            for value, _ in email.header.decode_header(msg.get(header, "")):
                print(f"{header}:", value, file=sys.stderr)
        print("Attachment:", name, file=sys.stderr)
    finally:
        sys.stderr.write("\x1b[39m")
        sys.stderr.flush()


def parse_size(x: str) -> int:
    for factor, units in [
        (1000, ["KB"]),
        (1024, ["K", "Ki", "KiB"]),
        (1_000_000, ["MB"]),
        (1024**2, ["M", "Mi", "MiB"]),
        (1_000_000_000, ["GB"]),
        (1024**3, ["G", "Gi", "GiB"]),
        (1, ["B"]),
    ]:
        for unit in units:
            if x.endswith(unit):
                return int(x[: -len(unit)]) * factor
    return int(x)


def main(argv: Optional[List[str]] = None) -> None:
    example = " ".join(
        map(
            shlex.quote,
            [
                sys.argv[0],
                "-v",
                "-H",
                "mx2f77.netcup.net",
                "-l",
                "archiv@club-aquarium.de",
                "-m",
                '"INBOX.Rechnungen Eingang"',
            ],
        )
    )
    p = argparse.ArgumentParser(
        description="Download PDF attachments from mailbox and feed them into splendid-invoice",
        epilog=f"Example: {example}",
    )
    p.add_argument("-H", "--host", required=True, help="IMAP host")
    p.add_argument("-l", "--login", required=True, help="IMAP login")
    g = p.add_mutually_exclusive_group(required=True)  # type: argparse._ArgumentGroup
    g.add_argument("-p", "--password", help="IMAP password")
    g.add_argument(
        "--password-from-stdin",
        action="store_true",
        help="read IMAP password from stdin",
    )
    p.add_argument(
        "-m", "--mailbox", help="mailbox sub-directory, be sure to quote properly"
    )
    p.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print parsed PDF to standard error.",
    )
    p.add_argument(
        "--confirm",
        action="store_true",
        help="Wait for user to press Enter after each PDF.",
    )
    g = p.add_argument_group("selection arguments")
    g.add_argument(
        "--after",
        type=parse_datetime,
        help="Skip messages before AFTER. (format YYYY-MM-DD HH:MM:SS[+-]HH:MM)",
    )
    g.add_argument(
        "-n", "--max-count", type=int, metavar="N", help="Stop after N messages."
    )
    g = p.add_argument_group("git arguments")
    g.add_argument(
        "--git",
        metavar="FILE",
        help="Write csv to git-tracked file FILE.",
    )
    g.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        help="When writing to a git-tracked file, append newer invoices to the top of the file.",
    )
    g.add_argument(
        "--max-size",
        type=parse_size,
        help="When writing to a git-tracked file, create a file if a maximum file size would be exceeded.",
    )
    args = p.parse_args(argv)

    after = args.after
    if args.git is not None:
        if after is None:
            after = git_get_author_time(args.git, args.verbose)
        # TODO check if args.git is dirty

    first = True
    for msg, pdfname, pdfdata in fetch_pdfs(
        host=args.host,
        login=args.login,
        password=input() if args.password is None else args.password,
        mailbox=args.mailbox,
        max_count=args.max_count,
        after=after,
    ):
        if first:
            first = False
        else:
            print(file=sys.stderr)
        print_mail_info(msg, pdfname)
        pdf = None  # type: Optional[popplerqt5.Poppler.Document]
        try:
            pdf = popplerqt5.Poppler.Document.loadFromData(pdfdata)
            invoice = DummyInvoice()  # type: Invoice
            for cls in (Zugferd1p0Invoice, MonospaceInvoice, NewInvoice):
                try:
                    invoice = cls(pdf)
                except (AssertionError, ValueError):
                    pass
            if args.git is None:
                out = CSVStdout()  # type: CSVOutput
            elif args.reverse:
                out = GitCSVOutputPrepend(
                    args.git,
                    msg,
                    pdfname,
                    max_size=args.max_size,
                    verbose=args.verbose,
                )
            else:
                out = GitCSVOutputAppend(
                    args.git,
                    msg,
                    pdfname,
                    max_size=args.max_size,
                    verbose=args.verbose,
                )
            with out:
                csv_from_pdf(out, invoice, print_pages=args.verbose)
        except Exception:
            with NamedTemporaryFile(
                "wb", prefix="splendid-invoice.", suffix=".pdf", delete=False
            ) as fp:
                if pdf is None:
                    fp.write(pdfdata)
                    fp.flush()
                else:
                    conv = pdf.pdfConverter()
                    conv.setOutputFileName(fp.name)
                    conv.setPDFOptions(
                        popplerqt5.Poppler.PDFConverter.PDFOption.WithChanges
                    )
                    assert conv.convert()
                print(
                    f"Cannot parse PDF file, written to {fp.name} for inspection.",
                    file=sys.stderr,
                )
            raise

        if args.confirm:
            print(end="Press Enter to continue...")
            input()


if __name__ == "__main__":
    main()
