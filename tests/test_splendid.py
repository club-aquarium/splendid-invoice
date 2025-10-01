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
import os
import pprint
import re
import unittest
from datetime import datetime
from typing import (
    Callable,
    Dict,  # noqa: F401
    List,
    Optional,
    Type,
    cast,
)

import popplerqt5  # type: ignore[import-not-found]

from splendid_invoice import Invoice, MonospaceInvoice, NewInvoice
from splendid_invoice.base import PaddedRow

TestMethod = Callable[[unittest.TestCase], None]


def filename_to_test_method_name(filename: str) -> str:
    assert filename.endswith(".pdf")
    filename = filename[:-4]
    assert re.match(
        r"^[A-Z_a-z][0-9A-Z_a-z]*$",
        filename,
    ), f"unsupported filename: {filename!r}"
    return f"test_{filename.lower()}"


def parse_date(row: List[str]) -> PaddedRow:
    delivery_date = datetime.strptime(row[0], "%Y-%m-%d").date()
    invoice_date = datetime.strptime(row[2], "%Y-%m-%d").date()
    dated_row = (delivery_date, row[1], invoice_date, *row[3:])
    assert len(dated_row) == len(Invoice.headers)
    return cast(PaddedRow, dated_row)


def load_csv(csvpath: str) -> List[PaddedRow]:
    with open(csvpath, "r", encoding="utf-8", newline="") as fp:
        rows = csv.reader(fp, delimiter=";")
        header = next(rows)
        assert tuple(header) == Invoice.headers
        return [parse_date(row) for row in rows]


def create_test_method(
    pdfpath: str,
    csvpath: str,
    method_name: Optional[str] = None,
) -> TestMethod:
    def method(self: unittest.TestCase) -> None:
        doc = popplerqt5.Poppler.Document.load(pdfpath)
        try:
            invoice = MonospaceInvoice(doc)  # type: Invoice
        except AssertionError:
            invoice = NewInvoice(doc)
        try:
            expected = load_csv(csvpath)

            records = list(invoice)
            i = 0
            for record in records:
                self.assertTrue(
                    i < len(expected),
                    f"got unexpected records in {pdfpath!r}:\n{pprint.pformat(records[i:])}",
                )
                self.assertEqual(record, expected[i])
                i += 1
            self.assertEqual(
                i,
                len(expected),
                f"missing records in {pdfpath!r}:\n{pprint.pformat(expected[i:])}",
            )
        finally:
            dest = os.environ.get("SPLENDID_INVOICE_OUTPUT_DIR", "")
            if dest:
                # write PDF to $SPLENDID_INVOICE_OUTPUT_DIR
                if method_name is None:
                    basename = os.path.basename(pdfpath)
                else:
                    basename = method_name + ".pdf"
                conv = doc.pdfConverter()
                conv.setOutputFileName(os.path.join(dest, basename))
                conv.setPDFOptions(
                    popplerqt5.Poppler.PDFConverter.PDFOption.WithChanges
                )
                assert conv.convert()

    method.__doc__ = os.path.basename(pdfpath)
    return method


def create_testcase_class(
    class_name: str,
    directory: str = os.path.join(os.path.dirname(__file__), "splendid"),
) -> Type[unittest.TestCase]:
    methods = {}  # type: Dict[str, TestMethod]
    with os.scandir(directory) as it:
        for pdf in it:
            if pdf.name.endswith(".pdf"):
                csvpath = pdf.path[:-3] + "csv"
                if os.path.exists(csvpath):
                    method_name = filename_to_test_method_name(pdf.name)
                    assert method_name not in methods, (
                        f"duplicate method name: {method_name}"
                    )
                    methods[method_name] = create_test_method(
                        pdf.path,
                        csvpath,
                        method_name,
                    )
    return type(class_name, (unittest.TestCase,), methods)


Splendid = create_testcase_class("Splendid")
