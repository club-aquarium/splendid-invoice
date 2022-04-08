"""
splendid-invoice
Copyright (C) 2022  schnusch

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
import bisect
import csv
import math
import sys
from dataclasses import dataclass
from datetime import date, datetime
from typing import Iterator, List, Optional, TextIO, Tuple, Type, TypeVar, cast

import popplerqt5  # type: ignore


def approx_gcd(a: Optional[float], b: float) -> float:
    tolerance = 0.01

    if a is None or math.isclose(a, 0, rel_tol=tolerance):
        return b
    elif math.isclose(b, 0, rel_tol=tolerance):
        return a

    adiv, bdiv = 1, 1
    while not math.isclose(a / adiv, b / bdiv, rel_tol=tolerance):
        if a / adiv < b / bdiv:
            a, b = b, a
            adiv, bdiv = bdiv, adiv
        adiv += 1
    return (a / adiv + b / bdiv) / 2


@dataclass
class GridSpace:
    y: int
    x: int
    _h: int
    _w: int

    def __lt__(self, other: "GridSpace") -> bool:
        for attr in ("y", "x", "_h", "_w"):
            a = getattr(self, attr)
            b = getattr(other, attr)
            if a < b:
                return True
            elif a > b:
                return False
        return False

    @property
    def width(self) -> int:
        return -self._w

    @property
    def height(self) -> int:
        return -self._h


GridTextBox = Tuple[GridSpace, popplerqt5.Poppler.TextBox]
T = TypeVar("T", bound="TextGrid")


class TextGrid:
    @classmethod
    def from_page(cls: Type[T], page: popplerqt5.Poppler.Page) -> T:
        return cls(page.textList())

    def __init__(self, boxes: List[popplerqt5.Poppler.TextBox]):
        self._guess_grid_offset(boxes)
        self._guess_grid(boxes)
        self.text_boxes = []  # type: List[GridTextBox]
        for box in boxes:
            bisect.insort(self.text_boxes, (self._to_grid(box), box))

    def _guess_grid_offset(self, boxes: List[popplerqt5.Poppler.TextBox]) -> None:
        """Find the very top and very left text boxes to find an origin for
        the grid.
        """
        offx = offy = None  # type: Optional[float]
        for box in boxes:
            bbox = box.boundingBox()
            x, y = bbox.left(), bbox.top()
            offx = x if offx is None else min(offx, x)
            offy = y if offy is None else min(offy, y)
        assert offx is not None and offy is not None
        self.gridoffx = offx
        self.gridoffy = offy

    def _guess_grid(self, boxes: List[popplerqt5.Poppler.TextBox]) -> None:
        """Using a text boxes vertical position relative to the very top
        text box works best for line height.

        Inversely using a text boxes width instead of its relative
        horizontal position works best for the character width.
        """
        gridw = gridh = None  # type: Optional[float]
        for box in boxes:
            bbox = box.boundingBox()
            y = bbox.top()
            w = bbox.width()
            # gridw = approx_gcd(gridw, x - self.gridoffx)
            gridh = approx_gcd(gridh, y - self.gridoffy)
            gridw = approx_gcd(gridw, w)
            # gridh = approx_gcd(gridh, h)
        assert gridw is not None and gridh is not None
        self.gridx = gridw
        self.gridy = gridh

    def _to_grid(self, box: popplerqt5.Poppler.TextBox) -> GridSpace:
        bbox = box.boundingBox()
        x = int(round((bbox.left() - self.gridoffx) / self.gridx))
        y = int(round((bbox.top() - self.gridoffy) / self.gridy))
        w = int(round(bbox.width() / self.gridx))
        h = int(round(bbox.height() / self.gridy))
        assert h == 1, f"h == {1} expected for monospace font"
        assert (
            len(box.text()) == w
        ), f"len({repr(box.text())}) == {w} expected for monospace font"
        return GridSpace(y, x, -h, -w)

    def iter_rows(self) -> Iterator[List[GridTextBox]]:
        y = 0
        row = []  # type: List[GridTextBox]
        for g, box in self.text_boxes:
            if g.y != y:
                if row:
                    yield row
                    row = []
                y = g.y
            row.append((g, box))
        if row:
            yield row

    def _color_used_char(
        self, x: Tuple[str, Optional[popplerqt5.Poppler.TextBox]]
    ) -> str:
        c, box = x
        if box is None or not getattr(box, "used", False):
            return c
        return f"\x1b[33m{c}\x1b[39m"

    def get_used_text(self, space: str = " ") -> str:
        chars = []  # type: List[List[Tuple[str, Optional[popplerqt5.Poppler.TextBox]]]]
        for g, box in self.text_boxes:
            while g.y >= len(chars):
                chars.append([])
            row = chars[g.y]
            while g.x + g.width >= len(row):
                row.append((" ", None))
            for i, c in enumerate(box.text(), start=g.x):
                row[i] = (c, box)
            if box.hasSpaceAfter():
                row[g.x + g.width] = (space, None)
        return "\n".join("".join(map(self._color_used_char, row)) for row in chars)


ParsedRow = Tuple[
    str,  # Artikel
    str,  # Bezeichnung
    str,  # Inhalt
    str,  # Anzahl
    str,  # Menge
    str,  # Preis
    str,  # Betrag
]

PaddedRow = Tuple[
    date,  # Leistungsdatum
    str,  # Lieferschein
    date,  # Rechnungsdatum
    str,  # Rechnungs-Nr.
    str,  # Artikel
    str,  # Bezeichnung
    str,  # Inhalt
    str,  # Anzahl
    str,  # Menge
    str,  # Preis
    str,  # Betrag
]


class InvoicePage(TextGrid):
    columns = [
        (0, 10),
        (9, 42),
        (39, 50),
        (48, 56),
        (56, 66),
        (65, None),
    ]  # type: List[Tuple[int, Optional[int]]]

    @staticmethod
    def is_table_header(row: List[GridTextBox]) -> bool:
        expected = {
            "Artikel",
            "Bezeichnung",
            "Inhalt",
            "Menge",
            "Preis",
            "Betrag",
            "EUR",
        }
        got = set(box.text() for _, box in row)
        return expected <= got

    @staticmethod
    def contains_underscore_line(row: List[GridTextBox]) -> bool:
        for g, box in row:
            if all(map("_".__eq__, box.text())):
                return True
        return False

    def _find_text(self, text: str) -> popplerqt5.Poppler.TextBox:
        for _, box in self.text_boxes:
            if box.text() == text:
                return box
        raise ValueError(f"cannot find {repr(text)}")

    def get_delivery_info(self) -> Tuple[str, date]:
        id = self._find_text("Lieferschein").nextWord()
        date = self._find_text("Leistungsdatum").nextWord()
        id.used = True
        date.used = True
        return (
            id.text(),
            datetime.strptime(date.text().split("/", 1)[0], "%d.%m.%y").date(),
        )

    def get_invoice_info(self) -> Tuple[str, date]:
        invoice = self._find_text("Rechnungs-Nr.").nextWord()
        vom = invoice.nextWord()
        assert vom.text() == "vom"
        date = vom.nextWord()
        invoice.used = True
        date.used = True
        return (
            invoice.text(),
            datetime.strptime(date.text(), "%d.%m.%Y").date(),
        )

    @classmethod
    def _sort_into_columns(
        cls, row: List[GridTextBox]
    ) -> List[List[popplerqt5.Poppler.TextBox]]:
        cols = [[] for _ in cls.columns]  # type: List[List[GridTextBox]]
        for g, box in row:
            for col, (left, right) in zip(cols, cls.columns):
                if left <= g.x and (right is None or g.x + g.width <= right):
                    col.append(box)
        return cols

    def _split_count(self, count: str) -> List[str]:
        parts = count.split(maxsplit=1)
        if len(parts) < 2:
            return ["", count]
        try:
            int(parts[0], 10)
        except ValueError:
            return ["", count]
        return parts

    def _format_columns(
        self, columns: List[List[popplerqt5.Poppler.TextBox]]
    ) -> ParsedRow:
        row = []
        for col in columns:
            texts = []
            for box in col:
                texts.append(box.text())
                box.used = True
            row.append(" ".join(texts))
        row[3:4] = self._split_count(row[3])
        return cast(ParsedRow, tuple(row))

    def parse_table(self) -> Iterator[ParsedRow]:
        rows = self.iter_rows()
        # skip header
        for row in rows:
            if self.is_table_header(row):
                break

        prev_columns = None
        for row in rows:
            # end on next header
            if self.contains_underscore_line(row):
                break

            columns = self._sort_into_columns(row)
            if not columns[0]:
                # article ID unset
                if not columns[1]:
                    # description unset, ignore
                    pass
                elif prev_columns is not None:
                    # append to previous row
                    for prev_col, col in zip(prev_columns, columns):
                        prev_col.extend(col)
            else:
                if prev_columns is not None and any(map(bool, prev_columns)):
                    yield self._format_columns(prev_columns)
                prev_columns = columns

        if prev_columns is not None and any(map(bool, prev_columns)):
            yield self._format_columns(prev_columns)


class Invoice:
    headers = (
        "Leistungsdatum",
        "Lieferschein",
        "Rechnungsdatum",
        "Rechnungs-Nr.",
        "Artikel",
        "Bezeichnung",
        "Inhalt",
        "Anzahl",
        "Menge",
        "Preis",
        "Betrag",
    )

    @classmethod
    def load(cls, name: str) -> "Invoice":
        return cls(popplerqt5.Poppler.Document.load(name))

    def __init__(self, doc: popplerqt5.Poppler.Document):
        self.pages = [
            InvoicePage.from_page(doc.page(i)) for i in range(len(doc))
        ]  # type: List[InvoicePage]

    def __iter__(self) -> Iterator[PaddedRow]:
        delivery_id = ""
        delivery_date = cast(date, "")
        for page in self.pages:
            try:
                delivery_id, delivery_date = page.get_delivery_info()
            except ValueError:
                pass
            invoice_id, invoice_date = page.get_invoice_info()
            for row in page.parse_table():
                padded_row = (
                    delivery_date,
                    delivery_id,
                    invoice_date,
                    invoice_id,
                    *row,
                )  # type: PaddedRow
                assert len(padded_row) == len(self.headers)
                yield padded_row

    def print_pages(self) -> None:
        for page in self.pages:
            print(page.get_used_text(), file=sys.stderr)
            print(file=sys.stderr)


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
    p = argparse.ArgumentParser(description="Parse PDF invoices from Splendid Drinks")
    p.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print parsed PDF to standard error.",
    )
    p.add_argument("invoice", nargs="+", metavar="<invoice>")
    args = p.parse_args(argv)

    first = True
    for name in args.invoice:
        csv_from_pdf(
            sys.stdout,
            Invoice.load(name),
            write_headers=first,
            print_pages=args.verbose,
        )
        first = False
