from dataclasses import dataclass, field
from typing import Optional

from .calculated_price_type import CalculatedPriceType
from .code_type import CodeType
from .idtype import Idtype
from .quantity_type import QuantityType
from .recorded_status_type import RecordedStatusType
from .specified_binary_file_type import SpecifiedBinaryFileType
from .text_type import TextType
from .work_item_complex_description_type import WorkItemComplexDescriptionType
from .work_item_quantity_analysis_type import WorkItemQuantityAnalysisType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class BasicWorkItemType:
    """
    Basic Work Item.

    :ivar id: ID
    :ivar reference_id: Reference ID
    :ivar primary_classification_code: Primary Classification Code
    :ivar alternative_classification_code: Alternative Classification
        Code
    :ivar type_code: Type Code
    :ivar comment: Comment
    :ivar total_quantity: Total Quantity
    :ivar total_quantity_classification_code: Total Quantity
        Classification Code
    :ivar index: Index Text
    :ivar requested_action_code: Requested Action Code
    :ivar price_list_item_id: Price List Item ID
    :ivar contractual_language_code: Contractual Language Code
    :ivar actual_work_item_complex_description: Complex Description
    :ivar total_quantity_work_item_quantity_analysis: Total Quantity
        Analysis
    :ivar unit_calculated_price: Calculated Unit Price
    :ivar total_calculated_price: Calculated Total Price
    :ivar changed_recorded_status: Recorded Changed Status
    :ivar item_basic_work_item: Item Basic Work Item
    :ivar referenced_specified_binary_file: Referenced Binary File
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    reference_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ReferenceID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    primary_classification_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "PrimaryClassificationCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    alternative_classification_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeClassificationCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    comment: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_quantity_classification_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TotalQuantityClassificationCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    index: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    requested_action_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "RequestedActionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    price_list_item_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "PriceListItemID",
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
    actual_work_item_complex_description: list[WorkItemComplexDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "ActualWorkItemComplexDescription",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_quantity_work_item_quantity_analysis: list[WorkItemQuantityAnalysisType] = (
        field(
            default_factory=list,
            metadata={
                "name": "TotalQuantityWorkItemQuantityAnalysis",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    unit_calculated_price: list[CalculatedPriceType] = field(
        default_factory=list,
        metadata={
            "name": "UnitCalculatedPrice",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_calculated_price: list[CalculatedPriceType] = field(
        default_factory=list,
        metadata={
            "name": "TotalCalculatedPrice",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    changed_recorded_status: list[RecordedStatusType] = field(
        default_factory=list,
        metadata={
            "name": "ChangedRecordedStatus",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    item_basic_work_item: list["BasicWorkItemType"] = field(
        default_factory=list,
        metadata={
            "name": "ItemBasicWorkItem",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    referenced_specified_binary_file: list[SpecifiedBinaryFileType] = field(
        default_factory=list,
        metadata={
            "name": "ReferencedSpecifiedBinaryFile",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
