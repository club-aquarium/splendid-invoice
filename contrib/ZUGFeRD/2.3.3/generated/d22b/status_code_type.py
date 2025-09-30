from dataclasses import dataclass, field
from typing import Optional

from .status_code_content_type import StatusCodeContentType
from .status_code_list_agency_idcontent_type import (
    StatusCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class StatusCodeType:
    value: Optional[StatusCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: StatusCodeListAgencyIdcontentType = field(
        init=False,
        default=StatusCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
