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
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from functools import cached_property
from itertools import zip_longest
from heapq import merge
from typing import (
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    cast,
)

import popplerqt5  # type: ignore


def open_stdout() -> TextIO:
    return open(
        sys.stdout.fileno(), "w", encoding="iso-8859-1", newline="", closefd=False
    )


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
        for g, box in self.text_boxes:  # they are sorted by Y-coordinate
            while y < g.y:
                yield row
                row = []
                y += 1
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


class InvoicePage:
    def get_delivery_info(self) -> Tuple[str, date]:
        raise NotImplementedError

    def get_invoice_info(self) -> Tuple[str, date]:
        raise NotImplementedError

    def parse_table(self) -> Iterator[ParsedRow]:
        raise NotImplementedError

    def print_page(self, fileobj: TextIO) -> None:
        raise NotImplementedError


class MonospaceInvoicePage(InvoicePage, TextGrid):
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

    @staticmethod
    def text_equals(row: List[GridTextBox], text: str) -> bool:
        row_text = " ".join(b.text() for _, b in row)
        return row_text == text

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
        """Sort text boxes into columns. The text box has to start and end
        in the same column, otherwise it is discarded.
        """
        cols = [[] for _ in cls.columns]  # type: List[List[GridTextBox]]
        for g, box in row:
            for col, (left, right) in zip(cols, cls.columns):
                if left <= g.x and (right is None or g.x + g.width <= right):
                    col.append(box)
        return cols

    def _split_count(self, count: str) -> List[str]:
        m = re.match(r"^(\d+)(-)? *(.*)$", count)
        if m is None:
            return ["", count]
        count, minus, unit = m.groups()
        if minus is not None:
            count = "-" + count
        return [count, unit]

    def _format_columns(
        self, columns: List[List[popplerqt5.Poppler.TextBox]]
    ) -> ParsedRow:
        """Join column texts to string and split units from the column
        "Anzahl" into a separate column.
        """
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
        """This iterates over the text boxes row by row and tries to sort
        them into each of their six columns. Rows with an empty first
        column/missing an article number are appended to the previous row.

        TODO handle pages with multiple deliveries. Currently the second
        "Lieferschein ... Lieferdarum ..." is added to its above article.
        """

        rows = self.iter_rows()

        # skip until table head
        for row in rows:
            if self.is_table_header(row):
                break

        prev_columns = None
        for row in rows:
            # empty row finishes the previous record, begin a new
            if not row:
                if prev_columns is not None and any(map(bool, prev_columns)):
                    yield self._format_columns(prev_columns)
                prev_columns = None
                continue

            if self.text_equals(
                row, "Das Datum der Lieferung entspricht dem Datum des Lieferscheines."
            ):
                continue

            # end on next header
            if self.contains_underscore_line(row):
                break

            columns = self._sort_into_columns(row)
            if not columns[0]:
                # article ID unset, add to above article
                if not columns[1]:
                    # description unset, ignore
                    pass
                elif prev_columns is not None:
                    # append to previous record
                    for prev_col, col in zip(prev_columns, columns):
                        prev_col.extend(col)
            else:
                # a new article has begun
                if prev_columns is not None and any(map(bool, prev_columns)):
                    yield self._format_columns(prev_columns)
                prev_columns = columns

        if prev_columns is not None and any(map(bool, prev_columns)):
            yield self._format_columns(prev_columns)

    def print_page(self, fileobj: TextIO) -> None:
        print(self.get_used_text(), file=fileobj)


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

    def __init__(self) -> None:
        self.pages = []  # type: List[InvoicePage]

    def __iter__(self) -> Iterator[PaddedRow]:
        delivery_id = ""
        delivery_date = cast(date, "")
        for page in self.pages:
            try:
                delivery_id, delivery_date = page.get_delivery_info()
            except ValueError:
                pass
            try:
                invoice_id, invoice_date = page.get_invoice_info()
            except (AttributeError, ValueError):
                invoice_id = ""
                invoice_date = cast(date, "")
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

    def print_pages(self, fileobj: TextIO = sys.stderr) -> None:
        for page in self.pages:
            page.print_page(fileobj)
            print(file=fileobj)


class MonospaceInvoice(Invoice):
    @classmethod
    def load(cls, name: str) -> "MonospaceInvoice":
        return cls(popplerqt5.Poppler.Document.load(name))

    def __init__(self, doc: popplerqt5.Poppler.Document):
        self.pages = [
            MonospaceInvoicePage.from_page(doc.page(i)) for i in range(len(doc))
        ]  # type: List[InvoicePage]


class RowOfTextBoxes(NamedTuple):
    # having the greater value first allows us to use bisect
    bottom: float
    top: float
    # by using a tuple we can use bisect
    boxes: List[Tuple[float, int, popplerqt5.Poppler.TextBox]]


class TableColumn(NamedTuple):
    # having the greater value first allows us to use bisect
    right: float
    left: float


def join_rows(a: RowOfTextBoxes, b: RowOfTextBoxes) -> RowOfTextBoxes:
    return RowOfTextBoxes(
        bottom=max(a.bottom, b.bottom),
        top=max(a.top, b.top),
        boxes=list(merge(a.boxes, b.boxes, key=lambda x: x[0])),
    )


def only_starts_of_next_word_chains(
    boxes: List[popplerqt5.Poppler.TextBox],
) -> Set[popplerqt5.Poppler.TextBox]:
    all = set(boxes)
    starts = set()  # type: Set[popplerqt5.Poppler.TextBox]
    while True:
        try:
            tbox = all.pop()
        except KeyError:
            break
        starts.add(tbox)
        tbox = tbox.nextWord()
        while tbox:
            all.discard(tbox)
            starts.discard(tbox)
            tbox = tbox.nextWord()
    return starts


def guess_columns(table: List[List[popplerqt5.Poppler.TextBox]]) -> List[TableColumn]:
    """Find common horizontal whitespace in multiple rows of text. The
    common whitespace are our column separators of the table.
    For the way this works using bisect look at NewInvoicePage._as_rows
    """
    columns = []  # type: List[TableColumn]
    for row in table:
        for tbox in row:
            # get dimensions of the next-word-chain
            bbox = tbox.boundingBox()
            left = bbox.left()
            right = bbox.right()
            tbox = tbox.nextWord()
            while tbox:
                bbox = tbox.boundingBox()
                left = min(left, bbox.left())
                right = max(right, bbox.right())
                tbox = tbox.nextWord()

            # see NewInvoicePage._as_rows
            i = bisect.bisect_left(columns, (left,))
            if i < len(columns) and columns[i].left <= right:
                column = columns[i]
                columns[i] = TableColumn(
                    right=max(column.right, right),
                    left=min(column.left, left),
                )

                # multiple columns might overlap now, see NewInvoicePage._as_rows
                for j in reversed(range(0, i)):
                    a = columns[j]
                    b = columns[i]
                    if a.left <= b.right and b.left <= a.right:
                        columns[j] = TableColumn(
                            right=max(a.right, b.right),
                            left=min(a.left, b.left),
                        )
                        columns.pop(i)
                        i -= 1
                    else:
                        break
                j = i + 1
                while j < len(columns):
                    a = columns[i]
                    b = columns[j]
                    if a.left <= b.right and b.left <= a.right:
                        columns[i] = TableColumn(
                            right=max(a.right, b.right),
                            left=min(a.left, b.left),
                        )
                        columns.pop(j)
                    else:
                        break
            else:
                columns.insert(i, TableColumn(right=right, left=left))
            assert columns[i].left < columns[i].right

    return columns


def get_column(columns: List[TableColumn], x: float) -> int:
    """Get index of column x fits into."""
    i = bisect.bisect_left(columns, (x,))
    if i < len(columns) and columns[i].left <= x:
        return i
    raise ValueError(f"{x} does not fit in columns {columns}")


def iter_row(
    row: List[popplerqt5.Poppler.TextBox],
) -> Iterator[popplerqt5.Poppler.TextBox]:
    for tbox in row:
        while tbox:
            yield tbox
            tbox = tbox.nextWord()


def row_is_words(row: List[popplerqt5.Poppler.TextBox], words: List[str]) -> bool:
    for tbox, word in zip_longest(iter_row(row), words):
        if tbox is None or word is None or tbox.text() != word:
            return False
    return True


def mark_row_as_used(row: List[popplerqt5.Poppler.TextBox]) -> None:
    for tbox in iter_row(row):
        tbox.used = True


NewColumns = Tuple[
    List[popplerqt5.Poppler.TextBox],
    List[popplerqt5.Poppler.TextBox],
    List[popplerqt5.Poppler.TextBox],
    List[popplerqt5.Poppler.TextBox],
    List[popplerqt5.Poppler.TextBox],
]


class NewInvoicePage(InvoicePage):
    def __init__(self, page: popplerqt5.Poppler.Page):
        self.text_boxes = only_starts_of_next_word_chains(page.textList())

    @cached_property
    def _as_rows(self) -> List[List[popplerqt5.Poppler.TextBox]]:
        """Sort page content into rows of text. When a TextBox overlaps with
        an existing row it is added to it and the row's size is increased to fit
        all it's TextBoxes.
        We only ever store and care for words, that start a next-word-chain,
        because it's followers are assumed to belong to the same row. But they
        are included when increasing a row's height.
        """
        rows = []  # type: List[RowOfTextBoxes]
        for tbox in self.text_boxes:
            bbox = tbox.boundingBox()

            # To check if two intervals overlap we test if
            #     a.top <= b.bottom && b.top <= a.bottom
            # where a is the bbox to insert and b is one of the existing rows.
            # The bisect below already does a.top <= b.bottom for us.
            i = bisect.bisect_left(rows, (bbox.top(),))
            if i < len(rows) and rows[i].top <= bbox.bottom():
                row = rows[i]
                top = row.top
                bottom = row.bottom
                # because we only get words, that start a next-word-chain,
                # we add it's followers to the rows bounding box
                word = tbox
                while word:
                    word_bbox = word.boundingBox()
                    top = min(top, word_bbox.top())
                    bottom = max(bottom, word_bbox.bottom())
                    word = word.nextWord()
                # use an ever increasing 2nd member so bisect never compares TextBox
                bisect.insort(row.boxes, (bbox.left(), len(row.boxes), tbox))
                rows[i] = RowOfTextBoxes(bottom=bottom, top=top, boxes=row.boxes)

                # multiple rows might overlap now
                for j in reversed(range(0, i)):
                    a = rows[j]
                    b = rows[i]
                    if a.top <= b.bottom and b.top <= a.bottom:
                        rows[j] = join_rows(rows[j], rows[i])
                        rows.pop(i)
                        i -= 1
                    else:
                        break
                j = i + 1
                while j < len(rows):
                    a = rows[i]
                    b = rows[j]
                    if a.top <= b.bottom and b.top <= a.bottom:
                        rows[i] = join_rows(rows[i], rows[j])
                        rows.pop(j)
                    else:
                        break
            else:
                rows.insert(
                    i,
                    RowOfTextBoxes(
                        bottom=bbox.bottom(),
                        top=bbox.top(),
                        boxes=[(bbox.left(), 0, tbox)],
                    ),
                )
            assert rows[i].top < rows[i].bottom

        return [[tbox for _, _, tbox in row.boxes] for row in rows]

    def get_delivery_info(self) -> Tuple[str, date]:
        number_next = False
        delivery_number = None  # type: Optional[popplerqt5.Poppler.TextBox]
        for row in self._as_rows:
            for tbox in iter_row(row):
                if tbox.text() == "Lfs.:":
                    number_next = True
                elif number_next:
                    delivery_number = tbox
                    number_next = False
                elif delivery_number:
                    try:
                        parsed_date = datetime.strptime(tbox.text(), "%d.%m.%Y").date()
                    except ValueError:
                        pass
                    else:
                        delivery_number.used = True
                        tbox.used = True
                        return (delivery_number.text(), parsed_date)

        raise ValueError("cannot find delivery info")

    def get_invoice_info(self) -> Tuple[str, date]:
        invoice_number = None  # type: Optional[popplerqt5.Poppler.TextBox]
        invoice_date = None  # type: Optional[popplerqt5.Poppler.TextBox]
        parsed_date = None  # type: Optional[date]

        rechnung = ["R", "E", "C", "H", "N", "U", "N", "G:"]
        i = 0
        date_next = False
        for row in self._as_rows:
            for tbox in iter_row(row):
                if not invoice_number:
                    if i == len(rechnung):
                        invoice_number = tbox
                    elif tbox.text() == rechnung[i]:
                        i += 1
                    else:
                        i = int(tbox.text() == rechnung[0])

                if not invoice_date:
                    if date_next:
                        try:
                            parsed_date = datetime.strptime(
                                tbox.text(), "%d.%m.%Y"
                            ).date()
                        except ValueError:
                            pass
                        else:
                            invoice_date = tbox
                    date_next = tbox.text() == "Rechnungsdatum:"

                if invoice_number and invoice_date and parsed_date:
                    invoice_number.used = True
                    invoice_date.used = True
                    return (invoice_number.text(), parsed_date)

        raise ValueError("cannot find invoice info")

    @staticmethod
    def _format_columns(row: NewColumns) -> ParsedRow:
        formatted = []  # type: List[str]
        for tboxes in row:
            s = ""
            for tbox in tboxes:
                while tbox:
                    s += tbox.text()
                    if tbox.hasSpaceAfter():
                        s += " "
                    tbox.used = True
                    tbox = tbox.nextWord()
            formatted.append(s)
        amount = formatted[2].rsplit(maxsplit=1)
        while len(amount) < 2:
            amount.append("")
        price = formatted[3].rsplit("/", 1)[0]
        return (
            formatted[0],
            formatted[1],
            "",
            amount[0],
            amount[1],
            price,
            formatted[4],
        )

    def parse_table(self) -> Iterator[ParsedRow]:
        # find start of table
        rows = iter(self._as_rows)
        for row in rows:
            if row_is_words(
                row,
                ["Artikel", "Menge", "Einheit", "Preis", "Wert", "EUR"],
            ):
                mark_row_as_used(row)
                break
        else:
            return  # cannot find table header

        # skip leading text
        for row in rows:
            if row_is_words(row, ["Verkauf"]):
                mark_row_as_used(row)
                break
        else:
            raise ValueError("cannot find end of leading text in table")

        # collect rows of table
        table = []  # type: List[List[popplerqt5.Poppler.TextBox]]
        for row in rows:
            if row_is_words(row, ["Leergutlieferung"]) or row_is_words(
                row,
                [
                    "Leergutartikel",
                    "Lieferung",
                    "Rückgabe",
                    "Differenz",
                    "Pfand",
                    "Wert",
                ],
            ):
                mark_row_as_used(row)
                break
            table.append(row)

        columns = guess_columns(table)
        assert (
            len(columns) == 5
        ), f"expected table to have 5 columns, got {len(columns)}"

        combined_row = ([], [], [], [], [])  # type: NewColumns
        for row in table:
            parsed_row = ([], [], [], [], [])  # type: NewColumns
            for tbox in row:
                bbox = tbox.boundingBox()
                try:
                    i = get_column(columns, bbox.left())
                except ValueError:
                    raise ValueError(
                        "{repr(tbox.text())} ({repr(bbox)}) does not fit in the table"
                    )
                parsed_row[i].append(tbox)
            if (
                not parsed_row[0]
                and not parsed_row[2]
                and not parsed_row[3]
                and not parsed_row[4]
            ):
                # add incomplete rows to the previous
                combined_row[1].extend(parsed_row[1])
            else:
                if any(map(bool, combined_row)):
                    yield self._format_columns(combined_row)
                combined_row = parsed_row
        if any(map(bool, combined_row)):
            yield self._format_columns(combined_row)

    def print_page(self, fileobj: TextIO) -> None:
        print("NewInvoicePage.print_page() not yet implemented.", file=fileobj)


class NewInvoice(Invoice):
    @classmethod
    def load(cls, name: str) -> "NewInvoice":
        return cls(popplerqt5.Poppler.Document.load(name))

    def __init__(self, doc: popplerqt5.Poppler.Document):
        self.pages = [
            NewInvoicePage(doc.page(i)) for i in range(len(doc))
        ]  # type: List[InvoicePage]


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

    with open_stdout() as stdout:
        first = True
        for name in args.invoice:
            try:
                invoice = MonospaceInvoice.load(name)  # type: Invoice
            except AssertionError:
                invoice = NewInvoice.load(name)
            csv_from_pdf(
                stdout,
                invoice,
                write_headers=first,
                print_pages=args.verbose,
            )
            first = False


if __name__ == "__main__":
    main()
