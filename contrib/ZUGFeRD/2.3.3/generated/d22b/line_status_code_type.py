from dataclasses import dataclass, field
from typing import Optional

from .action_code_content_type import ActionCodeContentType
from .line_status_code_list_agency_idcontent_type import (
    LineStatusCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class LineStatusCodeType:
    value: Optional[ActionCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: LineStatusCodeListAgencyIdcontentType = field(
        init=False,
        default=LineStatusCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
