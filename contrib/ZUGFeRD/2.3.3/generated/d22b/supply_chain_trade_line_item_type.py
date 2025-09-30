from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .document_line_document_type import DocumentLineDocumentType
from .line_trade_agreement_type import LineTradeAgreementType
from .line_trade_delivery_type import LineTradeDeliveryType
from .line_trade_settlement_type import LineTradeSettlementType
from .note_type import NoteType
from .subordinate_trade_line_item_type import SubordinateTradeLineItemType
from .trade_product_type import TradeProductType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainTradeLineItemType:
    """
    Supply Chain Trade Line Item.

    :ivar description_code: Description Code
    :ivar associated_document_line_document: Associated Document Line
    :ivar specified_trade_product: Trade Product
    :ivar additional_information_note: Additional Information Note
    :ivar specified_line_trade_agreement: Line Trade Agreement
    :ivar specified_line_trade_delivery: Line Trade Delivery
    :ivar specified_line_trade_settlement: Line Trade Settlement
    :ivar included_subordinate_trade_line_item: Included Subordinate
        Trade Line Item
    """

    description_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "DescriptionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    associated_document_line_document: Optional[DocumentLineDocumentType] = field(
        default=None,
        metadata={
            "name": "AssociatedDocumentLineDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_trade_product: Optional[TradeProductType] = field(
        default=None,
        metadata={
            "name": "SpecifiedTradeProduct",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_information_note: list[NoteType] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInformationNote",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_line_trade_agreement: Optional[LineTradeAgreementType] = field(
        default=None,
        metadata={
            "name": "SpecifiedLineTradeAgreement",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_line_trade_delivery: Optional[LineTradeDeliveryType] = field(
        default=None,
        metadata={
            "name": "SpecifiedLineTradeDelivery",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
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
    included_subordinate_trade_line_item: list[SubordinateTradeLineItemType] = field(
        default_factory=list,
        metadata={
            "name": "IncludedSubordinateTradeLineItem",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
