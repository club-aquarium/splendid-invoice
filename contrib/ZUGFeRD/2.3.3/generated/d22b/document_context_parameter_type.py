from dataclasses import dataclass, field
from typing import Optional

from .document_version_type import DocumentVersionType
from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class DocumentContextParameterType:
    """
    Document Context Parameter.

    :ivar id: ID
    :ivar value: Value Text
    :ivar specified_document_version: Version
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    value: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_document_version: Optional[DocumentVersionType] = field(
        default=None,
        metadata={
            "name": "SpecifiedDocumentVersion",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
