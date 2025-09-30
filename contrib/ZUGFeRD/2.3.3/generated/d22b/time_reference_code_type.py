from dataclasses import dataclass, field
from typing import Optional

from .event_time_reference_code_content_type import (
    EventTimeReferenceCodeContentType,
)
from .time_reference_code_list_agency_idcontent_type import (
    TimeReferenceCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TimeReferenceCodeType:
    value: Optional[EventTimeReferenceCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: TimeReferenceCodeListAgencyIdcontentType = field(
        init=False,
        default=TimeReferenceCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
