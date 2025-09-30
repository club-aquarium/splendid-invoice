from dataclasses import dataclass, field
from typing import Optional

from .referenced_document_type import ReferencedDocumentType
from .supply_chain_consignment_type import SupplyChainConsignmentType
from .supply_chain_event_type import SupplyChainEventType
from .trade_party_type import TradePartyType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class HeaderTradeDeliveryType:
    """
    Header Trade Delivery.

    :ivar related_supply_chain_consignment: Related Consignment
    :ivar ship_to_trade_party: Ship To Party
    :ivar ultimate_ship_to_trade_party: Ultimate Ship To Party
    :ivar ship_from_trade_party: Ship From Party
    :ivar actual_despatch_supply_chain_event: Actual Despatch Event
    :ivar actual_pick_up_supply_chain_event: Actual Pick-Up Event
    :ivar actual_delivery_supply_chain_event: Actual Delivery Event
    :ivar actual_receipt_supply_chain_event: Actual Receipt Event
    :ivar additional_referenced_document: Additional Document
    :ivar despatch_advice_referenced_document: Despatch Advice Document
    :ivar receiving_advice_referenced_document: Receiving Advice
        Document
    :ivar delivery_note_referenced_document: Delivery Note Document
    :ivar consumption_report_referenced_document: Consumption Report
        Document
    :ivar previous_delivery_supply_chain_event: Previous Delivery Event
    :ivar packing_list_referenced_document: Packing List Document
    """

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
    previous_delivery_supply_chain_event: list[SupplyChainEventType] = field(
        default_factory=list,
        metadata={
            "name": "PreviousDeliverySupplyChainEvent",
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
