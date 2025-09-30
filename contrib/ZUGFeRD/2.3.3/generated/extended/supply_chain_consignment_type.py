from dataclasses import dataclass, field

from .logistics_transport_movement_type import LogisticsTransportMovementType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainConsignmentType:
    specified_logistics_transport_movement: list[LogisticsTransportMovementType] = (
        field(
            default_factory=list,
            metadata={
                "name": "SpecifiedLogisticsTransportMovement",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
