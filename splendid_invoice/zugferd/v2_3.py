"""
splendid-invoice
Copyright (C) 2025  schnusch

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
from datetime import date, datetime
from decimal import Decimal
from typing import Iterator, TextIO

import popplerqt5  # type: ignore[import-not-found]
from xsdata.formats.dataclass.parsers import XmlParser  # type: ignore[import-not-found]

from ..base import Invoice, PaddedRow
from .generated import en16931
from .generated.en16931 import AmountType, DateTimeType
from .v1_0 import format_decimal

# For a complete list of (verbose) unit codes see
# '../../contrib/ZUGFeRD/2.3.3/ZF233_DE_01/Dokumentation/4. EN16931+FacturX code lists values v15 - used from 2025-05-15.xlsx'
unit_codes = {
    "BO": "Flasche",
    "C62": "Stk.",
    "H87": "Stk.",
}


def parse_date(dt: DateTimeType.DateTimeString) -> date:
    assert dt.format == "102", "only date format 102 (YYYYMMDD) supported"
    return datetime.strptime(dt.value, "%Y%m%d").date()


def parse_price(amount: AmountType) -> Decimal:
    assert amount.value is not None, f"missing value {amount!r}"
    assert amount.currency_id is None or amount.currency_id == "EUR", (
        f"only prices in Euros supported, not {amount!r}"
    )
    return Decimal(amount.value)


class Zugferd_2_0_EN16931_Invoice(Invoice):
    _parser = XmlParser()

    @classmethod
    def load(cls, name: str) -> "Zugferd_2_0_EN16931_Invoice":
        return cls(popplerqt5.Poppler.Document.load(name))

    def __init__(self, doc: popplerqt5.Poppler.Document):
        success = False
        for file in doc.embeddedFiles():
            if file.name() in (
                "factur-x.xml",
                # compatibility to ZUGFeRD < 2.2
                "zugferd-invoice.xml",
            ):
                if not file.isValid():
                    raise ValueError(f"embedded {file.name()} is invalid")
                self.xml = self._parser.from_bytes(
                    file.data(),
                    en16931.CrossIndustryInvoice,
                )
                success = True
                break
        assert success, "missing factur-x.xml"

    def __iter__(self) -> Iterator[PaddedRow]:
        invoice_date = parse_date(
            self.xml.exchanged_document.issue_date_time.date_time_string
        )
        invoice_id = self.xml.exchanged_document.id.value
        delivery_date = parse_date(
            self.xml.supply_chain_trade_transaction.applicable_header_trade_delivery.actual_delivery_supply_chain_event.occurrence_date_time.date_time_string
        )
        delivery_id = ""  # TODO seems to be missing

        for item in self.xml.supply_chain_trade_transaction.included_supply_chain_trade_line_item:
            id = item.specified_trade_product.seller_assigned_id.value
            name = item.specified_trade_product.name.value.strip()

            size = ""  # TODO seems to be missing
            quantity = Decimal(item.specified_line_trade_delivery.billed_quantity.value)
            unit_code = item.specified_line_trade_delivery.billed_quantity.unit_code
            try:
                unit_code = unit_codes[unit_code]
            except KeyError:
                pass

            net_price = parse_price(
                item.specified_line_trade_agreement.gross_price_product_trade_price.charge_amount
            )
            total = parse_price(
                item.specified_line_trade_settlement.specified_trade_settlement_line_monetary_summation.line_total_amount
            )
            tax = Decimal(
                item.specified_line_trade_settlement.applicable_trade_tax.rate_applicable_percent.value
            )

            yield (
                delivery_date,  # Leistungsdatum
                delivery_id,  # Lieferschein
                invoice_date,  # Rechnungsdatum
                invoice_id,  # Rechnungs-Nr.
                id,  # Artikel
                name,  # Bezeichnung
                size,  # Inhalt
                format_decimal(quantity),  # Anzahl
                unit_code,  # Menge
                format_decimal(net_price),  # Preis
                format_decimal(total),  # Betrag
                format_decimal(tax),  # Umsatzsteuer
            )

    def print_pages(self, fileobj: TextIO = sys.stderr) -> None:
        print(
            f"extracted {len(self.xml.supply_chain_trade_transaction.included_supply_chain_trade_line_item)} items",
            file=sys.stderr,
        )
