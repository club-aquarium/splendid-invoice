from dataclasses import dataclass, field
from typing import Optional

from .payment_guarantee_means_code_content_type import (
    PaymentGuaranteeMeansCodeContentType,
)
from .payment_guarantee_means_code_list_agency_idcontent_type import (
    PaymentGuaranteeMeansCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PaymentGuaranteeMeansCodeType:
    value: Optional[PaymentGuaranteeMeansCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: PaymentGuaranteeMeansCodeListAgencyIdcontentType = field(
        init=False,
        default=PaymentGuaranteeMeansCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
