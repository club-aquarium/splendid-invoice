from dataclasses import dataclass, field
from typing import Optional

from .referenced_document_type import ReferencedDocumentType
from .trade_price_type import TradePriceType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LineTradeAgreementType:
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
            "required": True,
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
