from dataclasses import dataclass, field
from typing import Optional

from .binary_object_type import BinaryObjectType
from .code_type import CodeType
from .date_time_type import DateTimeType
from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class DocumentAuthenticationType:
    """
    Document Authentication.

    :ivar actual_date_time: Actual Date Time
    :ivar id: ID
    :ivar information: Information
    :ivar signatory: Signatory Text
    :ivar signatory_image_binary_object: Signatory Image Binary Object
    :ivar category_code: Category Code
    """

    actual_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ActualDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    information: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    signatory: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Signatory",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    signatory_image_binary_object: Optional[BinaryObjectType] = field(
        default=None,
        metadata={
            "name": "SignatoryImageBinaryObject",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    category_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
