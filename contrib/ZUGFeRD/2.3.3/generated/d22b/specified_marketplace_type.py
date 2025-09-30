from dataclasses import dataclass, field
from typing import Optional

from .available_period_type import AvailablePeriodType
from .code_type import CodeType
from .idtype import Idtype
from .indicator_type import IndicatorType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SpecifiedMarketplaceType:
    """
    Marketplace.

    :ivar id: ID
    :ivar name: Name
    :ivar virtual_indicator: Virtual Indicator
    :ivar website_uriid: Website
    :ivar sales_method_code: Sales Method Code
    :ivar ordering_available_period: Available Ordering Period
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
    virtual_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "VirtualIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    website_uriid: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "WebsiteURIID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sales_method_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "SalesMethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    ordering_available_period: list[AvailablePeriodType] = field(
        default_factory=list,
        metadata={
            "name": "OrderingAvailablePeriod",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
