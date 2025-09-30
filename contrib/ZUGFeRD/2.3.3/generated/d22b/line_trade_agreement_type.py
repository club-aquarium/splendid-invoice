from dataclasses import dataclass, field
from typing import Optional

from .referenced_document_type import ReferencedDocumentType
from .specified_marketplace_type import SpecifiedMarketplaceType
from .text_type import TextType
from .trade_delivery_terms_type import TradeDeliveryTermsType
from .trade_party_type import TradePartyType
from .trade_price_type import TradePriceType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LineTradeAgreementType:
    """
    Line Trade Agreement.

    :ivar buyer_reference: Buyer Reference Text
    :ivar buyer_requisitioner_trade_party: Buyer Requisitioner
    :ivar applicable_trade_delivery_terms: Trade Delivery Terms
    :ivar seller_order_referenced_document: Seller Order Document
    :ivar buyer_order_referenced_document: Buyer Order Document
    :ivar quotation_referenced_document: Quotation Document
    :ivar contract_referenced_document: Contract Document
    :ivar demand_forecast_referenced_document: Demand Forecast Document
    :ivar promotional_deal_referenced_document: Promotional Deal
        Document
    :ivar additional_referenced_document: Additional Document
    :ivar gross_price_product_trade_price: Product Gross Price
    :ivar net_price_product_trade_price: Product Net Price
    :ivar requisitioner_referenced_document: Requisitioner Document
    :ivar item_seller_trade_party: Item Seller
    :ivar item_buyer_trade_party: Item Buyer
    :ivar included_specified_marketplace: Marketplace
    :ivar ultimate_customer_order_referenced_document: Ultimate Customer
        Order Document
    """

    buyer_reference: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "BuyerReference",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_requisitioner_trade_party: list[TradePartyType] = field(
        default_factory=list,
        metadata={
            "name": "BuyerRequisitionerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_trade_delivery_terms: Optional[TradeDeliveryTermsType] = field(
        default=None,
        metadata={
            "name": "ApplicableTradeDeliveryTerms",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    seller_order_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "SellerOrderReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_order_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "BuyerOrderReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    quotation_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "QuotationReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    contract_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "ContractReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    demand_forecast_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "DemandForecastReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    promotional_deal_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "PromotionalDealReferencedDocument",
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
    gross_price_product_trade_price: Optional[TradePriceType] = field(
        default=None,
        metadata={
            "name": "GrossPriceProductTradePrice",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    net_price_product_trade_price: Optional[TradePriceType] = field(
        default=None,
        metadata={
            "name": "NetPriceProductTradePrice",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    requisitioner_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "RequisitionerReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    item_seller_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "ItemSellerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    item_buyer_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "ItemBuyerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    included_specified_marketplace: Optional[SpecifiedMarketplaceType] = field(
        default=None,
        metadata={
            "name": "IncludedSpecifiedMarketplace",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    ultimate_customer_order_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "UltimateCustomerOrderReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
