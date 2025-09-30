from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype
from .registered_tax_type import RegisteredTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TaxRegistrationType:
    """
    Tax Registration.

    :ivar id: ID
    :ivar iossid: IOSS ID
    :ivar associated_registered_tax: Registered Tax
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    iossid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "IOSSID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    associated_registered_tax: Optional[RegisteredTaxType] = field(
        default=None,
        metadata={
            "name": "AssociatedRegisteredTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
