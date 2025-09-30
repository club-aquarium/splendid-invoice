from dataclasses import dataclass, field
from typing import Optional

from .price_type_code_content_type import PriceTypeCodeContentType
from .price_type_code_list_agency_idcontent_type import (
    PriceTypeCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PriceTypeCodeType:
    value: Optional[PriceTypeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: PriceTypeCodeListAgencyIdcontentType = field(
        init=False,
        default=PriceTypeCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
