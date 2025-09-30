from dataclasses import dataclass, field
from typing import Optional

from .specified_period_type import SpecifiedPeriodType
from .trade_allowance_charge_type import TradeAllowanceChargeType
from .trade_settlement_line_monetary_summation_type import (
    TradeSettlementLineMonetarySummationType,
)
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LineTradeSettlementType:
    applicable_trade_tax: Optional[TradeTaxType] = field(
        default=None,
        metadata={
            "name": "ApplicableTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    billing_specified_period: Optional[SpecifiedPeriodType] = field(
        default=None,
        metadata={
            "name": "BillingSpecifiedPeriod",
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
    specified_trade_settlement_line_monetary_summation: Optional[
        TradeSettlementLineMonetarySummationType
    ] = field(
        default=None,
        metadata={
            "name": "SpecifiedTradeSettlementLineMonetarySummation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
