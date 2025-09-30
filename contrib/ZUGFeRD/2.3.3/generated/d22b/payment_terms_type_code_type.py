from dataclasses import dataclass, field
from typing import Optional

from .payment_terms_type_code_content_type import (
    PaymentTermsTypeCodeContentType,
)
from .payment_terms_type_code_list_agency_idcontent_type import (
    PaymentTermsTypeCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PaymentTermsTypeCodeType:
    value: Optional[PaymentTermsTypeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: PaymentTermsTypeCodeListAgencyIdcontentType = field(
        init=False,
        default=PaymentTermsTypeCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
