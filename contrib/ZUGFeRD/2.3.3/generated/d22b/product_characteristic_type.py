from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .date_time_type import DateTimeType
from .idtype import Idtype
from .indicator_type import IndicatorType
from .measure_type import MeasureType
from .product_characteristic_condition_type import (
    ProductCharacteristicConditionType,
)
from .referenced_standard_type import ReferencedStandardType
from .specified_binary_file_type import SpecifiedBinaryFileType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ProductCharacteristicType:
    """
    Product Characteristic.

    :ivar id: ID
    :ivar type_code: Type Code
    :ivar description: Description
    :ivar value_measure: Value Measure
    :ivar measurement_method_code: Measurement Method Code
    :ivar value: Value Text
    :ivar value_code: Value Code
    :ivar value_date_time: Value Date Time
    :ivar value_indicator: Value Indicator
    :ivar content_type_code: Content Type Code
    :ivar value_specified_binary_file: Value Binary File
    :ivar applicable_product_characteristic_condition: Applicable
        Condition
    :ivar applicable_referenced_standard: Applicable Referenced Standard
    """

    id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "ID",
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
    description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    value_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "ValueMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    measurement_method_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "MeasurementMethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    value: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    value_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ValueCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    value_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ValueDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    value_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "ValueIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    content_type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ContentTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    value_specified_binary_file: Optional[SpecifiedBinaryFileType] = field(
        default=None,
        metadata={
            "name": "ValueSpecifiedBinaryFile",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_product_characteristic_condition: list[
        ProductCharacteristicConditionType
    ] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableProductCharacteristicCondition",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_referenced_standard: Optional[ReferencedStandardType] = field(
        default=None,
        metadata={
            "name": "ApplicableReferencedStandard",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
