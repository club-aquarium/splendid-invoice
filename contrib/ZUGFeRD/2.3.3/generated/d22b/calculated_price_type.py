from dataclasses import dataclass, field

from .amount_type import AmountType
from .applied_allowance_charge_type import AppliedAllowanceChargeType
from .code_type import CodeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class CalculatedPriceType:
    """
    Calculated Price.

    :ivar type_code: Type Code
    :ivar charge_amount: Charge Amount
    :ivar related_applied_allowance_charge: Applied Allowance/Charge
    """

    type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    charge_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "ChargeAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    related_applied_allowance_charge: list[AppliedAllowanceChargeType] = field(
        default_factory=list,
        metadata={
            "name": "RelatedAppliedAllowanceCharge",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
