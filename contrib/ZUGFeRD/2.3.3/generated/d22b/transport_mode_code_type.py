from dataclasses import dataclass, field
from typing import Optional

from .transport_mode_code_content_type import TransportModeCodeContentType
from .transport_mode_code_list_agency_idcontent_type import (
    TransportModeCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TransportModeCodeType:
    value: Optional[TransportModeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: TransportModeCodeListAgencyIdcontentType = field(
        init=False,
        default=TransportModeCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
