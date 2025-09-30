from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .date_time_type import DateTimeType
from .document_authentication_type import DocumentAuthenticationType
from .document_code_type import DocumentCodeType
from .formatted_date_time_type import FormattedDateTimeType
from .idtype import Idtype
from .indicator_type import IndicatorType
from .message_function_code_type import MessageFunctionCodeType
from .note_type import NoteType
from .referenced_document_type import ReferencedDocumentType
from .specified_binary_file_type import SpecifiedBinaryFileType
from .specified_period_type import SpecifiedPeriodType
from .text_type import TextType
from .trade_party_type import TradePartyType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ExchangedDocumentType:
    """
    Exchanged Document.

    :ivar id: ID
    :ivar name: Name
    :ivar type_code: Type Code
    :ivar issue_date_time: Issue Date Time
    :ivar copy_indicator:
    :ivar purpose: Purpose Text
    :ivar control_requirement_indicator: Control Requirement Indicator
    :ivar language_id: Language Code
    :ivar purpose_code: Purpose Code
    :ivar revision_date_time: Revision Date Time
    :ivar version_id: Version ID
    :ivar global_id: Global ID
    :ivar revision_id: Revision ID
    :ivar previous_revision_id: Previous Revision ID
    :ivar category_code: Category Code
    :ivar requested_response_type_code: Response Request Type Code
    :ivar creation_date_time: Creation Date Time
    :ivar first_version_issue_date_time: First Version Issue Date Time
    :ivar subtype_code: Subtype Code
    :ivar included_note: Note
    :ivar reference_referenced_document: Reference Document
    :ivar signatory_document_authentication: Signatory Authentication
    :ivar effective_specified_period: Effective Period
    :ivar issuer_trade_party: Issuer
    :ivar attached_specified_binary_file: Attached File
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
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
    type_code: Optional[DocumentCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    issue_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "IssueDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
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
    purpose: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    control_requirement_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "ControlRequirementIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    language_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "LanguageID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    purpose_code: Optional[MessageFunctionCodeType] = field(
        default=None,
        metadata={
            "name": "PurposeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    revision_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "RevisionDateTime",
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
    previous_revision_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "PreviousRevisionID",
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
    requested_response_type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "RequestedResponseTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    creation_date_time: Optional[FormattedDateTimeType] = field(
        default=None,
        metadata={
            "name": "CreationDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    first_version_issue_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "FirstVersionIssueDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    subtype_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "SubtypeCode",
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
    signatory_document_authentication: Optional[DocumentAuthenticationType] = field(
        default=None,
        metadata={
            "name": "SignatoryDocumentAuthentication",
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
