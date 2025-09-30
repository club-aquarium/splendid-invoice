from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .legal_organization_type import LegalOrganizationType
from .logistics_location_type import LogisticsLocationType
from .party_role_code_type import PartyRoleCodeType
from .specified_binary_file_type import SpecifiedBinaryFileType
from .tax_registration_type import TaxRegistrationType
from .text_type import TextType
from .trade_address_type import TradeAddressType
from .trade_contact_type import TradeContactType
from .universal_communication_type import UniversalCommunicationType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradePartyType:
    """
    Trade Party.

    :ivar id: ID
    :ivar global_id: Global ID
    :ivar type_code: Type Code
    :ivar name: Name
    :ivar role_code: Role Code
    :ivar description: Description
    :ivar registered_id: Registered ID
    :ivar role: Role Text
    :ivar specified_legal_organization: Legal Organization
    :ivar defined_trade_contact: Defined Contact Details
    :ivar postal_trade_address: Postal Address
    :ivar uriuniversal_communication: URI
    :ivar specified_logistics_location: Logistics Location
    :ivar specified_tax_registration: Tax Registration
    :ivar end_point_uriuniversal_communication: End Point URI
    :ivar logo_associated_specified_binary_file: Logo Binary File
    """

    id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    global_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "GlobalID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    role_code: list[PartyRoleCodeType] = field(
        default_factory=list,
        metadata={
            "name": "RoleCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    registered_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    role: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_legal_organization: Optional[LegalOrganizationType] = field(
        default=None,
        metadata={
            "name": "SpecifiedLegalOrganization",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    defined_trade_contact: list[TradeContactType] = field(
        default_factory=list,
        metadata={
            "name": "DefinedTradeContact",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    postal_trade_address: Optional[TradeAddressType] = field(
        default=None,
        metadata={
            "name": "PostalTradeAddress",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    uriuniversal_communication: list[UniversalCommunicationType] = field(
        default_factory=list,
        metadata={
            "name": "URIUniversalCommunication",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_logistics_location: list[LogisticsLocationType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedLogisticsLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_tax_registration: list[TaxRegistrationType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedTaxRegistration",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    end_point_uriuniversal_communication: Optional[UniversalCommunicationType] = field(
        default=None,
        metadata={
            "name": "EndPointURIUniversalCommunication",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    logo_associated_specified_binary_file: list[SpecifiedBinaryFileType] = field(
        default_factory=list,
        metadata={
            "name": "LogoAssociatedSpecifiedBinaryFile",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
