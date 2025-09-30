from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .indicator_type import IndicatorType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class RegisteredTaxType:
    """
    Registered Tax.

    :ivar type_code: Type Code
    :ivar exemption_reason_code: Exemption Reason Code
    :ivar exemption_reason: Exemption Reason Text
    :ivar currency_code: Currency Code
    :ivar jurisdiction: Jurisdiction Text
    :ivar description: Description
    :ivar customs_duty_indicator: Customs Duty Indicator
    """

    type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
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
    exemption_reason: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "ExemptionReason",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    currency_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    jurisdiction: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Jurisdiction",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    customs_duty_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "CustomsDutyIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
