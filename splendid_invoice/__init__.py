"""
splendid-invoice
Copyright (C) 2023-2025  schnusch

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
import sys
from collections.abc import Iterable
from types import TracebackType
from typing import (
    Any,
    List,
    Optional,
    TextIO,
    Type,
)

from .base import CSVOutput, Invoice
from .splendid import MonospaceInvoice, NewInvoice
from .zugferd.v1_0 import Zugferd_1_0_Invoice
from .zugferd.v2_3 import Zugferd_2_0_EN16931_Invoice


def open_stdout() -> TextIO:
    return open(sys.stdout.fileno(), "w", encoding="utf-8", newline="", closefd=False)


class CSVStdout(CSVOutput):
    def __init__(self) -> None:
        self.stdout = open_stdout()
        try:
            super().__init__(self.stdout)
        except BaseException:
            self.stdout.close()
            raise
        self.buffered_headers = []  # type: List[Iterable[Any]]

    def __exit__(
        self,
        type: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        self.stdout.close()
        return super().__exit__(type, value, traceback)

    def writeheaders(self, headers: Iterable[Any]) -> None:
        self.buffered_headers.append(headers)

    def writerow(self, row: Iterable[Any]) -> None:
        buffered_headers = self.buffered_headers
        if buffered_headers:
            # avoid infinite recursion, super().writeheaders calls self.writerow
            self.buffered_headers = []
            for header in buffered_headers:
                super().writeheaders(header)
        super().writerow(row)


def csv_from_pdf(
    out: CSVOutput,
    invoice: Invoice,
    print_pages: bool = False,
) -> None:
    out.writeheaders(invoice.headers)
    for row in invoice:
        out.writerow(row)

    if print_pages:
        invoice.print_pages()


def main(argv: Optional[List[str]] = None) -> None:
    p = argparse.ArgumentParser(
        description="Parse PDF invoices from Splendid Drinks or conforming to the ZUGFeRD 1.0 standard"
    )
    p.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print parsed PDF to standard error.",
    )
    p.add_argument("invoice", nargs="+", metavar="<invoice>")
    args = p.parse_args(argv)

    with CSVStdout() as out:
        for name in args.invoice:
            try:
                invoice = Zugferd_2_0_EN16931_Invoice.load(name)  # type: Invoice
            except AssertionError:
                try:
                    invoice = Zugferd_1_0_Invoice.load(name)
                except AssertionError:
                    try:
                        invoice = MonospaceInvoice.load(name)
                    except AssertionError:
                        invoice = NewInvoice.load(name)
            csv_from_pdf(out, invoice, print_pages=args.verbose)
