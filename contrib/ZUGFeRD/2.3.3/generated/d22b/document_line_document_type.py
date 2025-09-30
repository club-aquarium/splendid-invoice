from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .line_status_code_type import LineStatusCodeType
from .note_type import NoteType
from .referenced_document_type import ReferencedDocumentType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class DocumentLineDocumentType:
    """
    Document Line.

    :ivar line_id: Line ID
    :ivar parent_line_id: Parent Line ID
    :ivar line_status_code: Status Code
    :ivar line_status_reason_code: Status Reason Code
    :ivar category_code: Category Code
    :ivar response_reason_code: Response Reason Code
    :ivar included_note: Note
    :ivar reference_referenced_document: Reference Document
    """

    line_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "LineID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    parent_line_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ParentLineID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    line_status_code: Optional[LineStatusCodeType] = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    line_status_reason_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "LineStatusReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    category_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    response_reason_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ResponseReasonCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    included_note: list[NoteType] = field(
        default_factory=list,
        metadata={
            "name": "IncludedNote",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    reference_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
