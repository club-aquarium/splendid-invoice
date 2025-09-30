from dataclasses import dataclass, field
from typing import Optional

from .binary_object_type import BinaryObjectType
from .code_type import CodeType
from .date_time_type import DateTimeType
from .document_code_type import DocumentCodeType
from .document_status_code_type import DocumentStatusCodeType
from .formatted_date_time_type import FormattedDateTimeType
from .idtype import Idtype
from .indicator_type import IndicatorType
from .note_type import NoteType
from .reference_code_type import ReferenceCodeType
from .specified_binary_file_type import SpecifiedBinaryFileType
from .specified_period_type import SpecifiedPeriodType
from .text_type import TextType
from .trade_party_type import TradePartyType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ReferencedDocumentType:
    """
    Referenced Document.

    :ivar issuer_assigned_id: Issuer Assigned ID
    :ivar uriid: URI
    :ivar status_code: Status Code
    :ivar copy_indicator: Copy Indicator
    :ivar line_id: Line ID
    :ivar type_code: Type Code
    :ivar global_id: Global ID
    :ivar revision_id: Revision ID
    :ivar name: Name
    :ivar receipt_date_time: Receipt Date Time
    :ivar attachment_binary_object: Attached Binary Object
    :ivar information: Information
    :ivar category_code: Category Code
    :ivar reference_type_code: Reference Type Code
    :ivar section_name: Section Name
    :ivar previous_revision_id: Previous Revision ID
    :ivar formatted_issue_date_time: Formatted Issue Date Time
    :ivar page_id: Page ID
    :ivar subordinate_line_id: Subordinate Line ID
    :ivar subtype_code: Subtype Code
    :ivar effective_specified_period: Effective Period
    :ivar issuer_trade_party: Issuer
    :ivar attached_specified_binary_file: Attached Binary File
    :ivar included_note: Included Note
    """

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
    status_code: Optional[DocumentStatusCodeType] = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    copy_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
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
    global_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "GlobalID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    revision_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "RevisionID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    receipt_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ReceiptDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    attachment_binary_object: list[BinaryObjectType] = field(
        default_factory=list,
        metadata={
            "name": "AttachmentBinaryObject",
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
    category_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CategoryCode",
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
    section_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "SectionName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    previous_revision_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "PreviousRevisionID",
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
    page_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "PageID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    subordinate_line_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SubordinateLineID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    subtype_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "SubtypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    effective_specified_period: Optional[SpecifiedPeriodType] = field(
        default=None,
        metadata={
            "name": "EffectiveSpecifiedPeriod",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    issuer_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "IssuerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    attached_specified_binary_file: list[SpecifiedBinaryFileType] = field(
        default_factory=list,
        metadata={
            "name": "AttachedSpecifiedBinaryFile",
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
