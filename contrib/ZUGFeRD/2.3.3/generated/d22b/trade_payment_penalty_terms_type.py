from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .date_time_type import DateTimeType
from .measure_type import MeasureType
from .percent_type import PercentType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradePaymentPenaltyTermsType:
    """
    Trade Payment Penalty Terms.

    :ivar basis_date_time: Basis Date Time
    :ivar basis_period_measure: Basis Period Measure
    :ivar basis_amount: Basis Amount
    :ivar calculation_percent: Calculation Percent
    :ivar actual_penalty_amount: Actual Penalty Amount
    """

    basis_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "BasisDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    basis_period_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "BasisPeriodMeasure",
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
    calculation_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "CalculationPercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_penalty_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "ActualPenaltyAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
