from dataclasses import dataclass, field
from typing import Optional

from .allowance_charge_reason_code_type import AllowanceChargeReasonCodeType
from .amount_type import AmountType
from .indicator_type import IndicatorType
from .numeric_type import NumericType
from .percent_type import PercentType
from .quantity_type import QuantityType
from .text_type import TextType
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeAllowanceChargeType:
    charge_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "ChargeIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    sequence_numeric: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    calculation_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "CalculationPercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    basis_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "BasisAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    basis_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "BasisQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "ActualAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    reason_code: Optional[AllowanceChargeReasonCodeType] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    reason: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    category_trade_tax: Optional[TradeTaxType] = field(
        default=None,
        metadata={
            "name": "CategoryTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
