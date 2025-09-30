from dataclasses import dataclass, field
from typing import Optional

from .creditor_financial_account_type import CreditorFinancialAccountType
from .debtor_financial_account_type import DebtorFinancialAccountType
from .payment_means_code_type import PaymentMeansCodeType

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
