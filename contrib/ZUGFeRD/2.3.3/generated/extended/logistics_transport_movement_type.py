from dataclasses import dataclass, field
from typing import Optional

from .transport_mode_code_type import TransportModeCodeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LogisticsTransportMovementType:
    mode_code: Optional[TransportModeCodeType] = field(
        default=None,
        metadata={
            "name": "ModeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
