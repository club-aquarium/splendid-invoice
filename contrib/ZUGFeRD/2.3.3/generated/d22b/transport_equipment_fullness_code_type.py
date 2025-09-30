from dataclasses import dataclass, field
from typing import Optional

from .transport_equipment_fullness_code_content_type import (
    TransportEquipmentFullnessCodeContentType,
)
from .transport_equipment_fullness_code_list_agency_idcontent_type import (
    TransportEquipmentFullnessCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TransportEquipmentFullnessCodeType:
    value: Optional[TransportEquipmentFullnessCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: TransportEquipmentFullnessCodeListAgencyIdcontentType = field(
        init=False,
        default=TransportEquipmentFullnessCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
