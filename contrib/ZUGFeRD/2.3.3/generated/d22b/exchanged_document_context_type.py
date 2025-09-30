from dataclasses import dataclass, field
from typing import Optional

from .document_context_parameter_type import DocumentContextParameterType
from .idtype import Idtype
from .indicator_type import IndicatorType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ExchangedDocumentContextType:
    """
    Exchanged Document Context.

    :ivar specified_transaction_id: Transaction ID
    :ivar test_indicator: Test Indicator
    :ivar business_process_specified_document_context_parameter:
        Business Process
    :ivar bimspecified_document_context_parameter: BIM
    :ivar scenario_specified_document_context_parameter: Scenario
    :ivar application_specified_document_context_parameter: Application
    :ivar guideline_specified_document_context_parameter: Guideline
    :ivar subset_specified_document_context_parameter: Subset
    :ivar message_standard_specified_document_context_parameter: Message
        Standard
    :ivar user_specified_document_context_parameter: User Specified
        Parameter
    """

    specified_transaction_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SpecifiedTransactionID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    test_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "TestIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    business_process_specified_document_context_parameter: list[
        DocumentContextParameterType
    ] = field(
        default_factory=list,
        metadata={
            "name": "BusinessProcessSpecifiedDocumentContextParameter",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    bimspecified_document_context_parameter: list[DocumentContextParameterType] = field(
        default_factory=list,
        metadata={
            "name": "BIMSpecifiedDocumentContextParameter",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    scenario_specified_document_context_parameter: list[
        DocumentContextParameterType
    ] = field(
        default_factory=list,
        metadata={
            "name": "ScenarioSpecifiedDocumentContextParameter",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    application_specified_document_context_parameter: list[
        DocumentContextParameterType
    ] = field(
        default_factory=list,
        metadata={
            "name": "ApplicationSpecifiedDocumentContextParameter",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    guideline_specified_document_context_parameter: list[
        DocumentContextParameterType
    ] = field(
        default_factory=list,
        metadata={
            "name": "GuidelineSpecifiedDocumentContextParameter",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    subset_specified_document_context_parameter: list[DocumentContextParameterType] = (
        field(
            default_factory=list,
            metadata={
                "name": "SubsetSpecifiedDocumentContextParameter",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    message_standard_specified_document_context_parameter: Optional[
        DocumentContextParameterType
    ] = field(
        default=None,
        metadata={
            "name": "MessageStandardSpecifiedDocumentContextParameter",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    user_specified_document_context_parameter: list[DocumentContextParameterType] = (
        field(
            default_factory=list,
            metadata={
                "name": "UserSpecifiedDocumentContextParameter",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
