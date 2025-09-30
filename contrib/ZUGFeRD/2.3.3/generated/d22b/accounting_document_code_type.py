from dataclasses import dataclass, field
from typing import Optional

from .accounting_document_code_list_agency_idcontent_type import (
    AccountingDocumentCodeListAgencyIdcontentType,
)
from .document_name_code_accounting_content_type import (
    DocumentNameCodeAccountingContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class AccountingDocumentCodeType:
    value: Optional[DocumentNameCodeAccountingContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: AccountingDocumentCodeListAgencyIdcontentType = field(
        init=False,
        default=AccountingDocumentCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
