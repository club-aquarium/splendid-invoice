from dataclasses import dataclass, field
from typing import Optional

from .transport_payment_arrangement_code_content_type import (
    TransportPaymentArrangementCodeContentType,
)
from .transport_service_payment_arrangement_code_list_agency_idcontent_type import (
    TransportServicePaymentArrangementCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TransportServicePaymentArrangementCodeType:
    value: Optional[TransportPaymentArrangementCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: TransportServicePaymentArrangementCodeListAgencyIdcontentType = (
        field(
            init=False,
            default=TransportServicePaymentArrangementCodeListAgencyIdcontentType.VALUE_6,
            metadata={
                "name": "listAgencyID",
                "type": "Attribute",
            },
        )
    )
