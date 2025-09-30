from dataclasses import dataclass, field
from typing import Optional

from .dimension_type_code_type import DimensionTypeCodeType
from .idtype import Idtype
from .linear_unit_measure_type import LinearUnitMeasureType
from .measure_type import MeasureType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SpatialDimensionType:
    """
    Spatial Dimensions.

    :ivar value_measure: Value Measure
    :ivar type_code: Type Code
    :ivar description: Description
    :ivar width_measure: Width
    :ivar length_measure: Length
    :ivar height_measure: Height
    :ivar id: ID
    :ivar diameter_measure: Diameter
    """

    value_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "ValueMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[DimensionTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
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
    width_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "WidthMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    length_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "LengthMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    height_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "HeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    diameter_measure: Optional[LinearUnitMeasureType] = field(
        default=None,
        metadata={
            "name": "DiameterMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
