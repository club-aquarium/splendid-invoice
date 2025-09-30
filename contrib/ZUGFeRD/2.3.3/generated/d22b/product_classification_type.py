from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .product_characteristic_type import ProductCharacteristicType
from .referenced_standard_type import ReferencedStandardType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ProductClassificationType:
    """
    Product Classification.

    :ivar system_id: System ID
    :ivar system_name: System Name
    :ivar class_code: Class Code
    :ivar class_name: Class Name
    :ivar sub_class_code: Sub-Class Code
    :ivar class_product_characteristic: Product Class Characteristic
    :ivar applicable_referenced_standard: Applicable Referenced Standard
    """

    system_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SystemID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    system_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "SystemName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    class_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    class_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "ClassName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sub_class_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "SubClassCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    class_product_characteristic: list[ProductCharacteristicType] = field(
        default_factory=list,
        metadata={
            "name": "ClassProductCharacteristic",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_referenced_standard: Optional[ReferencedStandardType] = field(
        default=None,
        metadata={
            "name": "ApplicableReferencedStandard",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
