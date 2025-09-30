from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .legal_registration_type import LegalRegistrationType
from .text_type import TextType
from .trade_address_type import TradeAddressType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LegalOrganizationType:
    """
    Legal Organization.

    :ivar legal_classification_code: Legal Classification Code
    :ivar name: Name
    :ivar id: ID
    :ivar trading_business_name: Trading Name
    :ivar postal_trade_address: Postal Address
    :ivar authorized_legal_registration: Authorized Registration
    """

    legal_classification_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "LegalClassificationCode",
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
    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    trading_business_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "TradingBusinessName",
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
    authorized_legal_registration: list[LegalRegistrationType] = field(
        default_factory=list,
        metadata={
            "name": "AuthorizedLegalRegistration",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
