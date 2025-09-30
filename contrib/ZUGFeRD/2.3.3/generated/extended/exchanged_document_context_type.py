from dataclasses import dataclass, field
from typing import Optional

from .document_context_parameter_type import DocumentContextParameterType
from .indicator_type import IndicatorType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ExchangedDocumentContextType:
    test_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "TestIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    business_process_specified_document_context_parameter: Optional[
        DocumentContextParameterType
    ] = field(
        default=None,
        metadata={
            "name": "BusinessProcessSpecifiedDocumentContextParameter",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    guideline_specified_document_context_parameter: Optional[
        DocumentContextParameterType
    ] = field(
        default=None,
        metadata={
            "name": "GuidelineSpecifiedDocumentContextParameter",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
