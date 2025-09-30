from dataclasses import dataclass, field
from typing import Optional

from .event_time_reference_code_payment_terms_event_content_type import (
    EventTimeReferenceCodePaymentTermsEventContentType,
)
from .payment_terms_event_time_reference_code_list_agency_idcontent_type import (
    PaymentTermsEventTimeReferenceCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PaymentTermsEventTimeReferenceCodeType:
    value: Optional[EventTimeReferenceCodePaymentTermsEventContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: PaymentTermsEventTimeReferenceCodeListAgencyIdcontentType = field(
        init=False,
        default=PaymentTermsEventTimeReferenceCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
