from dataclasses import dataclass, field
from typing import Optional

from .accounting_debit_credit_status_code_list_agency_idcontent_type import (
    AccountingDebitCreditStatusCodeListAgencyIdcontentType,
)
from .status_description_code_accounting_debit_credit_content_type import (
    StatusDescriptionCodeAccountingDebitCreditContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class AccountingDebitCreditStatusCodeType:
    value: Optional[StatusDescriptionCodeAccountingDebitCreditContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_id: str = field(
        init=False,
        default="4405_Accounting Debit Credit",
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: AccountingDebitCreditStatusCodeListAgencyIdcontentType = field(
        init=False,
        default=AccountingDebitCreditStatusCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_version_id: str = field(
        init=False,
        default="D22A",
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    list_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "listURI",
            "type": "Attribute",
        },
    )
