from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .code_type import CodeType
from .date_type import DateType
from .rate_type import RateType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class AppliedTaxType:
    """
    Applied Tax.

    :ivar calculated_amount: Calculated Amount
    :ivar type_code: Type Code
    :ivar calculated_rate: Calculated Rate
    :ivar basis_amount: Basis Amount
    :ivar tax_point_date: Tax Point Date
    """

    calculated_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "CalculatedAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    calculated_rate: Optional[RateType] = field(
        default=None,
        metadata={
            "name": "CalculatedRate",
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
    tax_point_date: Optional[DateType] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
