from dataclasses import dataclass, field
from typing import Optional

from .currency_code_type import CurrencyCodeType
from .date_time_type import DateTimeType
from .rate_type import RateType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeCurrencyExchangeType:
    source_currency_code: Optional[CurrencyCodeType] = field(
        default=None,
        metadata={
            "name": "SourceCurrencyCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    target_currency_code: Optional[CurrencyCodeType] = field(
        default=None,
        metadata={
            "name": "TargetCurrencyCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    conversion_rate: Optional[RateType] = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    conversion_rate_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ConversionRateDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
