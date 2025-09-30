from dataclasses import dataclass, field
from typing import Optional

from .binary_object_type import BinaryObjectType
from .document_code_type import DocumentCodeType
from .formatted_date_time_type import FormattedDateTimeType
from .idtype import Idtype
from .reference_code_type import ReferenceCodeType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ReferencedDocumentType:
    issuer_assigned_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "IssuerAssignedID",
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
    line_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "LineID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[DocumentCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    attachment_binary_object: Optional[BinaryObjectType] = field(
        default=None,
        metadata={
            "name": "AttachmentBinaryObject",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    reference_type_code: Optional[ReferenceCodeType] = field(
        default=None,
        metadata={
            "name": "ReferenceTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    formatted_issue_date_time: Optional[FormattedDateTimeType] = field(
        default=None,
        metadata={
            "name": "FormattedIssueDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
