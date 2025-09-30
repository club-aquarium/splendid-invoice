from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeSettlementHeaderMonetarySummationType:
    tax_basis_total_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "TaxBasisTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    tax_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "max_occurs": 2,
        },
    )
    grand_total_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "GrandTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    due_payable_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "DuePayableAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
