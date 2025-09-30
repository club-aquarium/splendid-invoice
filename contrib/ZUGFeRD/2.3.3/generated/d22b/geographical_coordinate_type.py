from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype
from .measure_type import MeasureType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class GeographicalCoordinateType:
    """
    Geographical Coordinate.

    :ivar altitude_measure: Altitude
    :ivar latitude_measure: Latitude
    :ivar longitude_measure: Longitude
    :ivar system_id: System ID
    """

    altitude_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "AltitudeMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    latitude_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "LatitudeMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    longitude_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "LongitudeMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    system_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SystemID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
