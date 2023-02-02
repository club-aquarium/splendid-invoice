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

import sys
from datetime import date
from typing import (
    Iterator,
    List,
    Optional,
    TextIO,
    Tuple,
)

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
