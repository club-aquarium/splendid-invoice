from dataclasses import dataclass, field
from typing import Optional

from .location_function_code_content_type import (
    LocationFunctionCodeContentType,
)
from .location_function_code_list_agency_idcontent_type import (
    LocationFunctionCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class LocationFunctionCodeType:
    value: Optional[LocationFunctionCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: LocationFunctionCodeListAgencyIdcontentType = field(
        init=False,
        default=LocationFunctionCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
