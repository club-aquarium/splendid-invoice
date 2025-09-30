from dataclasses import dataclass, field
from typing import Optional

from .advance_payment_type import AdvancePaymentType
from .amount_type import AmountType
from .code_type import CodeType
from .currency_code_type import CurrencyCodeType
from .date_time_type import DateTimeType
from .financial_adjustment_type import FinancialAdjustmentType
from .idtype import Idtype
from .logistics_service_charge_type import LogisticsServiceChargeType
from .referenced_document_type import ReferencedDocumentType
from .specified_period_type import SpecifiedPeriodType
from .text_type import TextType
from .trade_accounting_account_type import TradeAccountingAccountType
from .trade_allowance_charge_type import TradeAllowanceChargeType
from .trade_currency_exchange_type import TradeCurrencyExchangeType
from .trade_party_type import TradePartyType
from .trade_payment_terms_type import TradePaymentTermsType
from .trade_settlement_financial_card_type import (
    TradeSettlementFinancialCardType,
)
from .trade_settlement_header_monetary_summation_type import (
    TradeSettlementHeaderMonetarySummationType,
)
from .trade_settlement_payment_means_type import (
    TradeSettlementPaymentMeansType,
)
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class HeaderTradeSettlementType:
    """
    Header Trade Settlement.

    :ivar due_payable_amount: Due Payable Amount
    :ivar creditor_reference_type_code: Creditor Reference Type Code
    :ivar creditor_reference_type: Creditor Reference Type Text
    :ivar creditor_reference_issuer_id: Creditor Reference Issuer ID
    :ivar creditor_reference_id: Creditor Reference ID
    :ivar payment_reference: Payment Reference Text
    :ivar tax_currency_code: Tax Currency Code
    :ivar invoice_currency_code: Invoice Currency Code
    :ivar payment_currency_code: Payment Currency Code
    :ivar invoice_issuer_reference: Invoice Issuer Reference Text
    :ivar invoice_date_time: Invoice Date Time
    :ivar next_invoice_date_time: Next Invoice Date Time
    :ivar credit_reason_code: Credit Reason Code
    :ivar credit_reason: Credit Reason Text
    :ivar invoicer_trade_party: Invoicer
    :ivar invoicee_trade_party: Invoicee
    :ivar payee_trade_party: Payee
    :ivar payer_trade_party: Payer
    :ivar tax_applicable_trade_currency_exchange: Tax Currency Exchange
    :ivar invoice_applicable_trade_currency_exchange: Invoice Currency
        Exchange
    :ivar payment_applicable_trade_currency_exchange: Payment Currency
        Exchange
    :ivar specified_trade_settlement_payment_means: Payment Means
    :ivar applicable_trade_tax: Trade Tax
    :ivar billing_specified_period: Billing Period
    :ivar specified_trade_allowance_charge: Allowance/Charge
    :ivar subtotal_calculated_trade_tax: Subtotal Calculated Tax
    :ivar specified_logistics_service_charge: Logistics Service Charge
    :ivar specified_trade_payment_terms: Payment Terms
    :ivar specified_trade_settlement_header_monetary_summation: Monetary
        Summation
    :ivar specified_financial_adjustment: Financial Adjustment
    :ivar invoice_referenced_document: Invoice Document
    :ivar pro_forma_invoice_referenced_document: Pro-Forma Invoice
        Document
    :ivar letter_of_credit_referenced_document: Letter Of Credit
        Document
    :ivar factoring_agreement_referenced_document: Factoring Agreement
        Document
    :ivar factoring_list_referenced_document: Factoring List Document
    :ivar payable_specified_trade_accounting_account: Accounts Payable
    :ivar receivable_specified_trade_accounting_account: Accounts
        Receivable
    :ivar purchase_specified_trade_accounting_account: Purchase
        Accounting Account
    :ivar sales_specified_trade_accounting_account: Sales Accounting
        Account
    :ivar specified_trade_settlement_financial_card: Financial Card
    :ivar specified_advance_payment: Advance Payment
    :ivar ultimate_payee_trade_party: Ultimate Payee
    """

    due_payable_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "DuePayableAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    creditor_reference_type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "CreditorReferenceTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    creditor_reference_type: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "CreditorReferenceType",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    creditor_reference_issuer_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "CreditorReferenceIssuerID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    creditor_reference_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "CreditorReferenceID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payment_reference: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "PaymentReference",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    tax_currency_code: Optional[CurrencyCodeType] = field(
        default=None,
        metadata={
            "name": "TaxCurrencyCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoice_currency_code: Optional[CurrencyCodeType] = field(
        default=None,
        metadata={
            "name": "InvoiceCurrencyCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payment_currency_code: Optional[CurrencyCodeType] = field(
        default=None,
        metadata={
            "name": "PaymentCurrencyCode",
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
    invoice_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "InvoiceDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    next_invoice_date_time: list[DateTimeType] = field(
        default_factory=list,
        metadata={
            "name": "NextInvoiceDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    credit_reason_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CreditReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    credit_reason: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "CreditReason",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoicer_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "InvoicerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoicee_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "InvoiceeTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payee_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "PayeeTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payer_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "PayerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    tax_applicable_trade_currency_exchange: Optional[TradeCurrencyExchangeType] = field(
        default=None,
        metadata={
            "name": "TaxApplicableTradeCurrencyExchange",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoice_applicable_trade_currency_exchange: Optional[TradeCurrencyExchangeType] = (
        field(
            default=None,
            metadata={
                "name": "InvoiceApplicableTradeCurrencyExchange",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    payment_applicable_trade_currency_exchange: Optional[TradeCurrencyExchangeType] = (
        field(
            default=None,
            metadata={
                "name": "PaymentApplicableTradeCurrencyExchange",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    specified_trade_settlement_payment_means: list[TradeSettlementPaymentMeansType] = (
        field(
            default_factory=list,
            metadata={
                "name": "SpecifiedTradeSettlementPaymentMeans",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
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
    specified_trade_settlement_header_monetary_summation: Optional[
        TradeSettlementHeaderMonetarySummationType
    ] = field(
        default=None,
        metadata={
            "name": "SpecifiedTradeSettlementHeaderMonetarySummation",
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
    pro_forma_invoice_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "ProFormaInvoiceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    letter_of_credit_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "LetterOfCreditReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    factoring_agreement_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "FactoringAgreementReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    factoring_list_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "FactoringListReferencedDocument",
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
    specified_trade_settlement_financial_card: list[
        TradeSettlementFinancialCardType
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedTradeSettlementFinancialCard",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_advance_payment: list[AdvancePaymentType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedAdvancePayment",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    ultimate_payee_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "UltimatePayeeTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
