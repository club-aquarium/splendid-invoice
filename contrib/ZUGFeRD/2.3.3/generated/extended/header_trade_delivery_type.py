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
    actual_delivery_supply_chain_event: Optional[SupplyChainEventType] = field(
        default=None,
        metadata={
            "name": "ActualDeliverySupplyChainEvent",
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
