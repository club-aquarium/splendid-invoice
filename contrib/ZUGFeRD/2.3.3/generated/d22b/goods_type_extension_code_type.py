from dataclasses import dataclass, field
from typing import Optional

from .goods_type_extension_code_content_type import (
    GoodsTypeExtensionCodeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class GoodsTypeExtensionCodeType:
    value: Optional[GoodsTypeExtensionCodeContentType] = field(
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
