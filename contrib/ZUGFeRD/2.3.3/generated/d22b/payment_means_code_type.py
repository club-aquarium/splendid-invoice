from dataclasses import dataclass, field
from typing import Optional

from .payment_means_code_content_type import PaymentMeansCodeContentType
from .payment_means_code_list_agency_idcontent_type import (
    PaymentMeansCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PaymentMeansCodeType:
    value: Optional[PaymentMeansCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: PaymentMeansCodeListAgencyIdcontentType = field(
        init=False,
        default=PaymentMeansCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
