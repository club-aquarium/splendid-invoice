from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype
from .note_type import NoteType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class DocumentLineDocumentType:
    line_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "LineID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    included_note: Optional[NoteType] = field(
        default=None,
        metadata={
            "name": "IncludedNote",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
