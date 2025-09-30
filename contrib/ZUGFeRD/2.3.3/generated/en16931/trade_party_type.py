from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype
from .legal_organization_type import LegalOrganizationType
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
    name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
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
    defined_trade_contact: Optional[TradeContactType] = field(
        default=None,
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
    uriuniversal_communication: Optional[UniversalCommunicationType] = field(
        default=None,
        metadata={
            "name": "URIUniversalCommunication",
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
            "max_occurs": 2,
        },
    )
