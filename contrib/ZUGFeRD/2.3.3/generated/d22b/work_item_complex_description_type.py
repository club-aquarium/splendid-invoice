from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .specification_query_type import SpecificationQueryType
from .specification_response_type import SpecificationResponseType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class WorkItemComplexDescriptionType:
    """
    Work Item Complex Description.

    :ivar abstract: Abstract
    :ivar content: Content Text
    :ivar contractual_language_code: Contractual Language Code
    :ivar requesting_specification_query: Requesting Specification Query
    :ivar responding_specification_response: Responding Specification
        Answer
    :ivar subset_work_item_complex_description: Subset Complex
        Description
    """

    abstract: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    content: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    contractual_language_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ContractualLanguageCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    requesting_specification_query: list[SpecificationQueryType] = field(
        default_factory=list,
        metadata={
            "name": "RequestingSpecificationQuery",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    responding_specification_response: list[SpecificationResponseType] = field(
        default_factory=list,
        metadata={
            "name": "RespondingSpecificationResponse",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    subset_work_item_complex_description: Optional["WorkItemComplexDescriptionType"] = (
        field(
            default=None,
            metadata={
                "name": "SubsetWorkItemComplexDescription",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
