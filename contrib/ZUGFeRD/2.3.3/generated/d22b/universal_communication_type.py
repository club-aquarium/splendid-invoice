from dataclasses import dataclass, field
from typing import Optional

from .communication_channel_code_type import CommunicationChannelCodeType
from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class UniversalCommunicationType:
    """
    Communication.

    :ivar uriid: URI
    :ivar channel_code: Channel Code
    :ivar complete_number: Complete Number
    """

    uriid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "URIID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    channel_code: Optional[CommunicationChannelCodeType] = field(
        default=None,
        metadata={
            "name": "ChannelCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    complete_number: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CompleteNumber",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
