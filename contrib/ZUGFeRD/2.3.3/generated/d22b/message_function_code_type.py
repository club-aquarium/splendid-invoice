from dataclasses import dataclass, field
from typing import Optional

from .message_function_code_content_type import MessageFunctionCodeContentType
from .message_function_code_list_agency_idcontent_type import (
    MessageFunctionCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class MessageFunctionCodeType:
    value: Optional[MessageFunctionCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: MessageFunctionCodeListAgencyIdcontentType = field(
        init=False,
        default=MessageFunctionCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
