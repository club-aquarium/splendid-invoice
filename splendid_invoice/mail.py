"""
splendid-invoice
Copyright (C) 2022-2023  schnusch

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

from contextlib import contextmanager
from datetime import datetime, timezone
from email.message import Message
from email.utils import mktime_tz, parsedate_tz
from queue import Queue
from tempfile import NamedTemporaryFile
from typing import Iterator, List, Optional, TextIO, Tuple, cast

import popplerqt5  # type: ignore

from . import (
    csv_from_pdf,
    open_stdout,
)
from .base import Invoice
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
                    or name.endswith(".pdf")
                )
            ):
                yield (msg, name, part.get_payload(decode=True))


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


@contextmanager
def wrapped_open_stdout(first: bool) -> Iterator[Tuple[bool, TextIO]]:
    with open_stdout() as stdout:
        yield (first, stdout)


def open_noexist(name: str) -> TextIO:
    try:
        return open(name, "r", encoding="iso-8859-1", newline="")
    except FileNotFoundError:
        return open(os.path.devnull, "r")


@contextmanager
def renamed_tempfile(dest: str) -> Iterator[TextIO]:
    with NamedTemporaryFile(
        dir=os.path.dirname(dest) or os.path.curdir,
        mode="w",
        encoding="iso-8859-1",
        newline="",
    ) as tmp:
        yield cast(TextIO, tmp)
        os.rename(tmp.name, dest)
        tmp._closer.delete = False


@contextmanager
def append_csv(name: str) -> Iterator[Tuple[bool, TextIO]]:
    with open_noexist(name) as inp, renamed_tempfile(name) as out:
        lines = iter(inp)
        # prepend old lines
        empty = True
        for line in lines:
            out.write(line)
            empty = False
        # empty file needs new headers
        yield (empty, out)


@contextmanager
def prepend_csv(name: str) -> Iterator[Tuple[bool, TextIO]]:
    with open_noexist(name) as inp, renamed_tempfile(name) as out:
        lines = iter(inp)
        # skip header
        reader = csv.reader(lines, delimiter=";")
        try:
            next(iter(reader))
        except StopIteration:
            pass
        # tell caller to write new header
        yield (True, out)
        # append old lines
        for line in lines:
            out.write(line)


def parse_datetime(dt: str) -> datetime:
    return datetime.strptime(dt, "%Y-%m-%d %H:%M:%S%z")


def git_get_author_time(path: str) -> Optional[datetime]:
    proc = subprocess.run(
        [
            "git",
            "-C",
            os.path.dirname(path) or os.path.curdir,
            "log",
            "--format=format:%aI",  # ISO-8601 author date
            "--max-count=1",
            "--",
            os.path.basename(path) or os.path.curdir,
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        encoding="utf-8",
    )
    if proc.returncode == 0 and proc.stdout:
        return datetime.strptime(proc.stdout.strip(), "%Y-%m-%dT%H:%M:%S%z")
    else:
        return None


def git_commit(path: str, msg: Message, pdfname: str, verbose: bool) -> None:
    git = ["git", "-C", os.path.dirname(path) or os.path.curdir]
    name = os.path.basename(path) or os.path.curdir

    p = subprocess.run(
        [*git, "diff", "--quiet", "HEAD", "--", name], stdin=subprocess.DEVNULL
    )
    if p.returncode == 0:
        return

    cmd = [*git, "add", "--", name]
    if verbose:
        print("$", *map(shlex.quote, cmd), file=sys.stderr)
    subprocess.run(cmd, stdin=subprocess.DEVNULL, check=True)

    cmd = [*git, "commit", "-F", "-"]
    date = get_message_date(msg)
    if date:
        cmd.append("--date=" + date.strftime("%Y-%m-%dT%H:%M:%S%z"))
    if verbose:
        cmd.append("--verbose")
    cmd.append("--")
    cmd.append(name)
    message = [f"add {pdfname}", ""]
    for header in ("Subject", "From", "Date"):
        if header in msg:
            for value, _ in email.header.decode_header(msg.get(header, "")):
                assert isinstance(value, str)
                message.append(f"{header}: {value}")
    if verbose:
        print("$", *map(shlex.quote, cmd), file=sys.stderr)
    subprocess.run(cmd, input="\n".join(message), encoding="utf-8", check=True)


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
    args = p.parse_args(argv)

    after = args.after
    if args.git is not None:
        if after is None:
            after = git_get_author_time(args.git)
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
        if not first:
            print(file=sys.stderr)
        print_mail_info(msg, pdfname)
        try:
            pdf = popplerqt5.Poppler.Document.loadFromData(pdfdata)
            try:
                invoice = Zugferd1p0Invoice(pdf)  # type: Invoice
            except AssertionError:
                try:
                    invoice = MonospaceInvoice(pdf)
                except AssertionError:
                    invoice = NewInvoice(pdf)
            if args.git is None:
                context = wrapped_open_stdout(first)
            elif args.reverse:
                context = prepend_csv(args.git)
            else:
                context = append_csv(args.git)
            with context as (write_headers, out):
                csv_from_pdf(out, invoice, write_headers, print_pages=args.verbose)
        except Exception:
            with NamedTemporaryFile(
                "wb", prefix="splendid-invoice.", suffix=".pdf", delete=False
            ) as fp:
                fp.write(pdfdata)
                fp.flush()
                print(
                    f"Cannot parse PDF file, written to {fp.name} for inspection.",
                    file=sys.stderr,
                )
            raise
        if args.git is not None:
            git_commit(args.git, msg, pdfname, args.verbose)
        first = False

        if args.confirm:
            print(end="Press Enter to continue...")
            input()


if __name__ == "__main__":
    main()
