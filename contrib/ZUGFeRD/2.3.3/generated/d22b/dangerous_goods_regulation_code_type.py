from dataclasses import dataclass, field
from typing import Optional

from .dangerous_goods_regulation_code_content_type import (
    DangerousGoodsRegulationCodeContentType,
)
from .dangerous_goods_regulation_code_list_agency_idcontent_type import (
    DangerousGoodsRegulationCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class DangerousGoodsRegulationCodeType:
    value: Optional[DangerousGoodsRegulationCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: DangerousGoodsRegulationCodeListAgencyIdcontentType = field(
        init=False,
        default=DangerousGoodsRegulationCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
