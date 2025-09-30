from dataclasses import dataclass, field
from typing import Optional

from .address_type_code_list_agency_idcontent_type import (
    AddressTypeCodeListAgencyIdcontentType,
)
from .address_type_content_type import AddressTypeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class AddressTypeCodeType:
    value: Optional[AddressTypeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_id: str = field(
        init=False,
        default="3131",
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: AddressTypeCodeListAgencyIdcontentType = field(
        init=False,
        default=AddressTypeCodeListAgencyIdcontentType.VALUE_6,
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
