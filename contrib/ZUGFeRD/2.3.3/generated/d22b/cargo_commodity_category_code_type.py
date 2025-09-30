from dataclasses import dataclass, field
from typing import Optional

from .commodity_identification_code_content_type import (
    CommodityIdentificationCodeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class CargoCommodityCategoryCodeType:
    value: Optional[CommodityIdentificationCodeContentType] = field(
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
