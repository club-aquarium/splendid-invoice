from dataclasses import dataclass, field
from typing import Optional

from .accounting_amount_type_content_type import (
    AccountingAmountTypeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class AccountingAmountTypeCodeType:
    value: Optional[AccountingAmountTypeContentType] = field(
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
