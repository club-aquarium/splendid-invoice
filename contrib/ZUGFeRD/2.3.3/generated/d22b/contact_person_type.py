from dataclasses import dataclass, field
from typing import Optional

from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ContactPersonType:
    """
    Contact Person.

    :ivar given_name: Given Name
    :ivar middle_name: Middle Name
    :ivar family_name: Family Name
    """

    given_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    middle_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    family_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FamilyName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
