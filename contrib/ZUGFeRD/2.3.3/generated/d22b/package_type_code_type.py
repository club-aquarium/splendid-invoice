from dataclasses import dataclass, field
from typing import Optional

from .package_type_code_content_type import PackageTypeCodeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PackageTypeCodeType:
    value: Optional[PackageTypeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: str = field(
        init=False,
        default="6",
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
