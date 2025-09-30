from dataclasses import dataclass, field
from typing import Optional

from .quantity_type import QuantityType
from .supply_chain_event_type import SupplyChainEventType
from .supply_chain_packaging_type import SupplyChainPackagingType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SubordinateLineTradeDeliveryType:
    """
    Subordinate Line Trade Delivery.

    :ivar package_quantity: Package Quantity
    :ivar product_unit_quantity: Product Unit Quantity
    :ivar per_package_unit_quantity: Per Package Unit Quantity
    :ivar billed_quantity: Billed Quantity
    :ivar included_supply_chain_packaging: Included Packaging
    :ivar actual_delivery_supply_chain_event: Actual Delivery Event
    """

    package_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "PackageQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    product_unit_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "ProductUnitQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    per_package_unit_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "PerPackageUnitQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    billed_quantity: list[QuantityType] = field(
        default_factory=list,
        metadata={
            "name": "BilledQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    included_supply_chain_packaging: list[SupplyChainPackagingType] = field(
        default_factory=list,
        metadata={
            "name": "IncludedSupplyChainPackaging",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_delivery_supply_chain_event: list[SupplyChainEventType] = field(
        default_factory=list,
        metadata={
            "name": "ActualDeliverySupplyChainEvent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
