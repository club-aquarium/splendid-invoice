from dataclasses import dataclass, field
from typing import Optional

from .accounting_debit_credit_status_code_type import (
    AccountingDebitCreditStatusCodeType,
)
from .amount_type import AmountType
from .code_type import CodeType
from .date_time_type import DateTimeType
from .quantity_type import QuantityType
from .referenced_document_type import ReferencedDocumentType
from .text_type import TextType
from .trade_party_type import TradePartyType
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class FinancialAdjustmentType:
    """
    Financial Adjustment.

    :ivar reason_code: Reason Code
    :ivar reason: Reason Text
    :ivar actual_amount: Actual Amount
    :ivar actual_quantity: Actual Quantity
    :ivar actual_date_time: Actual Date Time
    :ivar direction_code: Direction Code
    :ivar claim_related_trade_party: Claim Related Party
    :ivar invoice_reference_referenced_document: Reference Invoice
        Document
    :ivar related_trade_tax: Related Tax
    """

    reason_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    reason: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "ActualAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "ActualQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ActualDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    direction_code: Optional[AccountingDebitCreditStatusCodeType] = field(
        default=None,
        metadata={
            "name": "DirectionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    claim_related_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "ClaimRelatedTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoice_reference_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "InvoiceReferenceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    related_trade_tax: list[TradeTaxType] = field(
        default_factory=list,
        metadata={
            "name": "RelatedTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
