from dataclasses import dataclass, field
from typing import Optional

from .country_idscheme_agency_idcontent_type import (
    CountryIdschemeAgencyIdcontentType,
)
from .isotwoletter_country_code_content_type import (
    IsotwoletterCountryCodeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class CountryIdtype:
    class Meta:
        name = "CountryIDType"

    value: Optional[IsotwoletterCountryCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    scheme_agency_id: Optional[CountryIdschemeAgencyIdcontentType] = field(
        default=None,
        metadata={
            "name": "schemeAgencyID",
            "type": "Attribute",
        },
    )
