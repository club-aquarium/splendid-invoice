from dataclasses import dataclass, field
from typing import Optional

from .reference_code_list_agency_idcontent_type import (
    ReferenceCodeListAgencyIdcontentType,
)
from .reference_type_code_content_type import ReferenceTypeCodeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class ReferenceCodeType:
    value: Optional[ReferenceTypeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: ReferenceCodeListAgencyIdcontentType = field(
        init=False,
        default=ReferenceCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
