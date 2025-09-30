from dataclasses import dataclass, field
from typing import Optional

from .date_time_type import DateTimeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SpecifiedPeriodType:
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
