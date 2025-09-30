from dataclasses import dataclass, field
from typing import Optional

from .delivery_terms_function_code_content_type import (
    DeliveryTermsFunctionCodeContentType,
)
from .delivery_terms_function_code_list_agency_idcontent_type import (
    DeliveryTermsFunctionCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class DeliveryTermsFunctionCodeType:
    value: Optional[DeliveryTermsFunctionCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: DeliveryTermsFunctionCodeListAgencyIdcontentType = field(
        init=False,
        default=DeliveryTermsFunctionCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
