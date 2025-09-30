from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .creditor_financial_account_type import CreditorFinancialAccountType
from .creditor_financial_institution_type import (
    CreditorFinancialInstitutionType,
)
from .debtor_financial_account_type import DebtorFinancialAccountType
from .debtor_financial_institution_type import DebtorFinancialInstitutionType
from .idtype import Idtype
from .payment_guarantee_means_code_type import PaymentGuaranteeMeansCodeType
from .payment_means_channel_code_type import PaymentMeansChannelCodeType
from .payment_means_code_type import PaymentMeansCodeType
from .text_type import TextType
from .trade_settlement_financial_card_type import (
    TradeSettlementFinancialCardType,
)

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeSettlementPaymentMeansType:
    """
    Trade Settlement Payment Means.

    :ivar payment_channel_code: Payment Channel Code
    :ivar type_code: Type Code
    :ivar guarantee_method_code: Guarantee Method Code
    :ivar payment_method_code: Payment Method Code
    :ivar information: Information
    :ivar id: ID
    :ivar applicable_trade_settlement_financial_card: Financial Card
    :ivar payer_party_debtor_financial_account: Payer Debtor Financial
        Account
    :ivar payee_party_creditor_financial_account: Payee Creditor
        Financial Account
    :ivar payer_specified_debtor_financial_institution: Payer Debtor
        Financial Institution
    :ivar payee_specified_creditor_financial_institution: Payee Creditor
        Financial Institution
    """

    payment_channel_code: Optional[PaymentMeansChannelCodeType] = field(
        default=None,
        metadata={
            "name": "PaymentChannelCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[PaymentMeansCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    guarantee_method_code: Optional[PaymentGuaranteeMeansCodeType] = field(
        default=None,
        metadata={
            "name": "GuaranteeMethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payment_method_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "PaymentMethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    information: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_trade_settlement_financial_card: Optional[
        TradeSettlementFinancialCardType
    ] = field(
        default=None,
        metadata={
            "name": "ApplicableTradeSettlementFinancialCard",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payer_party_debtor_financial_account: Optional[DebtorFinancialAccountType] = field(
        default=None,
        metadata={
            "name": "PayerPartyDebtorFinancialAccount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payee_party_creditor_financial_account: list[CreditorFinancialAccountType] = field(
        default_factory=list,
        metadata={
            "name": "PayeePartyCreditorFinancialAccount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payer_specified_debtor_financial_institution: Optional[
        DebtorFinancialInstitutionType
    ] = field(
        default=None,
        metadata={
            "name": "PayerSpecifiedDebtorFinancialInstitution",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payee_specified_creditor_financial_institution: Optional[
        CreditorFinancialInstitutionType
    ] = field(
        default=None,
        metadata={
            "name": "PayeeSpecifiedCreditorFinancialInstitution",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
