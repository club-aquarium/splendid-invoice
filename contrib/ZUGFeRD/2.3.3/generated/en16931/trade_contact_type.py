from dataclasses import dataclass, field
from typing import Optional

from .text_type import TextType
from .universal_communication_type import UniversalCommunicationType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeContactType:
    person_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    department_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "DepartmentName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    telephone_universal_communication: Optional[UniversalCommunicationType] = field(
        default=None,
        metadata={
            "name": "TelephoneUniversalCommunication",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    email_uriuniversal_communication: Optional[UniversalCommunicationType] = field(
        default=None,
        metadata={
            "name": "EmailURIUniversalCommunication",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
