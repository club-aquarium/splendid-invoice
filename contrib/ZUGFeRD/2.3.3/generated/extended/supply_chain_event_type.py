from dataclasses import dataclass, field
from typing import Optional

from .date_time_type import DateTimeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainEventType:
    occurrence_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "OccurrenceDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
