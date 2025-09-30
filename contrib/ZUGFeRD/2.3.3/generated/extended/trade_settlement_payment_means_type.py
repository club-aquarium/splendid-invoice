from dataclasses import dataclass, field
from typing import Optional

from .creditor_financial_account_type import CreditorFinancialAccountType
from .creditor_financial_institution_type import (
    CreditorFinancialInstitutionType,
)
from .debtor_financial_account_type import DebtorFinancialAccountType
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
    type_code: Optional[PaymentMeansCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    information: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Information",
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
    payee_party_creditor_financial_account: Optional[CreditorFinancialAccountType] = (
        field(
            default=None,
            metadata={
                "name": "PayeePartyCreditorFinancialAccount",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
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
