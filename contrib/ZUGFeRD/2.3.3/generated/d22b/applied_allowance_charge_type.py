from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .applied_tax_type import AppliedTaxType
from .code_type import CodeType
from .indicator_type import IndicatorType
from .percent_type import PercentType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class AppliedAllowanceChargeType:
    """
    Applied Allowance/Charge.

    :ivar actual_amount: Actual Amount
    :ivar description: Description
    :ivar reason_code: Reason Code
    :ivar calculation_percent: Calculation Percent
    :ivar basis_amount: Basis Amount
    :ivar charge_indicator: Charge Indicator
    :ivar category_applied_tax: Tax Category
    """

    actual_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "ActualAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    reason_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
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
    charge_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "ChargeIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    category_applied_tax: Optional[AppliedTaxType] = field(
        default=None,
        metadata={
            "name": "CategoryAppliedTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
