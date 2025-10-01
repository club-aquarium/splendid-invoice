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
import xml.etree.cElementTree as ET
from datetime import date, datetime
from decimal import ROUND_HALF_UP, Decimal
from typing import (
    Callable,
    Iterator,
    Optional,
    TextIO,
    Tuple,
    TypeVar,
    Union,
)

import popplerqt5  # type: ignore

from .base import Invoice, PaddedRow

namespaces = {
    "rsm": "urn:ferd:CrossIndustryDocument:invoice:1p0",
    "ram": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:12",
    "udt": "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:15",
}


def _full_tag(ns: str, name: str) -> str:
    return "{%s}%s" % (namespaces[ns], name)


class ElementNotFound(Exception):
    pass


def _get_path(elem: ET.Element, path: str) -> ET.Element:
    child = elem.find(path, namespaces)
    if child is None:
        raise ElementNotFound(f"cannot find {path}")
    return child


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def try_get(
    root: Optional[ET.Element],
    path: str,
    parse: Callable[[ET.Element], T1],
    default: T2,
) -> Union[T1, T2]:
    elem = None  # type: Optional[ET.Element]
    if root is not None:
        try:
            elem = _get_path(root, path)
        except ElementNotFound:
            pass
    return default if elem is None else parse(elem)


def get_text(elem: ET.Element) -> str:
    return elem.text or ""


def parse_date(elem: ET.Element) -> date:
    assert elem.attrib["format"] == "102", "only date format 102 (YYYYMMDD) supported"
    assert elem.text is not None, "date string expected"
    return datetime.strptime(elem.text, "%Y%m%d").date()


def format_decimal(d: Decimal) -> str:
    return str(d.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)).replace(".", ",")


unit_codes = {
    "C62": "Stk.",
    "DAY": "Tag(e)",
    "HAR": "Hektar",
    "HUR": "Std.",
    "KGM": "kg",
    "KTM": "km",
    "KWH": "kWh",
    "LS": "pausch.",
    "LTR": "l",
    "MIN": "min",
    "MMK": "mm²",
    "MMT": "mm",
    "MTK": "m²",
    "MTQ": "m³",
    "MTR": "m",
    "NAR": "Anz.",
    "NPR": "Pr.",
    "P1": "%",
    "SET": "Set(s)",
    "TNE": "t",
    "WEE": "Woche(n)",
}


def parse_quantity(elem: ET.Element) -> Tuple[str, str]:
    assert elem.text is not None, "expected number string"
    d = Decimal(get_text(elem))
    return (format_decimal(d), elem.attrib["unitCode"])


def parse_price(elem: ET.Element) -> Tuple[str, str]:
    assert elem.text is not None, "expected number string"
    d = Decimal(elem.text)
    currency_id = elem.attrib.get("currencyID")
    assert currency_id == "EUR", f"only prices in Euros supported, {repr(elem)}"
    return (format_decimal(d), currency_id)


def parse_tax(elem: ET.Element) -> str:
    type_code = get_text(_get_path(elem, "ram:TypeCode"))
    category_code = get_text(_get_path(elem, "ram:CategoryCode"))
    assert type_code == "VAT" and category_code == "S"
    tax = Decimal(get_text(_get_path(elem, "ram:ApplicablePercent")))
    return format_decimal(tax)


def parse_line_item(
    elem: ET.Element,
    invoice_date: Optional[date],
    invoice_id: str,
) -> PaddedRow:
    product_elem = _get_path(elem, "ram:SpecifiedTradeProduct")
    name = get_text(_get_path(product_elem, "ram:Name"))
    id = try_get(product_elem, "ram:SellerAssignedID", get_text, "")
    size, size_unit_code = try_get(
        product_elem,
        "ram:ApplicableProductCharacteristic/ram:ValueMeasure",
        parse_quantity,
        ("", ""),
    )

    delivery_elem = elem.find("ram:SpecifiedSupplyChainTradeDelivery", namespaces)
    delivery_date = try_get(
        delivery_elem,
        "ram:ActualDeliverySupplyChainEvent/ram:OccurrenceDateTime/udt:DateTimeString",
        parse_date,
        None,
    )
    delivery_id = try_get(
        delivery_elem, "ram:DeliveryNoteReferencedDocument/ram:ID", get_text, ""
    )
    quantity, quantity_unit_code = try_get(
        delivery_elem, "ram:BilledQuantity", parse_quantity, ("", "")
    )

    net_elem = elem.find(
        "ram:SpecifiedSupplyChainTradeAgreement/ram:GrossPriceProductTradePrice",
        namespaces,
    )
    net_price, _ = try_get(net_elem, "ram:ChargeAmount", parse_price, ("", ""))
    net_base_quantity, net_base_quantity_unit_code = try_get(
        net_elem, "ram:BasisQuantity", parse_quantity, ("", "")
    )

    settlement_elem = elem.find("ram:SpecifiedSupplyChainTradeSettlement", namespaces)
    total, _ = try_get(
        settlement_elem,
        "ram:SpecifiedTradeSettlementMonetarySummation/ram:LineTotalAmount",
        parse_price,
        ("", ""),
    )
    tax = try_get(settlement_elem, "ram:ApplicableTradeTax", parse_tax, "")

    assert Decimal(net_base_quantity.replace(",", ".")) == 1, (
        f"expected base quantity to be 1, not {repr(net_base_quantity)}"
    )
    assert net_base_quantity_unit_code == quantity_unit_code

    return (
        delivery_date,  # Leistungsdatum
        delivery_id,  # Lieferschein
        invoice_date,  # Rechnungsdatum
        invoice_id,  # Rechnungs-Nr.
        id,  # Artikel
        name,  # Bezeichnung
        size,  # Inhalt
        quantity,  # Anzahl
        unit_codes.get(quantity_unit_code, ""),  # Menge
        net_price,  # Preis
        total,  # Betrag
        tax,  # Umsatzsteuer
    )


def parse_xml(data: bytes) -> Iterator[PaddedRow]:
    root = ET.fromstring(data)
    assert root.tag == _full_tag("rsm", "CrossIndustryDocument")

    invoice_date = try_get(
        root,
        "rsm:HeaderExchangedDocument/ram:IssueDateTime/udt:DateTimeString",
        parse_date,
        None,
    )
    invoice_id = try_get(root, "rsm:HeaderExchangedDocument/ram:ID", get_text, "")

    for elem in root.iterfind(
        "rsm:SpecifiedSupplyChainTradeTransaction/ram:IncludedSupplyChainTradeLineItem",
        namespaces,
    ):
        try:
            row = parse_line_item(elem, invoice_date, invoice_id)
        except ElementNotFound:
            continue
        yield row


class Zugferd1p0Invoice(Invoice):
    @classmethod
    def load(cls, name: str) -> "Zugferd1p0Invoice":
        return cls(popplerqt5.Poppler.Document.load(name))

    def __init__(self, doc: popplerqt5.Poppler.Document):
        success = False
        for file in doc.embeddedFiles():
            if file.name() == "zugferd-invoice.xml":
                if not file.isValid():
                    raise ValueError("embedded zugferd-invoice.xml is invalid")
                self.rows = list(parse_xml(file.data()))
                success = True
                break
        assert success, "missing zugferd-invoice.xml"

    def __iter__(self) -> Iterator[PaddedRow]:
        return iter(self.rows)

    def print_pages(self, fileobj: TextIO = sys.stderr) -> None:
        print(f"extracted {len(self.rows)} items", file=sys.stderr)
