"""
splendid-invoice
Copyright (C) 2023-2024  schnusch

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
import sys
from collections.abc import Iterable
from datetime import date
from types import TracebackType
from typing import (
    TYPE_CHECKING,
    Any,
    Iterator,
    List,  # noqa: F401
    Optional,
    Protocol,
    TextIO,
    Tuple,
    Type,
    TypeVar,
)

if TYPE_CHECKING:
    from _csv import _QuotingType

_T_contra = TypeVar("_T_contra", contravariant=True)


# see https://github.com/python/typeshed/blob/54fde0c2a104241077a61172c8de53d60519670a/stdlib/_typeshed/__init__.pyi#L182-L184
class SupportsWrite(Protocol[_T_contra]):
    def write(self, __s: _T_contra) -> object: ...  # noqa: E704


T = TypeVar("T", bound="CSVOutput")


class CSVOutput(object):
    delimiter = ";"
    quoting: "_QuotingType" = csv.QUOTE_ALL

    def __init__(self, out: SupportsWrite[str]):
        self._writer = csv.writer(out, delimiter=self.delimiter, quoting=self.quoting)

    def __enter__(self: T) -> T:
        return self

    def __exit__(
        self,
        type: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        return None

    def writeheaders(self, headers: Iterable[Any]) -> None:
        self.writerow(headers)

    def writerow(self, row: Iterable[Any]) -> None:
        self._writer.writerow(row)


ParsedRow = Tuple[
    str,  # Artikel
    str,  # Bezeichnung
    str,  # Inhalt
    str,  # Anzahl
    str,  # Menge
    str,  # Preis
    str,  # Betrag
    str,  # Umsatzsteuer
]

PaddedRow = Tuple[
    Optional[date],  # Leistungsdatum
    str,  # Lieferschein
    Optional[date],  # Rechnungsdatum
    str,  # Rechnungs-Nr.
    str,  # Artikel
    str,  # Bezeichnung
    str,  # Inhalt
    str,  # Anzahl
    str,  # Menge
    str,  # Preis
    str,  # Betrag
    str,  # Umsatzsteuer
]


class InvoicePage:
    def get_delivery_info(self) -> Tuple[str, Optional[date]]:
        raise NotImplementedError

    def get_invoice_info(self) -> Tuple[str, Optional[date]]:
        raise NotImplementedError

    def parse_table(self) -> Iterator[ParsedRow]:
        raise NotImplementedError

    def print_page(self, fileobj: TextIO) -> None:
        print(
            f"{type(self).__module__}.{type(self).__qualname__}.print_page() not implemented.",
            file=fileobj,
        )


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
        "USt.",
    )

    def __init__(self) -> None:
        self.pages = []  # type: List[InvoicePage]

    def __iter__(self) -> Iterator[PaddedRow]:
        delivery_id = ""
        delivery_date = None
        for page in self.pages:
            try:
                delivery_id, delivery_date = page.get_delivery_info()
            except ValueError:
                pass
            try:
                invoice_id, invoice_date = page.get_invoice_info()
            except (AttributeError, ValueError):
                invoice_id = ""
                invoice_date = None
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


class DummyInvoice(Invoice):
    def __iter__(self) -> Iterator[PaddedRow]:
        return iter([])
