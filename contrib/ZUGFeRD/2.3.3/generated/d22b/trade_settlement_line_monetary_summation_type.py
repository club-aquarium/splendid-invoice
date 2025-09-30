from dataclasses import dataclass, field

from .amount_type import AmountType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeSettlementLineMonetarySummationType:
    """
    Trade Settlement Line Monetary Summation.

    :ivar line_total_amount: Line Total Amount
    :ivar charge_total_amount: Charge Total Amount
    :ivar allowance_total_amount: Allowance Total Amount
    :ivar tax_basis_total_amount: Tax Basis Total Amount
    :ivar tax_total_amount: Tax Total Amount
    :ivar grand_total_amount: Grand Total Amount
    :ivar information_amount: Information Amount
    :ivar total_allowance_charge_amount: Total Allowance/Charge Amount
    :ivar total_retail_value_information_amount: Total Retail Value
        Information Amount
    :ivar gross_line_total_amount: Gross Line Total Amount
    :ivar net_line_total_amount: Net Line Total Amount
    :ivar net_including_taxes_line_total_amount: Net Including Taxes
        Line Total Amount
    :ivar product_weight_loss_information_amount: Product Weight Loss
        Information Amount
    :ivar including_taxes_line_total_amount: Line Total Amount Including
        Taxes
    """

    line_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "LineTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    charge_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "ChargeTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    allowance_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    tax_basis_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "TaxBasisTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    tax_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    grand_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "GrandTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    information_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "InformationAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_allowance_charge_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "TotalAllowanceChargeAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_retail_value_information_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "TotalRetailValueInformationAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    gross_line_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "GrossLineTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    net_line_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "NetLineTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    net_including_taxes_line_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "NetIncludingTaxesLineTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    product_weight_loss_information_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "ProductWeightLossInformationAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    including_taxes_line_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "IncludingTaxesLineTotalAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
