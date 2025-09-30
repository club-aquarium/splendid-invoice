from dataclasses import dataclass, field
from typing import Optional

from .cargo_operational_category_code_content_type import (
    CargoOperationalCategoryCodeContentType,
)
from .cargo_operational_category_code_list_agency_idcontent_type import (
    CargoOperationalCategoryCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class CargoOperationalCategoryCodeType:
    value: Optional[CargoOperationalCategoryCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: CargoOperationalCategoryCodeListAgencyIdcontentType = field(
        init=False,
        default=CargoOperationalCategoryCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
