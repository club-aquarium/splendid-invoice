"""
splendid-invoice
Copyright (C) 2024  schnusch

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

import csv
import difflib
import os
import shlex
import subprocess
import sys
import tempfile
import unittest
from typing import Iterator, Tuple

import splendid_invoice.mail


def filter_expected_csv(dest: str) -> str:
    try:
        src = os.environ["SPLENDID_INVOICE_EXPECTED"]
    except KeyError:
        raise unittest.SkipTest(
            "missing environment variable SPLENDID_INVOICE_EXPECTED"
        )
    cmd = os.environ.get("SPLENDID_INVOICE_FILTER_CMD", "")
    if cmd:
        with open(src, "rb") as fin, open(dest, "wb") as fout:
            print(
                f"$ ({cmd})",
                "<",
                shlex.quote(src),
                ">",
                shlex.quote(dest),
                file=sys.stderr,
            )
            subprocess.run(cmd, shell=True, stdin=fin, stdout=fout, check=True)
        return dest
    else:
        return src


def csv_rows(name: str) -> Iterator[Tuple[str, ...]]:
    with open(name, "r", encoding="utf-8", newline="") as fp:
        for row in csv.reader(fp, delimiter=";"):
            yield tuple(row)


class TestMailGit(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory(prefix="splendid-invoice.")
        self.addCleanup(temp.cleanup)

        self.expected_csv = filter_expected_csv(os.path.join(temp.name, "expected.csv"))

        self.got_csv = os.environ.get("SPLENDID_INVOICE_GOT", "")
        if not self.got_csv:
            git = os.path.join(temp.name, "git")
            self.got_csv = os.path.join(git, "got.csv")
            try:
                mail_args = [
                    "--host",
                    os.environ["SPLENDID_INVOICE_MAIL_HOST"],
                    "--login",
                    os.environ["SPLENDID_INVOICE_MAIL_LOGIN"],
                    "--password",
                    os.environ["SPLENDID_INVOICE_MAIL_PASSWORD"],
                    "--git",
                    self.got_csv,
                    "--reverse",
                ]
            except KeyError as e:
                raise unittest.SkipTest(f"missing environment variable {e.args[0]}")
            mailbox = os.environ.get("SPLENDID_INVOICE_MAIL_MAILBOX", "")
            if mailbox:
                mail_args.extend(["--mailbox", mailbox])

            for cmd in [
                ["git", "init", "-q", "--", git],
                ["git", "-C", git, "config", "user.name", "test"],
                ["git", "-C", git, "config", "user.email", "test@localhost"],
            ]:
                subprocess.run(cmd, check=True)

            splendid_invoice.mail.main(mail_args)

    def test_mail_git(self) -> None:
        a = list(csv_rows(self.expected_csv))
        b = list(csv_rows(self.got_csv))
        # We allow exactly one block of additional lines in `self.got_csv` in
        # case the invoices from the mailbox are more up-to-date.
        ignore_leading_insert = 1
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b).get_opcodes():
            if tag != "equal":
                if ignore_leading_insert > 0 and tag == "insert":
                    ignore_leading_insert -= 1
                else:
                    if tag == "insert":
                        message = f"produced {j2 - j1} unexpected lines at {i1 + 1}"
                    elif tag == "delete":
                        message = f"missing {i2 - i1} lines at {i1 + 1}"
                    else:
                        assert tag == "replace"
                        message = f"differing lines at {i1 + 1}-{i2}"
                    self.assertEqual(a[i1:i2], b[j1:j2], message)
