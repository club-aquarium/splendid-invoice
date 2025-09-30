from dataclasses import dataclass, field
from typing import Optional

from .geographical_coordinate_type import GeographicalCoordinateType
from .idtype import Idtype
from .location_function_code_type import LocationFunctionCodeType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SubordinateLocationType:
    """
    Subordinate Location.

    :ivar id: ID
    :ivar name: Name
    :ivar type_code: Type Code
    :ivar physical_geographical_coordinate: Physical Geographical
        Coordinate
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
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
        },
    )
    type_code: Optional[LocationFunctionCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    physical_geographical_coordinate: Optional[GeographicalCoordinateType] = field(
        default=None,
        metadata={
            "name": "PhysicalGeographicalCoordinate",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
