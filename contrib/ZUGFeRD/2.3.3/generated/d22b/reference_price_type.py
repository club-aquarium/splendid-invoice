from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .code_type import CodeType
from .indicator_type import IndicatorType
from .quantity_type import QuantityType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ReferencePriceType:
    """
    Reference Price.

    :ivar charge_amount: Charge Amount
    :ivar basis_quantity: Basis Quantity
    :ivar net_price_indicator: Net Price Indicator
    :ivar comparison_method_code: Comparison Method Code
    """

    charge_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "ChargeAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    basis_quantity: list[QuantityType] = field(
        default_factory=list,
        metadata={
            "name": "BasisQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    net_price_indicator: list[IndicatorType] = field(
        default_factory=list,
        metadata={
            "name": "NetPriceIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    comparison_method_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ComparisonMethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
