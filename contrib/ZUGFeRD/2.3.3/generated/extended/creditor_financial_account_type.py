from dataclasses import dataclass, field
from typing import Optional

from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class CreditorFinancialAccountType:
    ibanid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "IBANID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    account_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    proprietary_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ProprietaryID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
