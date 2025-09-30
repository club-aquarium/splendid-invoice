from dataclasses import dataclass, field
from typing import Optional

from .accounting_account_type_code_type import AccountingAccountTypeCodeType
from .accounting_amount_type_code_type import AccountingAmountTypeCodeType
from .accounting_document_code_type import AccountingDocumentCodeType
from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeAccountingAccountType:
    """
    Trade Accounting Account.

    :ivar id: ID
    :ivar set_trigger_code: Set Trigger Code
    :ivar type_code: Type Code
    :ivar amount_type_code: Amount Type Code
    :ivar name: Name
    :ivar cost_reference_dimension_pattern: Cost Reference Dimension
        Pattern Text
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    set_trigger_code: Optional[AccountingDocumentCodeType] = field(
        default=None,
        metadata={
            "name": "SetTriggerCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: Optional[AccountingAccountTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    amount_type_code: Optional[AccountingAmountTypeCodeType] = field(
        default=None,
        metadata={
            "name": "AmountTypeCode",
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
    cost_reference_dimension_pattern: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CostReferenceDimensionPattern",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
