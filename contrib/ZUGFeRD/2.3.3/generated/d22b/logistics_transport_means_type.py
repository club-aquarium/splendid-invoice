from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype
from .text_type import TextType
from .trade_party_type import TradePartyType
from .transport_means_type_code_type import TransportMeansTypeCodeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LogisticsTransportMeansType:
    """
    Logistics Transport Means.

    :ivar type_code: Type Code
    :ivar type_value: Type Text
    :ivar id: ID
    :ivar name: Name
    :ivar owner_trade_party: Owner
    """

    type_code: Optional[TransportMeansTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_value: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    owner_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "OwnerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
