from dataclasses import dataclass, field
from typing import Optional

from .financial_institution_address_type import FinancialInstitutionAddressType
from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class BranchFinancialInstitutionType:
    """
    Branch Financial Institution.

    :ivar id: Sort Code
    :ivar name: Name
    :ivar location_financial_institution_address: Address
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
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
    location_financial_institution_address: Optional[
        FinancialInstitutionAddressType
    ] = field(
        default=None,
        metadata={
            "name": "LocationFinancialInstitutionAddress",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
