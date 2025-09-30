from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .code_type import CodeType
from .date_time_type import DateTimeType
from .formatted_date_time_type import FormattedDateTimeType
from .idtype import Idtype
from .measure_type import MeasureType
from .payment_terms_event_time_reference_code_type import (
    PaymentTermsEventTimeReferenceCodeType,
)
from .payment_terms_idtype import PaymentTermsIdtype
from .payment_terms_type_code_type import PaymentTermsTypeCodeType
from .percent_type import PercentType
from .text_type import TextType
from .trade_party_type import TradePartyType
from .trade_payment_discount_terms_type import TradePaymentDiscountTermsType
from .trade_payment_penalty_terms_type import TradePaymentPenaltyTermsType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradePaymentTermsType:
    """
    Trade Payment Terms.

    :ivar id: ID
    :ivar from_event_code: From Event Code
    :ivar settlement_period_measure: Settlement Period Measure
    :ivar description: Description
    :ivar due_date_date_time: Due Date Date Time
    :ivar type_code: Type Code
    :ivar instruction_type_code: Instruction Type Code
    :ivar direct_debit_mandate_id: Direct Debit Mandate ID
    :ivar partial_payment_percent: Partial Payment Percent
    :ivar payment_means_id: Payment Means ID
    :ivar partial_payment_amount: Partial Payment Amount
    :ivar due_date_time: Due Date Time
    :ivar bill_start_date_time: Bill Start Date Time
    :ivar applicable_trade_payment_penalty_terms: Payment Penalty Terms
    :ivar applicable_trade_payment_discount_terms: Payment Discount
        Terms
    :ivar payee_trade_party: Payee
    """

    id: Optional[PaymentTermsIdtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    from_event_code: Optional[PaymentTermsEventTimeReferenceCodeType] = field(
        default=None,
        metadata={
            "name": "FromEventCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    settlement_period_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "SettlementPeriodMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    description: list[TextType] = field(
        default_factory=list,
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
    type_code: Optional[PaymentTermsTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    instruction_type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "InstructionTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    direct_debit_mandate_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "DirectDebitMandateID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    partial_payment_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "PartialPaymentPercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payment_means_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMeansID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    partial_payment_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "PartialPaymentAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    due_date_time: Optional[FormattedDateTimeType] = field(
        default=None,
        metadata={
            "name": "DueDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    bill_start_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "BillStartDateTime",
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
    payee_trade_party: list[TradePartyType] = field(
        default_factory=list,
        metadata={
            "name": "PayeeTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
