from dataclasses import dataclass, field
from typing import Optional

from .currency_code_type import CurrencyCodeType
from .date_time_type import DateTimeType
from .idtype import Idtype
from .numeric_type import NumericType
from .rate_type import RateType
from .referenced_document_type import ReferencedDocumentType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeCurrencyExchangeType:
    """
    Trade Currency Exchange.

    :ivar source_currency_code: Source Currency Code
    :ivar source_unit_basis_numeric: Source Unit Basis
    :ivar target_currency_code: Target Currency Code
    :ivar target_unit_base_numeric: Target Unit Basis
    :ivar market_id: Market ID
    :ivar conversion_rate: Conversion Rate
    :ivar conversion_rate_date_time: Conversion Rate Date Time
    :ivar associated_referenced_document: Associated Document
    """

    source_currency_code: Optional[CurrencyCodeType] = field(
        default=None,
        metadata={
            "name": "SourceCurrencyCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    source_unit_basis_numeric: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "SourceUnitBasisNumeric",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
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
    target_unit_base_numeric: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "TargetUnitBaseNumeric",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    market_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "MarketID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
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
    associated_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
