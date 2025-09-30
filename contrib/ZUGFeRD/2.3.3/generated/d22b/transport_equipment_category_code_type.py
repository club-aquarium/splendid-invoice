from dataclasses import dataclass, field
from typing import Optional

from .transport_equipment_category_code_content_type import (
    TransportEquipmentCategoryCodeContentType,
)
from .transport_equipment_category_code_list_agency_idcontent_type import (
    TransportEquipmentCategoryCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TransportEquipmentCategoryCodeType:
    value: Optional[TransportEquipmentCategoryCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: TransportEquipmentCategoryCodeListAgencyIdcontentType = field(
        init=False,
        default=TransportEquipmentCategoryCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
