from dataclasses import dataclass, field
from typing import Optional

from .cargo_category_code_list_agency_idcontent_type import (
    CargoCategoryCodeListAgencyIdcontentType,
)
from .cargo_type_code_content_type import CargoTypeCodeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class CargoCategoryCodeType:
    value: Optional[CargoTypeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: CargoCategoryCodeListAgencyIdcontentType = field(
        init=False,
        default=CargoCategoryCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
