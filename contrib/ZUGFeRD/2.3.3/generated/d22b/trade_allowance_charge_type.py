from dataclasses import dataclass, field
from typing import Optional

from .allowance_charge_identification_code_type import (
    AllowanceChargeIdentificationCodeType,
)
from .allowance_charge_reason_code_type import AllowanceChargeReasonCodeType
from .amount_type import AmountType
from .idtype import Idtype
from .indicator_type import IndicatorType
from .numeric_type import NumericType
from .percent_type import PercentType
from .quantity_type import QuantityType
from .text_type import TextType
from .trade_currency_exchange_type import TradeCurrencyExchangeType
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeAllowanceChargeType:
    """
    Trade Allowance/Charge.

    :ivar charge_indicator: Charge Indicator
    :ivar id: ID
    :ivar sequence_numeric: Sequence Number
    :ivar calculation_percent: Calculation Percent
    :ivar basis_amount: Basis Amount
    :ivar basis_quantity: Basis Quantity
    :ivar prepaid_indicator: Prepaid Indicator
    :ivar actual_amount: Actual Amount
    :ivar unit_basis_amount: Unit Basis Amount
    :ivar reason_code: Reason Code
    :ivar reason: Reason Text
    :ivar type_code: Type Code
    :ivar category_trade_tax: Tax Category
    :ivar actual_trade_currency_exchange: Actual Currency Exchange
    """

    charge_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "ChargeIndicator",
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
    sequence_numeric: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    calculation_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "CalculationPercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    basis_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "BasisAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    basis_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "BasisQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    prepaid_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "PrepaidIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "ActualAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    unit_basis_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "UnitBasisAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    reason_code: Optional[AllowanceChargeReasonCodeType] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    reason: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[AllowanceChargeIdentificationCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    category_trade_tax: list[TradeTaxType] = field(
        default_factory=list,
        metadata={
            "name": "CategoryTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_trade_currency_exchange: Optional[TradeCurrencyExchangeType] = field(
        default=None,
        metadata={
            "name": "ActualTradeCurrencyExchange",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
