from dataclasses import dataclass, field
from typing import Optional

from .delivery_terms_code_type import DeliveryTermsCodeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeDeliveryTermsType:
    delivery_type_code: Optional[DeliveryTermsCodeType] = field(
        default=None,
        metadata={
            "name": "DeliveryTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
