from dataclasses import dataclass, field
from typing import Optional

from .charge_paying_party_role_code_list_agency_idcontent_type import (
    ChargePayingPartyRoleCodeListAgencyIdcontentType,
)
from .party_role_code_charge_paying_content_type import (
    PartyRoleCodeChargePayingContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class ChargePayingPartyRoleCodeType:
    value: Optional[PartyRoleCodeChargePayingContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: ChargePayingPartyRoleCodeListAgencyIdcontentType = field(
        init=False,
        default=ChargePayingPartyRoleCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
