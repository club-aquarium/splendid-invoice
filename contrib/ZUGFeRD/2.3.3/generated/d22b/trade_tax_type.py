from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .code_type import CodeType
from .currency_code_type import CurrencyCodeType
from .date_type import DateType
from .indicator_type import IndicatorType
from .numeric_type import NumericType
from .percent_type import PercentType
from .quantity_type import QuantityType
from .rate_type import RateType
from .tax_category_code_type import TaxCategoryCodeType
from .tax_type_code_type import TaxTypeCodeType
from .text_type import TextType
from .time_reference_code_type import TimeReferenceCodeType
from .trade_accounting_account_type import TradeAccountingAccountType
from .trade_country_type import TradeCountryType
from .trade_location_type import TradeLocationType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeTaxType:
    """
    Trade Tax.

    :ivar calculated_amount: Calculated Amount
    :ivar type_code: Type Code
    :ivar exemption_reason: Exemption Reason Text
    :ivar calculated_rate: Calculated Rate
    :ivar calculation_sequence_numeric: Calculation Sequence Number
    :ivar basis_quantity: Basis Quantity
    :ivar basis_amount: Basis Amount
    :ivar unit_basis_amount: Unit Basis Amount
    :ivar line_total_basis_amount: Line Total Basis Amount
    :ivar allowance_charge_basis_amount: Allowance/Charge Basis Amount
    :ivar category_code: Category Code
    :ivar currency_code: Currency Code
    :ivar jurisdiction: Jurisdiction Text
    :ivar customs_duty_indicator: Customs Duty Indicator
    :ivar exemption_reason_code: Exemption Reason Code
    :ivar tax_basis_allowance_rate: Basis Allowance Rate
    :ivar tax_point_date: Tax Point Date
    :ivar type_value: Type Text
    :ivar information_amount: Information Amount
    :ivar category_name: Category Name
    :ivar due_date_type_code: Due Date Type Code
    :ivar rate_applicable_percent: Applicable Rate Percent
    :ivar grand_total_amount: Grand Total Amount
    :ivar calculation_method_code: Tax Calculation Method Code
    :ivar specified_trade_accounting_account: Trade Accounting Account
    :ivar service_supply_trade_country: Service Supply Country
    :ivar buyer_repayable_tax_specified_trade_accounting_account: Buyer
        Repayable Tax Accounting Account
    :ivar seller_payable_tax_specified_trade_accounting_account: Seller
        Payable Tax Accounting Account
    :ivar seller_refundable_tax_specified_trade_accounting_account:
        Seller Refundable Tax Accounting Account
    :ivar buyer_deductible_tax_specified_trade_accounting_account: Buyer
        Deductible Tax Accounting Account
    :ivar buyer_non_deductible_tax_specified_trade_accounting_account:
        Buyer Non-Deductible Tax Accounting Account
    :ivar place_applicable_trade_location: Applicable Location
    """

    calculated_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "CalculatedAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[TaxTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    exemption_reason: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ExemptionReason",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    calculated_rate: Optional[RateType] = field(
        default=None,
        metadata={
            "name": "CalculatedRate",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    calculation_sequence_numeric: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "CalculationSequenceNumeric",
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
    basis_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "BasisAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    unit_basis_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "UnitBasisAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    line_total_basis_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "LineTotalBasisAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    allowance_charge_basis_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceChargeBasisAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    category_code: Optional[TaxCategoryCodeType] = field(
        default=None,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    currency_code: Optional[CurrencyCodeType] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    jurisdiction: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Jurisdiction",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    customs_duty_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "CustomsDutyIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    exemption_reason_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ExemptionReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    tax_basis_allowance_rate: Optional[RateType] = field(
        default=None,
        metadata={
            "name": "TaxBasisAllowanceRate",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    tax_point_date: Optional[DateType] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_value: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    information_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "InformationAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    category_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "CategoryName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    due_date_type_code: Optional[TimeReferenceCodeType] = field(
        default=None,
        metadata={
            "name": "DueDateTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    rate_applicable_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "RateApplicablePercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    grand_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "GrandTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    calculation_method_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CalculationMethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_trade_accounting_account: list[TradeAccountingAccountType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedTradeAccountingAccount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    service_supply_trade_country: Optional[TradeCountryType] = field(
        default=None,
        metadata={
            "name": "ServiceSupplyTradeCountry",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_repayable_tax_specified_trade_accounting_account: Optional[
        TradeAccountingAccountType
    ] = field(
        default=None,
        metadata={
            "name": "BuyerRepayableTaxSpecifiedTradeAccountingAccount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    seller_payable_tax_specified_trade_accounting_account: Optional[
        TradeAccountingAccountType
    ] = field(
        default=None,
        metadata={
            "name": "SellerPayableTaxSpecifiedTradeAccountingAccount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    seller_refundable_tax_specified_trade_accounting_account: Optional[
        TradeAccountingAccountType
    ] = field(
        default=None,
        metadata={
            "name": "SellerRefundableTaxSpecifiedTradeAccountingAccount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_deductible_tax_specified_trade_accounting_account: Optional[
        TradeAccountingAccountType
    ] = field(
        default=None,
        metadata={
            "name": "BuyerDeductibleTaxSpecifiedTradeAccountingAccount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_non_deductible_tax_specified_trade_accounting_account: Optional[
        TradeAccountingAccountType
    ] = field(
        default=None,
        metadata={
            "name": "BuyerNonDeductibleTaxSpecifiedTradeAccountingAccount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    place_applicable_trade_location: list[TradeLocationType] = field(
        default_factory=list,
        metadata={
            "name": "PlaceApplicableTradeLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
