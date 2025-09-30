from dataclasses import dataclass, field
from typing import Optional

from .dangerous_goods_packaging_level_code_list_agency_idcontent_type import (
    DangerousGoodsPackagingLevelCodeListAgencyIdcontentType,
)
from .dangerous_goods_packing_code_content_type import (
    DangerousGoodsPackingCodeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class DangerousGoodsPackagingLevelCodeType:
    value: Optional[DangerousGoodsPackingCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: DangerousGoodsPackagingLevelCodeListAgencyIdcontentType = field(
        init=False,
        default=DangerousGoodsPackagingLevelCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
