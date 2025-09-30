from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype

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
            "required": True,
        },
    )
