from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .code_type import CodeType
from .date_only_formatted_date_time_type import DateOnlyFormattedDateTimeType
from .date_type import DateType
from .idtype import Idtype
from .indicator_type import IndicatorType
from .numeric_type import NumericType
from .percent_type import PercentType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeSettlementFinancialCardType:
    """
    Trade Settlement Financial Card.

    :ivar microchip_indicator: Microchip Indicator
    :ivar id: ID
    :ivar type_code: Type Code
    :ivar cardholder_name: Cardholder Name
    :ivar expiry_date: Expiry Date
    :ivar verification_numeric: Verification Number
    :ivar valid_from_date_time: Valid From Date
    :ivar credit_limit_amount: Credit Limit Amount
    :ivar credit_available_amount: Credit Available Amount
    :ivar interest_rate_percent: Interest Rate
    :ivar issuing_company_name: Issuing Company Name
    :ivar description: Description
    """

    microchip_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "MicrochipIndicator",
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
    type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    cardholder_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CardholderName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    expiry_date: Optional[DateType] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    verification_numeric: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "VerificationNumeric",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    valid_from_date_time: Optional[DateOnlyFormattedDateTimeType] = field(
        default=None,
        metadata={
            "name": "ValidFromDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    credit_limit_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "CreditLimitAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    credit_available_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "CreditAvailableAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    interest_rate_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "InterestRatePercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    issuing_company_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "IssuingCompanyName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
