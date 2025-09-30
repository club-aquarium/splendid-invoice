from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype
from .product_characteristic_type import ProductCharacteristicType
from .product_classification_type import ProductClassificationType
from .text_type import TextType
from .trade_country_type import TradeCountryType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeProductType:
    global_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "GlobalID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    seller_assigned_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SellerAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_assigned_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "BuyerAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_product_characteristic: list[ProductCharacteristicType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableProductCharacteristic",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    designated_product_classification: list[ProductClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "DesignatedProductClassification",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    origin_trade_country: Optional[TradeCountryType] = field(
        default=None,
        metadata={
            "name": "OriginTradeCountry",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
