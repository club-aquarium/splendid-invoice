from dataclasses import dataclass, field
from typing import Optional

from .payment_means_channel_code_content_type import (
    PaymentMeansChannelCodeContentType,
)
from .payment_means_channel_code_list_agency_idcontent_type import (
    PaymentMeansChannelCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class PaymentMeansChannelCodeType:
    value: Optional[PaymentMeansChannelCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: PaymentMeansChannelCodeListAgencyIdcontentType = field(
        init=False,
        default=PaymentMeansChannelCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
