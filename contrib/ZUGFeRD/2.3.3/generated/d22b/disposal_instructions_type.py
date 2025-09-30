from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class DisposalInstructionsType:
    """
    Disposal Instructions.

    :ivar material_id: Material ID
    :ivar recycling_description_code: Recycling Description Code
    :ivar description: Description
    :ivar recycling_procedure: Recycling Procedure Text
    """

    material_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "MaterialID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    recycling_description_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "RecyclingDescriptionCode",
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
    recycling_procedure: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "RecyclingProcedure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
