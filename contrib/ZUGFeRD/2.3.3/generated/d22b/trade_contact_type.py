from dataclasses import dataclass, field
from typing import Optional

from .contact_person_type import ContactPersonType
from .contact_type_code_type import ContactTypeCodeType
from .idtype import Idtype
from .note_type import NoteType
from .text_type import TextType
from .universal_communication_type import UniversalCommunicationType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeContactType:
    """
    Trade Contact.

    :ivar id: ID
    :ivar person_name: Person Name
    :ivar department_name: Department Name
    :ivar type_code: Type Code
    :ivar job_title: Job Title
    :ivar responsibility: Responsibility Text
    :ivar person_id: Person ID
    :ivar telephone_universal_communication: Telephone
    :ivar direct_telephone_universal_communication: Direct Telephone
    :ivar mobile_telephone_universal_communication: Mobile Telephone
    :ivar fax_universal_communication: Fax
    :ivar email_uriuniversal_communication: Email Address
    :ivar telex_universal_communication: Telex
    :ivar voipuniversal_communication: VOIP
    :ivar instant_messaging_universal_communication: Instant Messaging
    :ivar specified_note: Note
    :ivar specified_contact_person: Person
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
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
    type_code: Optional[ContactTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    job_title: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "JobTitle",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    responsibility: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Responsibility",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    person_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "PersonID",
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
    direct_telephone_universal_communication: Optional[UniversalCommunicationType] = (
        field(
            default=None,
            metadata={
                "name": "DirectTelephoneUniversalCommunication",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    mobile_telephone_universal_communication: Optional[UniversalCommunicationType] = (
        field(
            default=None,
            metadata={
                "name": "MobileTelephoneUniversalCommunication",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    fax_universal_communication: Optional[UniversalCommunicationType] = field(
        default=None,
        metadata={
            "name": "FaxUniversalCommunication",
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
    telex_universal_communication: Optional[UniversalCommunicationType] = field(
        default=None,
        metadata={
            "name": "TelexUniversalCommunication",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    voipuniversal_communication: Optional[UniversalCommunicationType] = field(
        default=None,
        metadata={
            "name": "VOIPUniversalCommunication",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    instant_messaging_universal_communication: Optional[UniversalCommunicationType] = (
        field(
            default=None,
            metadata={
                "name": "InstantMessagingUniversalCommunication",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    specified_note: list[NoteType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedNote",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_contact_person: Optional[ContactPersonType] = field(
        default=None,
        metadata={
            "name": "SpecifiedContactPerson",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
