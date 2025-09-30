from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .referenced_product_type import ReferencedProductType
from .subordinate_line_trade_agreement_type import (
    SubordinateLineTradeAgreementType,
)
from .subordinate_line_trade_delivery_type import (
    SubordinateLineTradeDeliveryType,
)
from .subordinate_line_trade_settlement_type import (
    SubordinateLineTradeSettlementType,
)
from .trade_product_type import TradeProductType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SubordinateTradeLineItemType:
    """
    Subordinate Trade Line Item.

    :ivar id: ID
    :ivar response_reason_code: Response Reason Code
    :ivar category_code: Category Code
    :ivar specified_referenced_product: Referenced Product
    :ivar applicable_trade_product: Applicable Product
    :ivar specified_subordinate_line_trade_agreement: Subordinate Line
        Trade Agreement
    :ivar specified_subordinate_line_trade_delivery: Subordinate Line
        Trade Delivery
    :ivar specified_subordinate_line_trade_settlement: Subordinate Line
        Trade Settlement
    """

    id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    response_reason_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ResponseReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    category_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_referenced_product: Optional[ReferencedProductType] = field(
        default=None,
        metadata={
            "name": "SpecifiedReferencedProduct",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_trade_product: list[TradeProductType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableTradeProduct",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_subordinate_line_trade_agreement: Optional[
        SubordinateLineTradeAgreementType
    ] = field(
        default=None,
        metadata={
            "name": "SpecifiedSubordinateLineTradeAgreement",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_subordinate_line_trade_delivery: Optional[
        SubordinateLineTradeDeliveryType
    ] = field(
        default=None,
        metadata={
            "name": "SpecifiedSubordinateLineTradeDelivery",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_subordinate_line_trade_settlement: Optional[
        SubordinateLineTradeSettlementType
    ] = field(
        default=None,
        metadata={
            "name": "SpecifiedSubordinateLineTradeSettlement",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
