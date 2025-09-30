from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .text_type import TextType
from .trade_party_type import TradePartyType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TransportCargoInsuranceType:
    """
    Transport Cargo Insurance.

    :ivar coverage_code: Coverage Code
    :ivar coverage_description: Coverage Description
    :ivar contract_general_conditions: Contract General Conditions Text
    :ivar coverage_trade_party: Coverage Party
    """

    coverage_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CoverageCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    coverage_description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CoverageDescription",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    contract_general_conditions: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ContractGeneralConditions",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    coverage_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "CoverageTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
