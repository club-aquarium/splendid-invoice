from dataclasses import dataclass, field
from typing import Optional

from .referenced_document_type import ReferencedDocumentType
from .trade_price_type import TradePriceType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LineTradeAgreementType:
    buyer_order_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "BuyerOrderReferencedDocument",
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
