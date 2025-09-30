from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .code_type import CodeType
from .idtype import Idtype
from .specified_period_type import SpecifiedPeriodType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ReturnableAssetInstructionsType:
    """
    Returnable Asset Instructions.

    :ivar material_id: Material ID
    :ivar terms_and_conditions_description: Terms And Conditions Text
    :ivar terms_and_conditions_description_code: Terms And Conditions
        Code
    :ivar deposit_value_specified_amount: Deposit Amount
    :ivar deposit_value_validity_specified_period: Deposit Validity
        Period
    """

    material_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "MaterialID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    terms_and_conditions_description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "TermsAndConditionsDescription",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    terms_and_conditions_description_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TermsAndConditionsDescriptionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    deposit_value_specified_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "DepositValueSpecifiedAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    deposit_value_validity_specified_period: Optional[SpecifiedPeriodType] = field(
        default=None,
        metadata={
            "name": "DepositValueValiditySpecifiedPeriod",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
