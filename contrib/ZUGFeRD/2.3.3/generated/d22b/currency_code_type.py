from dataclasses import dataclass, field
from typing import Optional

from .currency_code_list_agency_idcontent_type import (
    CurrencyCodeListAgencyIdcontentType,
)
from .iso3_alpha_currency_code_content_type import (
    Iso3AlphaCurrencyCodeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class CurrencyCodeType:
    value: Optional[Iso3AlphaCurrencyCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: CurrencyCodeListAgencyIdcontentType = field(
        init=False,
        default=CurrencyCodeListAgencyIdcontentType.VALUE_5,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
