"""
splendid-invoice
Copyright (C) 2023  schnusch

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
import sys
from typing import (
    List,
    Optional,
    TextIO,
)

from .base import Invoice
from .splendid import MonospaceInvoice, NewInvoice
from .zugferd_1p0 import Zugferd1p0Invoice


def open_stdout() -> TextIO:
    return open(sys.stdout.fileno(), "w", encoding="utf-8", newline="", closefd=False)


def csv_from_pdf(
    fileobj: TextIO,
    invoice: Invoice,
    write_headers: bool = False,
    print_pages: bool = False,
) -> None:
    out = csv.writer(fileobj, delimiter=";", quoting=csv.QUOTE_ALL)
    if write_headers:
        out.writerow(invoice.headers)
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

    with open_stdout() as stdout:
        first = True
        for name in args.invoice:
            try:
                invoice = Zugferd1p0Invoice.load(name)  # type: Invoice
            except AssertionError:
                try:
                    invoice = MonospaceInvoice.load(name)
                except AssertionError:
                    invoice = NewInvoice.load(name)
            csv_from_pdf(
                stdout,
                invoice,
                write_headers=first,
                print_pages=args.verbose,
            )
            first = False
