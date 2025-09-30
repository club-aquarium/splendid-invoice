from dataclasses import dataclass, field
from typing import Optional

from .payment_terms_description_identifier_content_type import (
    PaymentTermsDescriptionIdentifierContentType,
)
from .payment_terms_idscheme_agency_idcontent_type import (
    PaymentTermsIdschemeAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PaymentTermsIdtype:
    class Meta:
        name = "PaymentTermsIDType"

    value: Optional[PaymentTermsDescriptionIdentifierContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    scheme_agency_id: Optional[PaymentTermsIdschemeAgencyIdcontentType] = field(
        default=None,
        metadata={
            "name": "schemeAgencyID",
            "type": "Attribute",
        },
    )
