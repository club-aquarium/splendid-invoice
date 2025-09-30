from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .code_type import CodeType
from .percent_type import PercentType
from .tax_category_code_type import TaxCategoryCodeType
from .tax_type_code_type import TaxTypeCodeType
from .text_type import TextType
from .time_reference_code_type import TimeReferenceCodeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeTaxType:
    calculated_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "CalculatedAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[TaxTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    exemption_reason: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ExemptionReason",
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
    category_code: Optional[TaxCategoryCodeType] = field(
        default=None,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    exemption_reason_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ExemptionReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    due_date_type_code: Optional[TimeReferenceCodeType] = field(
        default=None,
        metadata={
            "name": "DueDateTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    rate_applicable_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "RateApplicablePercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
