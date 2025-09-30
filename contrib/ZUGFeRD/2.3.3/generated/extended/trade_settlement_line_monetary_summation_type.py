from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeSettlementLineMonetarySummationType:
    line_total_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "LineTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    charge_total_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "ChargeTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    allowance_total_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "AllowanceTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    tax_total_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "TaxTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    grand_total_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "GrandTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_allowance_charge_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "TotalAllowanceChargeAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
