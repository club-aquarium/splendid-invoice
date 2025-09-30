from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .seal_condition_code_type import SealConditionCodeType
from .sealing_party_role_code_type import SealingPartyRoleCodeType
from .trade_party_type import TradePartyType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LogisticsSealType:
    """
    Logistics Seal.

    :ivar id: ID
    :ivar maximum_id: Maximum ID
    :ivar type_code: Type Code
    :ivar condition_code: Condition Code
    :ivar sealing_party_role_code: Sealing Party Role Code
    :ivar issuing_trade_party: Issuing Party
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    maximum_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "MaximumID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    condition_code: list[SealConditionCodeType] = field(
        default_factory=list,
        metadata={
            "name": "ConditionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sealing_party_role_code: Optional[SealingPartyRoleCodeType] = field(
        default=None,
        metadata={
            "name": "SealingPartyRoleCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    issuing_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "IssuingTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
