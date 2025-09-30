from dataclasses import dataclass, field
from typing import Optional

from .binary_object_type import BinaryObjectType
from .code_type import CodeType
from .idtype import Idtype
from .measure_type import MeasureType
from .specified_period_type import SpecifiedPeriodType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SpecifiedBinaryFileType:
    """
    Binary File.

    :ivar id: ID
    :ivar title: Title
    :ivar author_name: Author Name
    :ivar version_id: Version ID
    :ivar file_name: Name
    :ivar uriid: URI
    :ivar mimecode: MIME Code
    :ivar encoding_code: Encoding Code
    :ivar character_set_code: Character Set Code
    :ivar included_binary_object: Included Binary Object
    :ivar access: Access Text
    :ivar description: Description
    :ivar size_measure: Size
    :ivar access_availability_specified_period: Access Availability
        Period
    """

    id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    title: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    author_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "AuthorName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    version_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    file_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    uriid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "URIID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    mimecode: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "MIMECode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    encoding_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "EncodingCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    character_set_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CharacterSetCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    included_binary_object: list[BinaryObjectType] = field(
        default_factory=list,
        metadata={
            "name": "IncludedBinaryObject",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    access: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Access",
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
    size_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "SizeMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    access_availability_specified_period: Optional[SpecifiedPeriodType] = field(
        default=None,
        metadata={
            "name": "AccessAvailabilitySpecifiedPeriod",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
