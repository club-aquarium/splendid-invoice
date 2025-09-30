from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ReferencedStandardType:
    """
    Referenced Standard.

    :ivar id: ID
    :ivar version_id: Version ID
    :ivar element_version_id: Element Version ID
    :ivar uriid: URI
    :ivar part_id: Part ID
    :ivar agency_id: Agency ID
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
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
    element_version_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ElementVersionID",
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
    part_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "PartID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    agency_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "AgencyID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
