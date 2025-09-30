from dataclasses import dataclass, field
from typing import Optional

from .header_trade_agreement_type import HeaderTradeAgreementType
from .header_trade_delivery_type import HeaderTradeDeliveryType
from .header_trade_settlement_type import HeaderTradeSettlementType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainTradeTransactionType:
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
