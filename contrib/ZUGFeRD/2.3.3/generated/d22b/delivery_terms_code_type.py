from dataclasses import dataclass, field
from typing import Optional

from .delivery_terms_code_content_type import DeliveryTermsCodeContentType
from .delivery_terms_code_list_agency_idcontent_type import (
    DeliveryTermsCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class DeliveryTermsCodeType:
    value: Optional[DeliveryTermsCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: DeliveryTermsCodeListAgencyIdcontentType = field(
        init=False,
        default=DeliveryTermsCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
