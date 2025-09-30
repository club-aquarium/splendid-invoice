from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class NoteType:
    content_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ContentCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    content: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    subject_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "SubjectCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
