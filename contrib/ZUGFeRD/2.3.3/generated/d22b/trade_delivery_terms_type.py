from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .delivery_terms_code_type import DeliveryTermsCodeType
from .delivery_terms_function_code_type import DeliveryTermsFunctionCodeType
from .indicator_type import IndicatorType
from .text_type import TextType
from .trade_location_type import TradeLocationType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeDeliveryTermsType:
    """
    Trade Delivery Terms.

    :ivar delivery_type_code: Code
    :ivar description: Description
    :ivar function_code: Function Code
    :ivar delivery_discontinuation_code: Delivery Discontinuation Code
    :ivar partial_delivery_allowed_indicator: Partial Delivery Allowed
        Indicator
    :ivar relevant_trade_location: Relevant Location
    """

    delivery_type_code: Optional[DeliveryTermsCodeType] = field(
        default=None,
        metadata={
            "name": "DeliveryTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    function_code: Optional[DeliveryTermsFunctionCodeType] = field(
        default=None,
        metadata={
            "name": "FunctionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    delivery_discontinuation_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "DeliveryDiscontinuationCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    partial_delivery_allowed_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "PartialDeliveryAllowedIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    relevant_trade_location: Optional[TradeLocationType] = field(
        default=None,
        metadata={
            "name": "RelevantTradeLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
