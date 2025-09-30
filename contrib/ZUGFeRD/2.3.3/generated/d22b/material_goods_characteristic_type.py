from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .measure_type import MeasureType
from .percent_type import PercentType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class MaterialGoodsCharacteristicType:
    """
    Material Goods Characteristic.

    :ivar description: Description
    :ivar type_code: Type Code
    :ivar proportional_constituent_percent: Constituent Percent
    :ivar absolute_presence_weight_measure: Absolute Presence Weight
    :ivar absolute_presence_volume_measure: Absolute Presence Volume
    """

    description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    proportional_constituent_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "ProportionalConstituentPercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    absolute_presence_weight_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "AbsolutePresenceWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    absolute_presence_volume_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "AbsolutePresenceVolumeMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
