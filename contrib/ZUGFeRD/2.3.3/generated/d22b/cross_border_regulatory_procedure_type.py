from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .code_type import CodeType
from .text_type import TextType
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class CrossBorderRegulatoryProcedureType:
    """
    Cross-Border Regulatory Procedure.

    :ivar type_code: Type Code
    :ivar transaction_nature_code: Transaction Nature Code
    :ivar tariff_amount: Tariff Amount
    :ivar non_tariff_charge_amount: Non-Tariff Charge Amount
    :ivar total_charge_amount: Total Charge Amount
    :ivar remark: Remark
    :ivar applicable_trade_tax: Trade Tax
    """

    type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    transaction_nature_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TransactionNatureCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    tariff_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "TariffAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    non_tariff_charge_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "NonTariffChargeAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_charge_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "TotalChargeAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    remark: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_trade_tax: list[TradeTaxType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
