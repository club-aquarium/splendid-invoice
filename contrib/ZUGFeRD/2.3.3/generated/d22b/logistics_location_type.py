from dataclasses import dataclass, field
from typing import Optional

from .country_idtype import CountryIdtype
from .geographical_coordinate_type import GeographicalCoordinateType
from .idtype import Idtype
from .location_function_code_type import LocationFunctionCodeType
from .subordinate_location_type import SubordinateLocationType
from .text_type import TextType
from .trade_address_type import TradeAddressType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LogisticsLocationType:
    """
    Logistics Location.

    :ivar id: ID
    :ivar name: Name
    :ivar type_code: Type Code
    :ivar description: Description
    :ivar country_id: Country Code
    :ivar country_sub_division_id: Country Sub-Division ID
    :ivar physical_geographical_coordinate: Geographical Coordinates
    :ivar postal_trade_address: Postal Address
    :ivar subordinate_location: Subordinate Location
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
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
    type_code: Optional[LocationFunctionCodeType] = field(
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
    country_id: Optional[CountryIdtype] = field(
        default=None,
        metadata={
            "name": "CountryID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    country_sub_division_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "CountrySubDivisionID",
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
    postal_trade_address: Optional[TradeAddressType] = field(
        default=None,
        metadata={
            "name": "PostalTradeAddress",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    subordinate_location: Optional[SubordinateLocationType] = field(
        default=None,
        metadata={
            "name": "SubordinateLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
