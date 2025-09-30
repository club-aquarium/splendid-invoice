from dataclasses import dataclass, field
from typing import Optional

from .document_line_document_type import DocumentLineDocumentType
from .line_trade_agreement_type import LineTradeAgreementType
from .line_trade_delivery_type import LineTradeDeliveryType
from .line_trade_settlement_type import LineTradeSettlementType
from .trade_product_type import TradeProductType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainTradeLineItemType:
    associated_document_line_document: Optional[DocumentLineDocumentType] = field(
        default=None,
        metadata={
            "name": "AssociatedDocumentLineDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    specified_trade_product: Optional[TradeProductType] = field(
        default=None,
        metadata={
            "name": "SpecifiedTradeProduct",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    specified_line_trade_agreement: Optional[LineTradeAgreementType] = field(
        default=None,
        metadata={
            "name": "SpecifiedLineTradeAgreement",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    specified_line_trade_delivery: Optional[LineTradeDeliveryType] = field(
        default=None,
        metadata={
            "name": "SpecifiedLineTradeDelivery",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    specified_line_trade_settlement: Optional[LineTradeSettlementType] = field(
        default=None,
        metadata={
            "name": "SpecifiedLineTradeSettlement",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
