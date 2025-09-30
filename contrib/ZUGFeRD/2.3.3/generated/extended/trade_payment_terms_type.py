from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .date_time_type import DateTimeType
from .idtype import Idtype
from .text_type import TextType
from .trade_party_type import TradePartyType
from .trade_payment_discount_terms_type import TradePaymentDiscountTermsType
from .trade_payment_penalty_terms_type import TradePaymentPenaltyTermsType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradePaymentTermsType:
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    due_date_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "DueDateDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    direct_debit_mandate_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "DirectDebitMandateID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    partial_payment_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "PartialPaymentAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_trade_payment_penalty_terms: Optional[TradePaymentPenaltyTermsType] = (
        field(
            default=None,
            metadata={
                "name": "ApplicableTradePaymentPenaltyTerms",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    applicable_trade_payment_discount_terms: Optional[TradePaymentDiscountTermsType] = (
        field(
            default=None,
            metadata={
                "name": "ApplicableTradePaymentDiscountTerms",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    payee_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "PayeeTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
