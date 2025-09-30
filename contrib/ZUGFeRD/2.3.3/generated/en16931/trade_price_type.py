from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .quantity_type import QuantityType
from .trade_allowance_charge_type import TradeAllowanceChargeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradePriceType:
    charge_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "ChargeAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
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
    applied_trade_allowance_charge: Optional[TradeAllowanceChargeType] = field(
        default=None,
        metadata={
            "name": "AppliedTradeAllowanceCharge",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
