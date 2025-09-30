from dataclasses import dataclass, field
from typing import Optional

from .cargo_category_code_type import CargoCategoryCodeType
from .cargo_commodity_category_code_type import CargoCommodityCategoryCodeType
from .cargo_operational_category_code_type import (
    CargoOperationalCategoryCodeType,
)
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TransportCargoType:
    """
    Transport Cargo.

    :ivar type_code: Type Code
    :ivar identification: Identification Text
    :ivar operational_category_code: Operational Category Code
    :ivar statistical_classification_code: Statistical Classification
        Code
    """

    type_code: Optional[CargoCategoryCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    identification: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Identification",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    operational_category_code: Optional[CargoOperationalCategoryCodeType] = field(
        default=None,
        metadata={
            "name": "OperationalCategoryCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    statistical_classification_code: Optional[CargoCommodityCategoryCodeType] = field(
        default=None,
        metadata={
            "name": "StatisticalClassificationCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
