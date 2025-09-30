from dataclasses import dataclass, field
from typing import Optional

from .date_time_type import DateTimeType
from .idtype import Idtype
from .material_goods_characteristic_type import MaterialGoodsCharacteristicType
from .product_characteristic_type import ProductCharacteristicType
from .supply_chain_event_type import SupplyChainEventType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeProductInstanceType:
    """
    Trade Product Instance.

    :ivar global_serial_id: Global Serial ID
    :ivar batch_id: Batch ID
    :ivar kanban_id: Kanban ID
    :ivar supplier_assigned_serial_id: Supplier Assigned Serial ID
    :ivar best_before_date_time: Best Before Date Time
    :ivar expiry_date_time: Expiry Date Time
    :ivar sell_by_date_time: Sell By Date Time
    :ivar serial_id: Serial ID
    :ivar registration_id: Registration ID
    :ivar production_supply_chain_event: Production Event
    :ivar packaging_supply_chain_event: Packaging Event
    :ivar applicable_material_goods_characteristic: Material Goods
        Characteristic
    :ivar applicable_product_characteristic: Product Characteristic
    """

    global_serial_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "GlobalSerialID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    batch_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "BatchID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    kanban_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "KanbanID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    supplier_assigned_serial_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SupplierAssignedSerialID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    best_before_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "BestBeforeDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    expiry_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ExpiryDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sell_by_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "SellByDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    serial_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "SerialID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    registration_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "RegistrationID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    production_supply_chain_event: Optional[SupplyChainEventType] = field(
        default=None,
        metadata={
            "name": "ProductionSupplyChainEvent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    packaging_supply_chain_event: Optional[SupplyChainEventType] = field(
        default=None,
        metadata={
            "name": "PackagingSupplyChainEvent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_material_goods_characteristic: list[MaterialGoodsCharacteristicType] = (
        field(
            default_factory=list,
            metadata={
                "name": "ApplicableMaterialGoodsCharacteristic",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    applicable_product_characteristic: list[ProductCharacteristicType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableProductCharacteristic",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
