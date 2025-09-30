from dataclasses import dataclass, field
from typing import Optional

from .trade_price_type import TradePriceType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LineTradeAgreementType:
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
