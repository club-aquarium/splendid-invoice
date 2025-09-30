from dataclasses import dataclass, field
from typing import Optional

from .country_idtype import CountryIdtype

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeAddressType:
    country_id: Optional[CountryIdtype] = field(
        default=None,
        metadata={
            "name": "CountryID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
