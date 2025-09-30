from dataclasses import dataclass, field
from typing import Optional

from .address_type_code_type import AddressTypeCodeType
from .code_type import CodeType
from .country_idtype import CountryIdtype
from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeAddressType:
    """
    Trade Address.

    :ivar id: ID
    :ivar postcode_code: Postcode
    :ivar post_office_box: Post Office Box
    :ivar building_name: Building Name
    :ivar line_one: Line One
    :ivar line_two: Line Two
    :ivar line_three: Line Three
    :ivar line_four: Line Four
    :ivar line_five: Line Five
    :ivar street_name: Street Name
    :ivar city_name: City Name
    :ivar city_sub_division_name: City Sub-Division Text
    :ivar country_id: Country Code
    :ivar country_name: Country Name
    :ivar country_sub_division_id: Country Sub-Division Code
    :ivar country_sub_division_name: Country Sub-Division Name
    :ivar attention_of: Attention Of
    :ivar care_of: Care Of
    :ivar building_number: Building Number
    :ivar department_name: Department Name
    :ivar additional_street_name: Additional Street Name
    :ivar city_id: City ID
    :ivar type_code: Type Code
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    postcode_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "PostcodeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    post_office_box: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "PostOfficeBox",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    building_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "BuildingName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    line_one: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "LineOne",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    line_two: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "LineTwo",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    line_three: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "LineThree",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    line_four: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "LineFour",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    line_five: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "LineFive",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    street_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "StreetName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    city_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CityName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    city_sub_division_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CitySubDivisionName",
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
    country_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "CountryName",
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
    country_sub_division_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "CountrySubDivisionName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    attention_of: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "AttentionOf",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    care_of: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    building_number: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "BuildingNumber",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    department_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "DepartmentName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_street_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "AdditionalStreetName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    city_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "CityID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: list[AddressTypeCodeType] = field(
        default_factory=list,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
