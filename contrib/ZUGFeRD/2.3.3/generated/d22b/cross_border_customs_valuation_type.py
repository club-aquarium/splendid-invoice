from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .code_type import CodeType
from .indicator_type import IndicatorType
from .percent_type import PercentType
from .text_type import TextType
from .trade_currency_exchange_type import TradeCurrencyExchangeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class CrossBorderCustomsValuationType:
    """
    Cross-Border Customs Valuation.

    :ivar added_adjustment_amount: Added Adjustment Amount
    :ivar deducted_adjustment_amount: Deducted Adjustment Amount
    :ivar added_adjustment_percent: Added Adjustment Percent
    :ivar deducted_adjustment_percent: Deducted Adjustment Percent
    :ivar method_code: Method Code
    :ivar wtoaddition_code: WTO Addition Code
    :ivar charge_apportion_method_code: Charge Apportion Method Code
    :ivar other_charge_amount: Other Charge Amount
    :ivar buyer_seller_relationship_indicator: Buyer Seller Relationship
        Indicator
    :ivar buyer_seller_relationship_price_influence_indicator: Buyer
        Seller Relationship Price Influence Indicator
    :ivar sale_restriction_indicator: Sale Restriction Indicator
    :ivar sale_price_condition_indicator: Sale Price Condition Indicator
    :ivar royalty_license_fee_indicator: Royalty Licence Fee Indicator
    :ivar type_code: Type Code
    :ivar sale_restriction: Sale Restriction Text
    :ivar applicable_trade_currency_exchange: Applicable Currency
        Exchange
    """

    added_adjustment_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "AddedAdjustmentAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    deducted_adjustment_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "DeductedAdjustmentAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    added_adjustment_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "AddedAdjustmentPercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    deducted_adjustment_percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "DeductedAdjustmentPercent",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    method_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "MethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    wtoaddition_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "WTOAdditionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    charge_apportion_method_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ChargeApportionMethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    other_charge_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "OtherChargeAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_seller_relationship_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "BuyerSellerRelationshipIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_seller_relationship_price_influence_indicator: Optional[IndicatorType] = (
        field(
            default=None,
            metadata={
                "name": "BuyerSellerRelationshipPriceInfluenceIndicator",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    sale_restriction_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "SaleRestrictionIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sale_price_condition_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "SalePriceConditionIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    royalty_license_fee_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "RoyaltyLicenseFeeIndicator",
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
    sale_restriction: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "SaleRestriction",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_trade_currency_exchange: Optional[TradeCurrencyExchangeType] = field(
        default=None,
        metadata={
            "name": "ApplicableTradeCurrencyExchange",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
