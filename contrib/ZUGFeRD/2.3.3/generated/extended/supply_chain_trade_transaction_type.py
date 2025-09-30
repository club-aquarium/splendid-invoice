from dataclasses import dataclass, field
from typing import Optional

from .header_trade_agreement_type import HeaderTradeAgreementType
from .header_trade_delivery_type import HeaderTradeDeliveryType
from .header_trade_settlement_type import HeaderTradeSettlementType
from .supply_chain_trade_line_item_type import SupplyChainTradeLineItemType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainTradeTransactionType:
    included_supply_chain_trade_line_item: list[SupplyChainTradeLineItemType] = field(
        default_factory=list,
        metadata={
            "name": "IncludedSupplyChainTradeLineItem",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "min_occurs": 1,
        },
    )
    applicable_header_trade_agreement: Optional[HeaderTradeAgreementType] = field(
        default=None,
        metadata={
            "name": "ApplicableHeaderTradeAgreement",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    applicable_header_trade_delivery: Optional[HeaderTradeDeliveryType] = field(
        default=None,
        metadata={
            "name": "ApplicableHeaderTradeDelivery",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    applicable_header_trade_settlement: Optional[HeaderTradeSettlementType] = field(
        default=None,
        metadata={
            "name": "ApplicableHeaderTradeSettlement",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
