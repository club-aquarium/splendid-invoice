from dataclasses import dataclass, field

from .amount_type import AmountType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeSettlementHeaderMonetarySummationType:
    """
    Trade Settlement Header Monetary Summation.

    :ivar line_total_amount: Line Total Amount
    :ivar charge_total_amount: Charge Total Amount
    :ivar allowance_total_amount: Allowance Total Amount
    :ivar tax_basis_total_amount: Tax Basis Total Amount
    :ivar tax_total_amount: Tax Total Amount
    :ivar rounding_amount: Rounding Amount
    :ivar grand_total_amount: Grand Total Amount
    :ivar information_amount: Information Amount
    :ivar total_prepaid_amount: Total Prepaid Amount
    :ivar total_discount_amount: Total Discount Amount
    :ivar total_allowance_charge_amount: Total Allowance/Charge Amount
    :ivar due_payable_amount: Due Payable Amount
    :ivar retail_value_excluding_tax_information_amount: Retail Value
        Excluding Tax Information Amount
    :ivar total_deposit_fee_information_amount: Total Deposit Fee
        Information Amount
    :ivar product_value_excluding_tobacco_tax_information_amount:
        Product Value Excluding Tobacco Tax Information Amount
    :ivar total_retail_value_information_amount: Total Retail Value
        Information Amount
    :ivar gross_line_total_amount: Gross Line Total Amount
    :ivar net_line_total_amount: Net Line Total Amount
    :ivar net_including_taxes_line_total_amount: Net Including Taxes
        Line Total Amount
    :ivar insurance_charge_total_amount: Insurance Charge Total Amount
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
    rounding_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "RoundingAmount",
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
    total_prepaid_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "TotalPrepaidAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_discount_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "TotalDiscountAmount",
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
    due_payable_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "DuePayableAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    retail_value_excluding_tax_information_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "RetailValueExcludingTaxInformationAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_deposit_fee_information_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "TotalDepositFeeInformationAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    product_value_excluding_tobacco_tax_information_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "ProductValueExcludingTobaccoTaxInformationAmount",
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
    insurance_charge_total_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "InsuranceChargeTotalAmount",
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
