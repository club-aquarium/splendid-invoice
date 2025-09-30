from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .quantity_type import QuantityType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ReferencedProductType:
    """
    Referenced Product.

    :ivar id: ID
    :ivar global_id: Global ID
    :ivar seller_assigned_id: Seller Assigned ID
    :ivar buyer_assigned_id: Buyer Assigned ID
    :ivar manufacturer_assigned_id: Manufacturer Assigned ID
    :ivar industry_assigned_id: Industry Assigned ID
    :ivar name: Name
    :ivar description: Description
    :ivar relationship_type_code: Relationship Type Code
    :ivar unit_quantity: Unit Quantity
    """

    id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    global_id: list[Idtype] = field(
        default_factory=list,
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
    manufacturer_assigned_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "ManufacturerAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    industry_assigned_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "IndustryAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
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
    relationship_type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "RelationshipTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    unit_quantity: list[QuantityType] = field(
        default_factory=list,
        metadata={
            "name": "UnitQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
