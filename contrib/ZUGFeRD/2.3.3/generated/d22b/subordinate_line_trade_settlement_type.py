from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .financial_adjustment_type import FinancialAdjustmentType
from .referenced_document_type import ReferencedDocumentType
from .trade_allowance_charge_type import TradeAllowanceChargeType
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SubordinateLineTradeSettlementType:
    """
    Subordinate Line Trade Settlement.

    :ivar amount_direction_code: Amount Direction Code
    :ivar applicable_trade_tax: Trade Tax
    :ivar invoice_referenced_document: Invoice Document
    :ivar specified_financial_adjustment: Specified Financial Adjustment
    :ivar specified_trade_allowance_charge: Specified Allowance Charge
    """

    amount_direction_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "AmountDirectionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_trade_tax: Optional[TradeTaxType] = field(
        default=None,
        metadata={
            "name": "ApplicableTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoice_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_financial_adjustment: list[FinancialAdjustmentType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedFinancialAdjustment",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_trade_allowance_charge: list[TradeAllowanceChargeType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedTradeAllowanceCharge",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
