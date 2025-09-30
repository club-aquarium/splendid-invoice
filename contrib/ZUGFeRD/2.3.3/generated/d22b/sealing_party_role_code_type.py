from dataclasses import dataclass, field
from typing import Optional

from .sealing_party_role_code_content_type import (
    SealingPartyRoleCodeContentType,
)
from .sealing_party_role_code_list_agency_idcontent_type import (
    SealingPartyRoleCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class SealingPartyRoleCodeType:
    value: Optional[SealingPartyRoleCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_id: str = field(
        init=False,
        default="9303",
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: SealingPartyRoleCodeListAgencyIdcontentType = field(
        init=False,
        default=SealingPartyRoleCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
