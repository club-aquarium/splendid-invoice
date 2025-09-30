from dataclasses import dataclass, field
from typing import Optional

from .advance_payment_type import AdvancePaymentType
from .currency_code_type import CurrencyCodeType
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
    creditor_reference_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "CreditorReferenceID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payment_reference: Optional[TextType] = field(
        default=None,
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
            "required": True,
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
            "min_occurs": 1,
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
            "required": True,
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
    specified_advance_payment: list[AdvancePaymentType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedAdvancePayment",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
