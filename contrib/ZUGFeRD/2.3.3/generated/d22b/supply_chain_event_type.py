from dataclasses import dataclass, field
from typing import Optional

from .binary_object_type import BinaryObjectType
from .code_type import CodeType
from .date_time_type import DateTimeType
from .idtype import Idtype
from .logistics_location_type import LogisticsLocationType
from .quantity_type import QuantityType
from .specified_period_type import SpecifiedPeriodType
from .text_type import TextType
from .time_only_formatted_date_time_type import TimeOnlyFormattedDateTimeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainEventType:
    """
    Supply Chain Event.

    :ivar id: ID
    :ivar occurrence_date_time: Occurrence Date Time
    :ivar type_code: Type Code
    :ivar description: Description
    :ivar description_binary_object: Description Binary Object
    :ivar unit_quantity: Unit Quantity
    :ivar latest_occurrence_date_time: Latest Occurrence Date Time
    :ivar earliest_occurrence_date_time: Earliest Occurrence Date Time
    :ivar time_occurrence_date_time: Occurrence Time
    :ivar occurrence_specified_period: Occurrence Period
    :ivar occurrence_logistics_location: Location
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    occurrence_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "OccurrenceDateTime",
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
    description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    description_binary_object: list[BinaryObjectType] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionBinaryObject",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    unit_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "UnitQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    latest_occurrence_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "LatestOccurrenceDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    earliest_occurrence_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "EarliestOccurrenceDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    time_occurrence_date_time: Optional[TimeOnlyFormattedDateTimeType] = field(
        default=None,
        metadata={
            "name": "TimeOccurrenceDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    occurrence_specified_period: Optional[SpecifiedPeriodType] = field(
        default=None,
        metadata={
            "name": "OccurrenceSpecifiedPeriod",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    occurrence_logistics_location: Optional[LogisticsLocationType] = field(
        default=None,
        metadata={
            "name": "OccurrenceLogisticsLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
