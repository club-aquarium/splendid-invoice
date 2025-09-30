from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .percent_type import PercentType
from .quantity_type import QuantityType
from .recorded_status_type import RecordedStatusType
from .text_type import TextType
from .work_item_dimension_type import WorkItemDimensionType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class WorkItemQuantityAnalysisType:
    """
    Work Item Quantity Analysis.

    :ivar id: ID
    :ivar actual_quantity: Actual Quantity
    :ivar description: Description
    :ivar actual_quantity_percent: Actual Quantity Percent
    :ivar type_code: Type Code
    :ivar primary_classification_code: Primary Classification Code
    :ivar alternative_classification_code: Alternative Classification
        Code
    :ivar contractual_language_code: Contractual Language Code
    :ivar actual_quantity_work_item_dimension: Actual Quantity Dimension
    :ivar breakdown_work_item_quantity_analysis: Quantity Breakdown
        Analysis
    :ivar changed_recorded_status: Changed Recorded Status
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
    actual_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "ActualQuantity",
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
    actual_quantity_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "ActualQuantityPercent",
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
    contractual_language_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ContractualLanguageCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_quantity_work_item_dimension: list[WorkItemDimensionType] = field(
        default_factory=list,
        metadata={
            "name": "ActualQuantityWorkItemDimension",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    breakdown_work_item_quantity_analysis: list["WorkItemQuantityAnalysisType"] = field(
        default_factory=list,
        metadata={
            "name": "BreakdownWorkItemQuantityAnalysis",
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
