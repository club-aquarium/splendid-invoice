from dataclasses import dataclass, field
from typing import Optional

from .basic_work_item_type import BasicWorkItemType
from .calculated_price_type import CalculatedPriceType
from .code_type import CodeType
from .idtype import Idtype
from .quantity_type import QuantityType
from .recorded_status_type import RecordedStatusType
from .specified_binary_file_type import SpecifiedBinaryFileType
from .text_type import TextType
from .work_item_complex_description_type import WorkItemComplexDescriptionType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class GroupedWorkItemType:
    """
    Grouped Work Item.

    :ivar id: ID
    :ivar primary_classification_code: Primary Classification Code
    :ivar alternative_classification_code: Alternative Classification
        Code
    :ivar type_code: Type Code
    :ivar comment: Comment
    :ivar total_quantity: Total Quantity
    :ivar index: Index Text
    :ivar requested_action_code: Requested Action Code
    :ivar price_list_item_id: Price List Item ID
    :ivar contractual_language_code: Contractual Language Code
    :ivar total_calculated_price: Total Calculated Price
    :ivar item_grouped_work_item: Item Grouped Work Item
    :ivar item_basic_work_item: Item Basic Work Item
    :ivar changed_recorded_status: Changed Recorded Status
    :ivar actual_work_item_complex_description: Complex Description
    :ivar referenced_specified_binary_file: Binary File
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
    total_calculated_price: list[CalculatedPriceType] = field(
        default_factory=list,
        metadata={
            "name": "TotalCalculatedPrice",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    item_grouped_work_item: list["GroupedWorkItemType"] = field(
        default_factory=list,
        metadata={
            "name": "ItemGroupedWorkItem",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    item_basic_work_item: list[BasicWorkItemType] = field(
        default_factory=list,
        metadata={
            "name": "ItemBasicWorkItem",
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
    actual_work_item_complex_description: list[WorkItemComplexDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "ActualWorkItemComplexDescription",
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
