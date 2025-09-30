from dataclasses import dataclass, field
from typing import Optional

from .seal_condition_code_content_type import SealConditionCodeContentType
from .seal_condition_code_list_agency_idcontent_type import (
    SealConditionCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class SealConditionCodeType:
    value: Optional[SealConditionCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: SealConditionCodeListAgencyIdcontentType = field(
        init=False,
        default=SealConditionCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
