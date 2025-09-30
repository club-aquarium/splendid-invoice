from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .date_time_type import DateTimeType
from .idtype import Idtype
from .indicator_type import IndicatorType
from .measure_type import MeasureType
from .numeric_type import NumericType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SpecifiedPeriodType:
    """
    Period.

    :ivar duration_measure: Duration Measure
    :ivar inclusive_indicator: Inclusive Indicator
    :ivar description: Description
    :ivar start_date_time: Start Date Time
    :ivar end_date_time: End Date Time
    :ivar complete_date_time: Complete Date Time
    :ivar open_indicator: Open Indicator
    :ivar season_code: Season Code
    :ivar id: ID
    :ivar name: Name
    :ivar sequence_numeric: Sequence Number
    :ivar start_date_flexibility_code: Start Date Flexibility Code
    :ivar continuous_indicator: Continuous Indicator
    :ivar purpose_code: Purpose Code
    """

    duration_measure: list[MeasureType] = field(
        default_factory=list,
        metadata={
            "name": "DurationMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    inclusive_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "InclusiveIndicator",
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
    start_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "StartDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    end_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "EndDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    complete_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "CompleteDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    open_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "OpenIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    season_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "SeasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sequence_numeric: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    start_date_flexibility_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "StartDateFlexibilityCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    continuous_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "ContinuousIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    purpose_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "PurposeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
