from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .indicator_type import IndicatorType
from .linear_unit_measure_type import LinearUnitMeasureType
from .logistics_seal_type import LogisticsSealType
from .note_type import NoteType
from .spatial_dimension_type import SpatialDimensionType
from .text_type import TextType
from .transport_equipment_category_code_type import (
    TransportEquipmentCategoryCodeType,
)
from .transport_equipment_fullness_code_type import (
    TransportEquipmentFullnessCodeType,
)

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LogisticsTransportEquipmentType:
    """
    Logistics Transport Equipment.

    :ivar id: ID
    :ivar loading_length_measure: Loading Length
    :ivar category_code: Category Code
    :ivar characteristic_code: Size/Type Code
    :ivar characteristic: Characteristic Text
    :ivar used_capacity_code: Full/Empty Code
    :ivar carrier_assigned_booking_id: Carrier Assigned Booking ID
    :ivar sealed_indicator: Sealed Indicator
    :ivar returnable_indicator: Returnable Indicator
    :ivar affixed_logistics_seal: Affixed Seal
    :ivar linear_spatial_dimension: Dimensions
    :ivar applicable_note: Applicable Note
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    loading_length_measure: Optional[LinearUnitMeasureType] = field(
        default=None,
        metadata={
            "name": "LoadingLengthMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    category_code: Optional[TransportEquipmentCategoryCodeType] = field(
        default=None,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    characteristic_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CharacteristicCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    characteristic: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Characteristic",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    used_capacity_code: Optional[TransportEquipmentFullnessCodeType] = field(
        default=None,
        metadata={
            "name": "UsedCapacityCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    carrier_assigned_booking_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "CarrierAssignedBookingID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sealed_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "SealedIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    returnable_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "ReturnableIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    affixed_logistics_seal: list[LogisticsSealType] = field(
        default_factory=list,
        metadata={
            "name": "AffixedLogisticsSeal",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    linear_spatial_dimension: Optional[SpatialDimensionType] = field(
        default=None,
        metadata={
            "name": "LinearSpatialDimension",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_note: list[NoteType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableNote",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
