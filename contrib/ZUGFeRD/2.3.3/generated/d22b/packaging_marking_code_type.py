from dataclasses import dataclass, field
from typing import Optional

from .packaging_marking_code_content_type import (
    PackagingMarkingCodeContentType,
)
from .packaging_marking_code_list_agency_idcontent_type import (
    PackagingMarkingCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PackagingMarkingCodeType:
    value: Optional[PackagingMarkingCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: PackagingMarkingCodeListAgencyIdcontentType = field(
        init=False,
        default=PackagingMarkingCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
