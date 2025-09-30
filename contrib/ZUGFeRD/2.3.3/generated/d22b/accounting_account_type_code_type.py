from dataclasses import dataclass, field
from typing import Optional

from .accounting_account_type_content_type import (
    AccountingAccountTypeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class AccountingAccountTypeCodeType:
    value: Optional[AccountingAccountTypeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: str = field(
        init=False,
        default="210",
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
