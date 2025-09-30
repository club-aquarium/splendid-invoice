from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .date_time_type import DateTimeType
from .financial_adjustment_type import FinancialAdjustmentType
from .indicator_type import IndicatorType
from .logistics_service_charge_type import LogisticsServiceChargeType
from .referenced_document_type import ReferencedDocumentType
from .specified_period_type import SpecifiedPeriodType
from .text_type import TextType
from .trade_accounting_account_type import TradeAccountingAccountType
from .trade_allowance_charge_type import TradeAllowanceChargeType
from .trade_payment_terms_type import TradePaymentTermsType
from .trade_settlement_financial_card_type import (
    TradeSettlementFinancialCardType,
)
from .trade_settlement_line_monetary_summation_type import (
    TradeSettlementLineMonetarySummationType,
)
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LineTradeSettlementType:
    """
    Line Trade Settlement.

    :ivar payment_reference: Payment Reference Text
    :ivar invoice_issuer_reference: Invoice Issuer Reference Text
    :ivar total_adjustment_amount: Total Adjustment Amount
    :ivar discount_indicator: Discount Indicator
    :ivar invoice_date_time: Invoice Date Time
    :ivar applicable_trade_tax: Trade Tax
    :ivar billing_specified_period: Billing Period
    :ivar specified_trade_allowance_charge: Allowance/Charge
    :ivar subtotal_calculated_trade_tax: Subtotal Calculated Tax
    :ivar specified_logistics_service_charge: Logistics Service Charge
    :ivar specified_trade_payment_terms: Payment Terms
    :ivar specified_trade_settlement_line_monetary_summation: Monetary
        Summation
    :ivar specified_financial_adjustment: Financial Adjustment
    :ivar invoice_referenced_document: Invoice Document
    :ivar additional_referenced_document: Additional Document
    :ivar payable_specified_trade_accounting_account: Accounts Payable
    :ivar receivable_specified_trade_accounting_account: Accounts
        Receivable
    :ivar purchase_specified_trade_accounting_account: Purchase
        Accounting Account
    :ivar sales_specified_trade_accounting_account: Sales Accounting
        Account
    :ivar specified_trade_settlement_financial_card: Financial Card
    """

    payment_reference: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "PaymentReference",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoice_issuer_reference: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "InvoiceIssuerReference",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_adjustment_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "TotalAdjustmentAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    discount_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "DiscountIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoice_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "InvoiceDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_trade_tax: list[TradeTaxType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    billing_specified_period: Optional[SpecifiedPeriodType] = field(
        default=None,
        metadata={
            "name": "BillingSpecifiedPeriod",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_trade_allowance_charge: list[TradeAllowanceChargeType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedTradeAllowanceCharge",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    subtotal_calculated_trade_tax: list[TradeTaxType] = field(
        default_factory=list,
        metadata={
            "name": "SubtotalCalculatedTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_logistics_service_charge: list[LogisticsServiceChargeType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedLogisticsServiceCharge",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_trade_payment_terms: list[TradePaymentTermsType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedTradePaymentTerms",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_trade_settlement_line_monetary_summation: Optional[
        TradeSettlementLineMonetarySummationType
    ] = field(
        default=None,
        metadata={
            "name": "SpecifiedTradeSettlementLineMonetarySummation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_financial_adjustment: list[FinancialAdjustmentType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedFinancialAdjustment",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoice_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payable_specified_trade_accounting_account: list[TradeAccountingAccountType] = (
        field(
            default_factory=list,
            metadata={
                "name": "PayableSpecifiedTradeAccountingAccount",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    receivable_specified_trade_accounting_account: list[TradeAccountingAccountType] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReceivableSpecifiedTradeAccountingAccount",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    purchase_specified_trade_accounting_account: list[TradeAccountingAccountType] = (
        field(
            default_factory=list,
            metadata={
                "name": "PurchaseSpecifiedTradeAccountingAccount",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    sales_specified_trade_accounting_account: list[TradeAccountingAccountType] = field(
        default_factory=list,
        metadata={
            "name": "SalesSpecifiedTradeAccountingAccount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_trade_settlement_financial_card: Optional[
        TradeSettlementFinancialCardType
    ] = field(
        default=None,
        metadata={
            "name": "SpecifiedTradeSettlementFinancialCard",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
