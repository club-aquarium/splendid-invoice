from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .automatic_data_capture_method_code_type import (
    AutomaticDataCaptureMethodCodeType,
)
from .code_type import CodeType
from .date_time_type import DateTimeType
from .packaging_marking_code_type import PackagingMarkingCodeType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class PackagingMarkingType:
    """
    Packaging Marking.

    :ivar type_code: Type Code
    :ivar content: Content Text
    :ivar content_date_time: Content Date Time
    :ivar content_amount: Content Amount
    :ivar barcode_type_code: Barcode Type Code
    :ivar content_code: Content Code
    :ivar automatic_data_capture_method_type_code: Automatic Data
        Capture Method Type Code
    """

    type_code: list[PackagingMarkingCodeType] = field(
        default_factory=list,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    content: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    content_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ContentDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    content_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "ContentAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    barcode_type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "BarcodeTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    content_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "ContentCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    automatic_data_capture_method_type_code: list[
        AutomaticDataCaptureMethodCodeType
    ] = field(
        default_factory=list,
        metadata={
            "name": "AutomaticDataCaptureMethodTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
