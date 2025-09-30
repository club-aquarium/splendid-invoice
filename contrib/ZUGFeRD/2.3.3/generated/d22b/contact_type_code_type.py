from dataclasses import dataclass, field
from typing import Optional

from .contact_function_code_content_type import ContactFunctionCodeContentType
from .contact_type_code_list_agency_idcontent_type import (
    ContactTypeCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class ContactTypeCodeType:
    value: Optional[ContactFunctionCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: ContactTypeCodeListAgencyIdcontentType = field(
        init=False,
        default=ContactTypeCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
