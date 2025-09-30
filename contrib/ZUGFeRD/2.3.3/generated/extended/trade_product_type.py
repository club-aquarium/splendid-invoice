from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype
from .product_characteristic_type import ProductCharacteristicType
from .product_classification_type import ProductClassificationType
from .referenced_product_type import ReferencedProductType
from .text_type import TextType
from .trade_country_type import TradeCountryType
from .trade_product_instance_type import TradeProductInstanceType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeProductType:
    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
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
    industry_assigned_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "IndustryAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    model_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ModelID",
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
    batch_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "BatchID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    brand_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "BrandName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    model_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ModelName",
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
    individual_trade_product_instance: list[TradeProductInstanceType] = field(
        default_factory=list,
        metadata={
            "name": "IndividualTradeProductInstance",
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
    included_referenced_product: list[ReferencedProductType] = field(
        default_factory=list,
        metadata={
            "name": "IncludedReferencedProduct",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
