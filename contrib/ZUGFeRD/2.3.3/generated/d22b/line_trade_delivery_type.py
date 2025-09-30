from dataclasses import dataclass, field
from typing import Optional

from .delivery_adjustment_type import DeliveryAdjustmentType
from .quantity_type import QuantityType
from .referenced_document_type import ReferencedDocumentType
from .supply_chain_consignment_type import SupplyChainConsignmentType
from .supply_chain_event_type import SupplyChainEventType
from .supply_chain_packaging_type import SupplyChainPackagingType
from .trade_party_type import TradePartyType
from .weight_unit_measure_type import WeightUnitMeasureType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LineTradeDeliveryType:
    """
    Line Trade Delivery.

    :ivar requested_quantity: Requested Quantity
    :ivar received_quantity: Received Quantity
    :ivar billed_quantity: Billed Quantity
    :ivar charge_free_quantity: Charge Free Quantity
    :ivar package_quantity: Package Quantity
    :ivar product_unit_quantity: Product Unit Quantity
    :ivar per_package_unit_quantity: Per Package Unit Quantity
    :ivar net_weight_measure: Net Weight
    :ivar gross_weight_measure: Gross Weight
    :ivar theoretical_weight_measure: Theoretical Weight
    :ivar despatched_quantity: Despatched Quantity
    :ivar specified_delivery_adjustment: Delivery Adjustment
    :ivar included_supply_chain_packaging: Included Packaging
    :ivar related_supply_chain_consignment: Related Consignment
    :ivar ship_to_trade_party: Ship To Party
    :ivar ultimate_ship_to_trade_party: Ultimate Ship To Party
    :ivar ship_from_trade_party: Ship From Party
    :ivar actual_despatch_supply_chain_event: Actual Despatch Event
    :ivar actual_pick_up_supply_chain_event: Actual Pick-Up Event
    :ivar requested_delivery_supply_chain_event: Requested Delivery
        Event
    :ivar actual_delivery_supply_chain_event: Actual Delivery Event
    :ivar actual_receipt_supply_chain_event: Actual Receipt Event
    :ivar additional_referenced_document: Additional Document
    :ivar despatch_advice_referenced_document: Despatch Advice Document
    :ivar receiving_advice_referenced_document: Receiving Advice
        Document
    :ivar delivery_note_referenced_document: Delivery Note Document
    :ivar consumption_report_referenced_document: Consumption Report
        Document
    :ivar packing_list_referenced_document: Packing List Document
    """

    requested_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "RequestedQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    received_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "ReceivedQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    billed_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "BilledQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    charge_free_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "ChargeFreeQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
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
    net_weight_measure: Optional[WeightUnitMeasureType] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    gross_weight_measure: Optional[WeightUnitMeasureType] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    theoretical_weight_measure: Optional[WeightUnitMeasureType] = field(
        default=None,
        metadata={
            "name": "TheoreticalWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    despatched_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "DespatchedQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_delivery_adjustment: list[DeliveryAdjustmentType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedDeliveryAdjustment",
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
    related_supply_chain_consignment: Optional[SupplyChainConsignmentType] = field(
        default=None,
        metadata={
            "name": "RelatedSupplyChainConsignment",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    ship_to_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "ShipToTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    ultimate_ship_to_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "UltimateShipToTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    ship_from_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "ShipFromTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_despatch_supply_chain_event: Optional[SupplyChainEventType] = field(
        default=None,
        metadata={
            "name": "ActualDespatchSupplyChainEvent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_pick_up_supply_chain_event: Optional[SupplyChainEventType] = field(
        default=None,
        metadata={
            "name": "ActualPickUpSupplyChainEvent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    requested_delivery_supply_chain_event: Optional[SupplyChainEventType] = field(
        default=None,
        metadata={
            "name": "RequestedDeliverySupplyChainEvent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_delivery_supply_chain_event: Optional[SupplyChainEventType] = field(
        default=None,
        metadata={
            "name": "ActualDeliverySupplyChainEvent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_receipt_supply_chain_event: Optional[SupplyChainEventType] = field(
        default=None,
        metadata={
            "name": "ActualReceiptSupplyChainEvent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    despatch_advice_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "DespatchAdviceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    receiving_advice_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "ReceivingAdviceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    delivery_note_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "DeliveryNoteReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    consumption_report_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "ConsumptionReportReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    packing_list_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "PackingListReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
