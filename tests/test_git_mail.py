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

import email.message
import email.policy
import os
import subprocess
import tempfile
import unittest
from collections.abc import Iterable
from contextlib import contextmanager
from datetime import datetime
from functools import partial
from typing import List  # noqa: F401
from typing import Iterator, Optional, Tuple
from unittest.mock import patch

import splendid_invoice.mail
from .test_git_full_mailbox import csv_rows


def concat_csvs(paths: Iterable[str]) -> Iterator[Tuple[str, ...]]:
    first = True
    for path in paths:
        rows = csv_rows(path)
        # skip header in all but the first file
        if first:
            first = False
        else:
            next(rows)
        for row in rows:
            yield row


def fake_fetch_pdf(
    pdfpath: str,
    host: str,
    login: str,
    password: str,
    mailbox: Optional[str] = None,
    max_count: Optional[int] = None,
    after: Optional[datetime] = None,
) -> Iterator[Tuple[email.message.Message, str, bytes]]:
    msg = email.message.EmailMessage(policy=email.policy.default)
    # msg does not need any headers
    with open(pdfpath, "rb") as fp:
        yield (msg, os.path.basename(pdfpath), fp.read())


class TestGitMail(unittest.TestCase):
    def setUp(self) -> None:
        directory = os.path.join(os.path.dirname(__file__), "splendid")
        self.mails = []  # type: List[Tuple[str, str]]
        with os.scandir(directory) as it:
            for pdf in it:
                if pdf.name.endswith(".pdf"):
                    csvpath = pdf.path[:-3] + "csv"
                    if os.path.exists(csvpath):
                        self.mails.append((pdf.path, csvpath))
        if not self.mails:
            self.skipTest(f"no PDFs found in {directory!r}")

        _temp = tempfile.TemporaryDirectory(prefix="splendid-invoice.")
        self.addCleanup(_temp.cleanup)
        temp = _temp.name
        for cmd in [
            ["git", "init", "-q", "--", temp],
            ["git", "-C", temp, "config", "user.name", "test"],
            ["git", "-C", temp, "config", "user.email", "test@localhost"],
        ]:
            subprocess.run(cmd, check=True)

        self.git_csv = os.path.join(temp, "invoices.csv")
        self.mail_cmd = [
            "--host",
            "",
            "--login",
            "",
            "--password",
            "",
            "--git",
            self.git_csv,
        ]

    @contextmanager
    def _git_log(
        self,
        start: str = "HEAD",
        extra_argv: List[str] = [],
    ) -> Iterator[None]:
        git = ["git", "-C", os.path.dirname(self.git_csv)]
        cmd = [*git, "--no-pager", "log", "--graph", "--oneline"]
        cmd.extend(extra_argv)
        p = subprocess.run(
            [*git, "rev-parse", start],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        if p.returncode == 0:
            cmd.append(f"{os.fsdecode(p.stdout.strip())}..HEAD")
        try:
            yield
        finally:
            subprocess.run(cmd, stdin=subprocess.DEVNULL, check=True)

    def _incremental_mail(self, argv: List[str]) -> Iterator[List[str]]:
        csvpaths = []  # type: List[str]
        for pdfpath, csvpath in self.mails:
            with patch(
                "splendid_invoice.mail.fetch_pdfs",
                partial(fake_fetch_pdf, pdfpath),
            ):
                # with self._git_log(extra_argv=["--patch"]):
                splendid_invoice.mail.main(argv)
            csvpaths.append(csvpath)
            yield csvpaths

    def test_append(self) -> None:
        for csvpaths in self._incremental_mail(self.mail_cmd):
            got_rows = list(csv_rows(self.git_csv))
            expected_rows = list(concat_csvs(csvpaths))
            self.assertEqual(got_rows, expected_rows)

    def test_prepend(self) -> None:
        for csvpaths in self._incremental_mail(self.mail_cmd + ["--reverse"]):
            got_rows = list(csv_rows(self.git_csv))
            expected_rows = list(concat_csvs(reversed(csvpaths)))
            self.assertEqual(got_rows, expected_rows)
