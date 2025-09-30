from dataclasses import dataclass, field
from typing import Optional

from .dimension_type_code_content_type import DimensionTypeCodeContentType
from .dimension_type_code_list_agency_idcontent_type import (
    DimensionTypeCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class DimensionTypeCodeType:
    value: Optional[DimensionTypeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: DimensionTypeCodeListAgencyIdcontentType = field(
        init=False,
        default=DimensionTypeCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
