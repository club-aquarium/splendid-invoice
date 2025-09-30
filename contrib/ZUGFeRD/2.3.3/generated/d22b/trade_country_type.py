from dataclasses import dataclass, field
from typing import Optional

from .country_idtype import CountryIdtype
from .text_type import TextType
from .trade_country_sub_division_type import TradeCountrySubDivisionType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeCountryType:
    """
    Trade Country.

    :ivar id: Code
    :ivar name: Name
    :ivar subordinate_trade_country_sub_division: Sub-Division
    """

    id: Optional[CountryIdtype] = field(
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
    subordinate_trade_country_sub_division: list[TradeCountrySubDivisionType] = field(
        default_factory=list,
        metadata={
            "name": "SubordinateTradeCountrySubDivision",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
