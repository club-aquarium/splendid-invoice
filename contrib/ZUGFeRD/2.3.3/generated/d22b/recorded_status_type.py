from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .date_time_type import DateTimeType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class RecordedStatusType:
    """
    Recorded Status.

    :ivar condition_code: Condition Code
    :ivar changer_name: Changer Name
    :ivar changed_date_time: Changed Date Time
    """

    condition_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ConditionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    changer_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ChangerName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    changed_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ChangedDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
