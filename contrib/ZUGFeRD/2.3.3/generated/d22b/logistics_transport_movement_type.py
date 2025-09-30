from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .logistics_transport_means_type import LogisticsTransportMeansType
from .status_code_type import StatusCodeType
from .text_type import TextType
from .transport_mode_code_type import TransportModeCodeType
from .transport_movement_stage_code_type import TransportMovementStageCodeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LogisticsTransportMovementType:
    """
    Logistics Transport Movement.

    :ivar stage_code: Stage Code
    :ivar mode_code: Mode Code
    :ivar mode: Mode Text
    :ivar id: ID
    :ivar status_code: Status Code
    :ivar service_code: Service Code
    :ivar service: Service Text
    :ivar type_value: Type Text
    :ivar cycle: Cycle Text
    :ivar used_logistics_transport_means: Used Transport Means
    """

    stage_code: Optional[TransportMovementStageCodeType] = field(
        default=None,
        metadata={
            "name": "StageCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    mode_code: Optional[TransportModeCodeType] = field(
        default=None,
        metadata={
            "name": "ModeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    mode: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Mode",
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
    status_code: Optional[StatusCodeType] = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    service_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ServiceCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    service: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Service",
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
    cycle: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Cycle",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    used_logistics_transport_means: Optional[LogisticsTransportMeansType] = field(
        default=None,
        metadata={
            "name": "UsedLogisticsTransportMeans",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
