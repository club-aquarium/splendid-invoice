from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .date_time_type import DateTimeType
from .numeric_type import NumericType
from .price_type_code_type import PriceTypeCodeType
from .quantity_type import QuantityType
from .reference_price_type import ReferencePriceType
from .referenced_document_type import ReferencedDocumentType
from .specified_period_type import SpecifiedPeriodType
from .text_type import TextType
from .trade_allowance_charge_type import TradeAllowanceChargeType
from .trade_location_type import TradeLocationType
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradePriceType:
    """
    Trade Price.

    :ivar type_code: Type Code
    :ivar charge_amount: Charge Amount
    :ivar basis_quantity: Basis Quantity
    :ivar minimum_quantity: Minimum Quantity
    :ivar maximum_quantity: Maximum Quantity
    :ivar change_reason: Change Reason Text
    :ivar order_unit_conversion_factor_numeric: Order Unit Conversion
        Factor
    :ivar type_value: Type Text
    :ivar basis_date_time: Basis Date Time
    :ivar applied_trade_allowance_charge: Applied Allowance/Charge
    :ivar validity_specified_period: Validity Period
    :ivar included_trade_tax: Included Tax
    :ivar delivery_trade_location: Delivery Location
    :ivar trade_comparison_reference_price: Trade Comparison Price
    :ivar associated_referenced_document: Associated Document
    """

    type_code: Optional[PriceTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    charge_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "ChargeAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "min_occurs": 1,
        },
    )
    basis_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "BasisQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    minimum_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    maximum_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    change_reason: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "ChangeReason",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    order_unit_conversion_factor_numeric: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "OrderUnitConversionFactorNumeric",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_value: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    basis_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "BasisDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applied_trade_allowance_charge: list[TradeAllowanceChargeType] = field(
        default_factory=list,
        metadata={
            "name": "AppliedTradeAllowanceCharge",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    validity_specified_period: Optional[SpecifiedPeriodType] = field(
        default=None,
        metadata={
            "name": "ValiditySpecifiedPeriod",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    included_trade_tax: list[TradeTaxType] = field(
        default_factory=list,
        metadata={
            "name": "IncludedTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    delivery_trade_location: list[TradeLocationType] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryTradeLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    trade_comparison_reference_price: list[ReferencePriceType] = field(
        default_factory=list,
        metadata={
            "name": "TradeComparisonReferencePrice",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    associated_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
