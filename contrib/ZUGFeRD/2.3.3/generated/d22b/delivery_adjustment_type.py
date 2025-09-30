from dataclasses import dataclass, field
from typing import Optional

from .adjustment_reason_code_type import AdjustmentReasonCodeType
from .amount_type import AmountType
from .date_time_type import DateTimeType
from .quantity_type import QuantityType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class DeliveryAdjustmentType:
    """
    Delivery Adjustment.

    :ivar reason_code: Reason Code
    :ivar reason: Reason Text
    :ivar actual_amount: Actual Amount
    :ivar actual_quantity: Actual Quantity
    :ivar actual_date_time: Actual Date Time
    """

    reason_code: Optional[AdjustmentReasonCodeType] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    reason: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "ActualAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "ActualQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    actual_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ActualDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
