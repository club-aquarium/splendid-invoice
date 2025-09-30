from dataclasses import dataclass, field
from typing import Optional

from .document_code_list_agency_idcontent_type import (
    DocumentCodeListAgencyIdcontentType,
)
from .document_name_code_content_type import DocumentNameCodeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class DocumentCodeType:
    value: Optional[DocumentNameCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: DocumentCodeListAgencyIdcontentType = field(
        init=False,
        default=DocumentCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
