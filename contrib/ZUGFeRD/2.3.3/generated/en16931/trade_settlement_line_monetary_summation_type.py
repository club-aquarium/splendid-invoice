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
