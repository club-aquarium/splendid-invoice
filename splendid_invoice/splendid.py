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

import bisect
import math
import os
import re
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date, datetime
from functools import partial
from heapq import merge
from itertools import islice, zip_longest
from typing import Mapping  # noqa: F401
from typing import (
    Any,
    Callable,
    Iterator,
    List,
    Literal,
    NamedTuple,
    Optional,
    Set,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
)

import popplerqt5  # type: ignore
from PyQt5.QtCore import QRectF, QSizeF  # type: ignore
from PyQt5.QtGui import QColor  # type: ignore

from .base import (
    Invoice,
    InvoicePage,
    PaddedRow,
    ParsedRow,
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


U = TypeVar("U")


def last(it: Iterator[U], default: Optional[U] = None) -> Optional[U]:
    for default in it:
        pass
    return default


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


DeliveryInfo = Tuple[str, date]


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

    def get_delivery_info(self) -> DeliveryInfo:
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
        row.append("")
        assert len(row) == len(cast(Any, ParsedRow).__args__)
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
    top: float
    bottom: float


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


def union_table_columns(a: TableColumn, b: TableColumn) -> TableColumn:
    return TableColumn(
        left=min(a.left, b.left),
        top=min(a.top, b.top),
        right=max(a.right, b.right),
        bottom=max(a.bottom, b.bottom),
    )


def get_word_chain_dimensions(tbox: popplerqt5.Poppler.TextBox) -> TableColumn:
    # get dimensions of the next-word-chain
    dim = TableColumn(
        left=math.inf,
        top=math.inf,
        right=-math.inf,
        bottom=-math.inf,
    )
    while tbox:
        bbox = tbox.boundingBox()
        dim = union_table_columns(
            dim,
            TableColumn(
                left=bbox.left(),
                top=bbox.top(),
                right=bbox.right(),
                bottom=bbox.bottom(),
            ),
        )
        tbox = tbox.nextWord()
    assert not math.isinf(dim.left)
    return dim


Row = List[popplerqt5.Poppler.TextBox]


def get_closest_column_indexes(dims: List[TableColumn]) -> Tuple[int, int]:
    distance = None  # type: Optional[float]
    closest = None  # type: Optional[Tuple[int, int]]
    for i, acol in enumerate(dims):
        for j, bcol in enumerate(dims[:i]):
            d = min(
                abs(bcol.left - acol.right),
                abs(acol.left - bcol.right),
            )
            if distance is None or d < distance:
                distance = d
                closest = (i, j)
    assert closest is not None
    return closest


def join_closest_columns_inplace(
    row: List[Tuple[TableColumn, List[popplerqt5.Poppler.TextBox]]],
) -> None:
    i, j = get_closest_column_indexes([dim for dim, _ in row])
    row[i] = (
        union_table_columns(row[i][0], row[j][0]),
        row[i][1] + row[j][1],
    )
    row.pop(j)


def guess_columns(
    table: List[Row],
    page: Optional[popplerqt5.Poppler.Page] = None,
) -> List[TableColumn]:
    """Find common horizontal whitespace in multiple rows of text. The
    common whitespace are our column separators of the table.
    For the way this works using bisect look at NewInvoice._as_rows
    """
    columns = []  # type: List[TableColumn]
    for row in table:
        # In Rechnung_R360251231.pdf article name and unit size are split into
        # two columns, so we join the closest columns together until 5 columns
        # are left.
        # We cannot add words to a wordchain so we have to convert every column
        # to a list of start words.
        row_columns = [
            (get_word_chain_dimensions(tbox), [tbox]) for tbox in row
        ]  # type: List[Tuple[TableColumn, List[popplerqt5.Poppler.TextBox]]]
        while len(row_columns) > 5:
            join_closest_columns_inplace(row_columns)

        # We expect our table to have at least 5 columns. If we find less than
        # 5 next-word-chains, we treat the row as suspicious and ignore it, if
        # it would cause us to union columns together.
        suspicious = len(row_columns) != 5

        for dim, tboxes in row_columns:
            # see NewInvoice._as_rows
            i = bisect.bisect_left(columns, (dim.left,))
            if i < len(columns) and columns[i].left <= dim.right:
                old_column = columns[i]
                columns[i] = union_table_columns(old_column, dim)

                class DoNotUnion(Exception):
                    pass

                try:
                    # multiple columns might overlap now, see NewInvoice._as_rows
                    for j in reversed(range(0, i)):
                        a = columns[j]
                        b = columns[i]
                        if a.left <= b.right and b.left <= a.right:
                            if suspicious:
                                # Do not allow unions caused by suspicious rows.
                                raise DoNotUnion
                            else:
                                columns[j] = union_table_columns(a, b)
                                columns.pop(i)
                                i -= 1
                        else:
                            break
                    j = i + 1
                    while j < len(columns):
                        a = columns[i]
                        b = columns[j]
                        if a.left <= b.right and b.left <= a.right:
                            if suspicious:
                                # Do not allow unions caused by suspicious rows.
                                raise DoNotUnion
                            else:
                                columns[i] = union_table_columns(a, b)
                                columns.pop(j)
                        else:
                            break
                except DoNotUnion:
                    columns[i] = old_column
            elif not suspicious:
                columns.insert(i, dim)
            assert columns[i].left < columns[i].right

    for i, c in enumerate(columns):
        add_annotation(
            page,
            (c.left, c.top),
            (c.right, c.bottom),
            f"guess_columns: {i}",
            color_env="SPLENDID_INVOICE_ANNOTATION_COLOR_COLUMN",
        )

    return columns


def get_column(columns: List[TableColumn], left: float, right: float) -> int:
    """Get index of column x fits into."""
    i = bisect.bisect_left(columns, (left,))
    if i < len(columns) and columns[i].left <= left and right <= columns[i].right:
        return i
    raise ValueError(f"{left} does not fit in columns {columns}")


def iter_row(row: Row) -> Iterator[popplerqt5.Poppler.TextBox]:
    for tbox in row:
        while tbox:
            yield tbox
            tbox = tbox.nextWord()


def row_is_words(row: Row, words: List[str]) -> bool:
    for tbox, word in zip_longest(iter_row(row), words):
        if tbox is None or word is None or tbox.text() != word:
            return False
    return True


def row_startswith_words(row: Row, words: List[str]) -> bool:
    for tbox, word in zip_longest(iter_row(row), words):
        if word is None:
            break
        elif tbox is None or tbox.text() != word:
            return False
    return True


def page_relative_qrectf(
    rect: QRectF,
    page_size: QSizeF,
) -> QRectF:
    """Annotations coordinates are relative to the page size, ((0,0) is top-left,
    (1,1) is bottom-right) see https://poppler.freedesktop.org/api/qt5/classPoppler_1_1Annotation.html#annotCreation
    """
    w = page_size.width()
    h = page_size.height()
    return QRectF(
        rect.left() / w,
        rect.top() / h,
        rect.width() / w,
        rect.height() / h,
    )


RGBaColor = Tuple[int, int, int, int]


def parse_hex_rgba(
    rgba: str,
    fallback: Optional[RGBaColor] = None,
) -> RGBaColor:
    if not re.match(r"^#[0-9A-Fa-f]{8}$", rgba):
        if fallback is None:
            raise ValueError(f"cannot parse {rgba!r}")
        else:
            return fallback
    i = int(rgba[1:], 16)
    return (
        (i & 0xFF000000) >> 24,
        (i & 0x00FF0000) >> 16,
        (i & 0x0000FF00) >> 8,
        (i & 0x000000FF),
    )


AnnotationColorName = Literal[
    "SPLENDID_INVOICE_ANNOTATION_COLOR_COLUMN",
    "SPLENDID_INVOICE_ANNOTATION_COLOR_DEFAULT",
    "SPLENDID_INVOICE_ANNOTATION_COLOR_ORIENTATION",
    "SPLENDID_INVOICE_ANNOTATION_COLOR_USED",
]
default_annotation_colors = {
    "SPLENDID_INVOICE_ANNOTATION_COLOR_COLUMN": (255, 0, 255, 63),
    "SPLENDID_INVOICE_ANNOTATION_COLOR_DEFAULT": (255, 255, 0, 127),
    "SPLENDID_INVOICE_ANNOTATION_COLOR_ORIENTATION": (0, 255, 255, 127),
    "SPLENDID_INVOICE_ANNOTATION_COLOR_USED": (0, 255, 0, 127),
}  # type: Mapping[AnnotationColorName, RGBaColor]


def get_color_env(var: AnnotationColorName) -> RGBaColor:
    return parse_hex_rgba(
        os.environ.get(var, ""),
        fallback=default_annotation_colors[var],
    )


def add_annotation(
    page: popplerqt5.Poppler.Page,
    topleft: Tuple[float, float],
    bottomright: Tuple[float, float],
    content: str,
    *,
    color_env: AnnotationColorName = "SPLENDID_INVOICE_ANNOTATION_COLOR_DEFAULT",
) -> None:
    x1, y1 = topleft
    x2, y2 = bottomright
    rect = page_relative_qrectf(
        QRectF(x1, y1, (x2 - x1), (y2 - y1)),
        page.pageSizeF(),
    )
    r, g, b, alpha = get_color_env(color_env)
    color = QColor.fromRgb(r, g, b)
    annot = popplerqt5.Poppler.GeomAnnotation()
    annot.setContents(content)
    annot.setBoundary(rect)
    annot.setGeomInnerColor(color)
    style = annot.style()
    style.setColor(color)  # TODO remove border
    style.setOpacity(alpha / 255)
    annot.setStyle(style)
    page.addAnnotation(annot)


def create_annotate_tbox_funcs(
    page: popplerqt5.Poppler.Page,
    tboxes: Iterable[popplerqt5.Poppler.TextBox],
    color: AnnotationColorName,
    prefix: Optional[str] = None,
) -> List[Callable[[], None]]:
    annotations = []  # type: List[Callable[[], None]]

    for tbox in tboxes:
        if page is not None:
            bbox = tbox.boundingBox()
            annotations.append(
                partial(
                    add_annotation,
                    page,
                    (bbox.left(), bbox.top()),
                    (bbox.right(), bbox.bottom()),
                    ("" if prefix is None else prefix + ": ") + tbox.text(),
                    color_env=color,
                )
            )

    return annotations


def mark_row_as_used(
    row: Row,
    *,
    nmax: Optional[int] = None,
    page: Optional[popplerqt5.Poppler.Page] = None,
    prefix: Optional[str] = None,
    orientation: bool = False,
) -> List[Callable[[], None]]:
    if page is None:
        return []
    else:
        return create_annotate_tbox_funcs(
            page,
            islice(iter_row(row), nmax),
            color=(
                "SPLENDID_INVOICE_ANNOTATION_COLOR_ORIENTATION"
                if orientation
                else "SPLENDID_INVOICE_ANNOTATION_COLOR_USED"
            ),
            prefix=prefix,
        )


class QueuedAnnotations(object):
    """Annotations are stacked in the order they are added. This class allows
    us to delay the call to page.addAnnotation(). We want guess_columns() to
    draw its annotations first and then other annotations on top.
    """

    def __init__(self) -> None:
        self._annotations = []  # type: List[Callable[[], None]]

    def enqueue_annotation(
        self,
        row: Row,
        *,
        nmax: Optional[int] = None,
        page: Optional[popplerqt5.Poppler.Page] = None,
        prefix: Optional[str] = None,
        orientation: bool = False,
    ) -> None:
        self._annotations.extend(
            mark_row_as_used(
                row,
                nmax=nmax,
                page=page,
                prefix=prefix,
                orientation=orientation,
            )
        )

    def add_annotations(self) -> None:
        i = None  # type: Optional[int]
        try:
            for i, annotate in enumerate(self._annotations):
                annotate()
        finally:
            if i is not None:
                self._annotations = self._annotations[i:]


class TableExtractor(QueuedAnnotations):
    def __init__(self) -> None:
        super().__init__()
        self._delivery = None  # type: Optional[DeliveryInfo]
        self._subheading = None  # type: Optional[str]

    @staticmethod
    def is_table_header(row: Row) -> bool:
        return row_is_words(
            row,
            ["Artikel", "Menge", "Einheit", "Preis", "Wert", "EUR"],
        )

    def get_delivery_info(
        self,
        page: popplerqt5.Poppler.Page,
        row: Row,
    ) -> DeliveryInfo:
        number_next = False
        delivery_number = None  # type: Optional[popplerqt5.Poppler.TextBox]
        for tbox in iter_row(row):
            if tbox.text() == "Lfs.:":
                number_next = True
                self.enqueue_annotation(
                    [tbox],
                    nmax=1,
                    page=page,
                    prefix="TableExtractor.get_delivery_info",
                    orientation=True,
                )
            elif number_next:
                delivery_number = tbox
                number_next = False
            elif delivery_number:
                try:
                    parsed_date = datetime.strptime(tbox.text(), "%d.%m.%Y").date()
                except ValueError:
                    pass
                else:
                    self.enqueue_annotation(
                        [delivery_number],
                        nmax=1,
                        page=page,
                        prefix="TableExtractor.get_delivery_info",
                    )
                    self.enqueue_annotation(
                        [tbox],
                        nmax=1,
                        page=page,
                        prefix="TableExtractor.get_delivery_info",
                    )
                    return (delivery_number.text(), parsed_date)

        raise ValueError("cannot find delivery info")

    @staticmethod
    def is_table_subheading(row: Row) -> str:
        for subheading in [
            "Verkauf",
            "Leergutlieferung",
            "Gratis",
            "Rückware",
            # TODO
        ]:
            if row_is_words(row, [subheading]):
                return subheading
        for subheading in [
            "Alternativ",
            "Ersatz",
            # TODO
        ]:
            if row_startswith_words(row, [subheading]):
                return subheading
        return ""

    @staticmethod
    def is_interesting_table_subheading(subheading: str) -> bool:
        return subheading in [
            "Verkauf",
            "Gratis",
            "Rückware",
            "Alternativ",
            "Ersatz",
        ]

    @staticmethod
    def is_leergut_header(row: Row) -> bool:
        return row_is_words(
            row,
            [
                "Leergutartikel",
                "Lieferung",
                "Rückgabe",
                "Differenz",
                "Pfand",
                "Wert",
            ],
        )

    @staticmethod
    def is_end_of_delivery(row: Row) -> bool:
        return row_startswith_words(row, ["Summe", "Lieferschein"])

    def find_table_header(
        self,
        page: popplerqt5.Poppler.Page,
        irows: Iterable[Row],
    ) -> bool:
        for row in irows:
            if self.is_table_header(row):
                self.enqueue_annotation(
                    row,
                    page=page,
                    prefix="TableExtractor.find_table_header -> TableExtractor.is_table_header",
                    orientation=True,
                )
                return True
        return False

    def get_table_rows(
        self,
        page: popplerqt5.Poppler.Page,
        rows: List[Row],
    ) -> List[Tuple[Optional[DeliveryInfo], List[Row]]]:
        current = []  # type: List[Row]
        table_rows = [
            (self._delivery, current),
        ]
        irows = iter(rows)

        while self.find_table_header(page, irows):
            for row in irows:
                new_subheading = self.is_table_subheading(row)
                if new_subheading:
                    self._subheading = new_subheading
                    self.enqueue_annotation(
                        row,
                        nmax=1,
                        page=page,
                        prefix="TableExtractor.get_table_rows -> TableExtractor.is_table_subheading",
                        orientation=True,
                    )
                elif self.is_leergut_header(row):
                    self.enqueue_annotation(
                        row,
                        page=page,
                        prefix="TableExtractor.get_table_rows -> TableExtractor.is_leergut_header",
                        orientation=True,
                    )
                    # If Leergut started, there must be a new table header
                    # before a new delivery can start, so we can skip to the
                    # next find_table_header.
                    self._delivery = None
                    self._subheading = None
                    break
                elif self.is_end_of_delivery(row):
                    self.enqueue_annotation(
                        row,
                        nmax=2,
                        page=page,
                        prefix="TableExtractor.get_table_rows -> TableExtractor.is_end_of_delivery",
                        orientation=True,
                    )
                    # If the delivery does not contain any Leergut, the next
                    # delivery will start without a new table header.
                    # So we do not break but continue on.
                    self._delivery = None
                    self._subheading = None
                elif self._subheading is None:
                    try:
                        self._delivery = self.get_delivery_info(page, row)
                    except ValueError:
                        pass
                    else:
                        # omit empty deliveries
                        if current:
                            current = []
                            table_rows.append((self._delivery, current))
                        else:
                            table_rows[-1] = (self._delivery, current)
                elif self.is_interesting_table_subheading(self._subheading):
                    current.append(row)

        if not current:
            assert table_rows.pop()[1] is current

        return table_rows


NewColumns = Tuple[
    Row,
    List[Union[popplerqt5.Poppler.TextBox, str]],
    Row,
    Row,
    Row,
]


# we use the look-behind as well as the \b at the beginning to match these as well:
# "Bulmers Original Cid.EW12x0,50"
# "Kolle Mate Bio20x0,50"
# "Quartiermeister Pils Bio20x0,50"
size_regex = re.compile(r"(?:\b|(?<=\bBio)|(?<=\bEW))((?:\d+x)*\d+(?:,\d+)?)l?\b")


def extract_size(name: str) -> Tuple[str, str]:
    # re.search will return the first match, but we want the last
    m = last(size_regex.finditer(name))
    if m is None:
        return (name, "")
    i, j = m.span()
    size = m[1]
    suffix = name[j:].lstrip(" ")
    if suffix.startswith("EUR") or suffix.startswith("%"):
        return (name, "")
    elif i == 0:
        return (suffix, size)
    else:
        prefix = name[:i].rstrip(" ")
        if j == len(name):
            return (prefix, size)
        else:
            return (prefix + " " + suffix, size)


class NewInvoice(Invoice, QueuedAnnotations):
    @classmethod
    def load(cls, name: str) -> "NewInvoice":
        return cls(popplerqt5.Poppler.Document.load(name))

    def __init__(self, doc: popplerqt5.Poppler.Document):
        QueuedAnnotations.__init__(self)
        self._page_rows = []  # type: List[Tuple[popplerqt5.Poppler.Page, List[Row]]]
        for i in range(len(doc)):
            page = doc.page(i)
            self._page_rows.append(
                (page, self._as_rows(only_starts_of_next_word_chains(page.textList())))
            )
        self._invoice_id, self._invoice_date = self.get_invoice_info()
        self._table_extractor = TableExtractor()
        # expected to exist
        self.pages = []  # type: List[InvoicePage]

    @staticmethod
    def _as_rows(text_boxes: Set[popplerqt5.Poppler.TextBox]) -> List[Row]:
        """Sort page content into rows of text. When a TextBox overlaps with
        an existing row it is added to it and the row's size is increased to fit
        all it's TextBoxes.
        We only ever store and care for words, that start a next-word-chain,
        because it's followers are assumed to belong to the same row. But they
        are included when increasing a row's height.
        """
        rows = []  # type: List[RowOfTextBoxes]
        for tbox in text_boxes:
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

    def get_invoice_info(self) -> Tuple[str, date]:
        invoice_number = None  # type: Optional[popplerqt5.Poppler.TextBox]
        invoice_date = None  # type: Optional[popplerqt5.Poppler.TextBox]
        parsed_date = None  # type: Optional[date]

        rechnung = ["R", "E", "C", "H", "N", "U", "N", "G:"]
        i = 0
        date_next = False
        for page, page_rows in self._page_rows:
            for row in page_rows:
                for tbox in iter_row(row):
                    if not invoice_number:
                        if i == len(rechnung):
                            invoice_number = tbox
                        elif tbox.text() == rechnung[i]:
                            i += 1
                            self.enqueue_annotation(
                                [tbox],
                                nmax=1,
                                page=page,
                                prefix="NewInvoice.get_invoice_info",
                                orientation=True,
                            )
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
                        if date_next:
                            self.enqueue_annotation(
                                [tbox],
                                nmax=1,
                                page=page,
                                prefix="NewInvoice.get_invoice_info",
                                orientation=True,
                            )

                    if invoice_number and invoice_date and parsed_date:
                        self.enqueue_annotation(
                            [invoice_number],
                            nmax=1,
                            page=page,
                            prefix="NewInvoice.get_invoice_info",
                        )
                        self.enqueue_annotation(
                            [invoice_date],
                            nmax=1,
                            page=page,
                            prefix="NewInvoice.get_invoice_info",
                        )
                        return (invoice_number.text(), parsed_date)

        raise ValueError("cannot find invoice info")

    @staticmethod
    def _format_columns(row: NewColumns) -> ParsedRow:
        formatted = []  # type: List[str]
        for tboxes in row:
            s = ""
            for tbox in tboxes:
                if isinstance(tbox, str):
                    s += tbox
                else:
                    while tbox:
                        s += tbox.text()
                        if tbox.hasSpaceAfter():
                            s += " "
                        tbox = tbox.nextWord()
            formatted.append(s)

        amount = formatted[2].rsplit(maxsplit=1)
        while len(amount) < 2:
            amount.append("")

        price = formatted[3].rsplit("/", 1)[0]

        name, size = extract_size(formatted[1])

        return (
            formatted[0],
            name,
            size,
            amount[0],
            amount[1],
            price,
            formatted[4],
            "",
        )

    def _pad_rows(
        self,
        rows: Iterable[ParsedRow],
        delivery_date: Optional[date],
        delivery_id: str,
    ) -> Iterator[PaddedRow]:
        for row in rows:
            yield (
                delivery_date,
                delivery_id,
                self._invoice_date,
                self._invoice_id,
                *row,
            )

    def __iter__(self) -> Iterator[PaddedRow]:
        for page, page_rows in self._page_rows:
            for delivery, rows in self._table_extractor.get_table_rows(page, page_rows):
                delivery_id, delivery_date = delivery or (
                    "",
                    None,
                )  # type: Tuple[str, Optional[date]]

                columns = guess_columns(rows, page)
                assert (
                    len(columns) == 5
                ), f"expected table to have 5 columns, got {len(columns)}"

                yield from self._pad_rows(
                    self._parse_table(columns, rows, page),
                    delivery_date,
                    delivery_id,
                )

            self._table_extractor.add_annotations()
            self.add_annotations()

    def _parse_table(
        self,
        columns: List[TableColumn],
        rows: Iterable[Row],
        page: popplerqt5.Poppler.Page,
    ) -> Iterator[ParsedRow]:
        combined_row = ([], [], [], [], [])  # type: NewColumns
        for row in rows:
            parsed_row = ([], [], [], [], [])  # type: NewColumns
            for tbox in row:
                dim = get_word_chain_dimensions(tbox)
                try:
                    i = get_column(columns, dim.left, dim.right)
                except ValueError:
                    # just ignore suspicious rows
                    if len(row) != 5:
                        continue
                    raise ValueError(
                        f"{repr(tbox.text())} {(dim.left, dim.right)} does not fit in the table"
                    )
                self.enqueue_annotation([tbox], page=page, prefix="NewInvoice.__iter__")
                parsed_row[i].append(tbox)
            if (
                not parsed_row[0]
                and not parsed_row[2]
                and not parsed_row[3]
                and not parsed_row[4]
            ):
                # add incomplete rows to the previous
                combined_row[1].append(" ")
                combined_row[1].extend(parsed_row[1])
            else:
                if any(map(bool, combined_row)):
                    yield self._format_columns(combined_row)
                combined_row = parsed_row
        if any(map(bool, combined_row)):
            yield self._format_columns(combined_row)
