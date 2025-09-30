from dataclasses import dataclass, field
from typing import Optional

from .party_role_code_content_type import PartyRoleCodeContentType
from .party_role_code_list_agency_idcontent_type import (
    PartyRoleCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PartyRoleCodeType:
    value: Optional[PartyRoleCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: PartyRoleCodeListAgencyIdcontentType = field(
        init=False,
        default=PartyRoleCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
