from dataclasses import dataclass, field
from typing import Optional

from .transport_movement_stage_code_content_type import (
    TransportMovementStageCodeContentType,
)
from .transport_movement_stage_code_list_agency_idcontent_type import (
    TransportMovementStageCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TransportMovementStageCodeType:
    value: Optional[TransportMovementStageCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: TransportMovementStageCodeListAgencyIdcontentType = field(
        init=False,
        default=TransportMovementStageCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
