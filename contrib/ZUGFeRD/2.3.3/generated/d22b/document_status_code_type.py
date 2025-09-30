from dataclasses import dataclass, field
from typing import Optional

from .document_status_code_content_type import DocumentStatusCodeContentType
from .document_status_code_list_agency_idcontent_type import (
    DocumentStatusCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class DocumentStatusCodeType:
    value: Optional[DocumentStatusCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: DocumentStatusCodeListAgencyIdcontentType = field(
        init=False,
        default=DocumentStatusCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
