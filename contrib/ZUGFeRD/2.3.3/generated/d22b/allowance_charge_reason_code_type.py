from dataclasses import dataclass, field
from typing import Optional

from .allowance_charge_reason_code_content_type import (
    AllowanceChargeReasonCodeContentType,
)
from .allowance_charge_reason_code_list_agency_idcontent_type import (
    AllowanceChargeReasonCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class AllowanceChargeReasonCodeType:
    value: Optional[AllowanceChargeReasonCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: AllowanceChargeReasonCodeListAgencyIdcontentType = field(
        init=False,
        default=AllowanceChargeReasonCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
