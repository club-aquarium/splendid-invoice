from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .charge_paying_party_role_code_type import ChargePayingPartyRoleCodeType
from .code_type import CodeType
from .freight_charge_tariff_class_code_type import (
    FreightChargeTariffClassCodeType,
)
from .freight_charge_type_idtype import FreightChargeTypeIdtype
from .logistics_charge_calculation_basis_code_type import (
    LogisticsChargeCalculationBasisCodeType,
)
from .logistics_location_type import LogisticsLocationType
from .text_type import TextType
from .trade_tax_type import TradeTaxType
from .transport_service_payment_arrangement_code_type import (
    TransportServicePaymentArrangementCodeType,
)

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class LogisticsServiceChargeType:
    """
    Logistics Service Charge.

    :ivar id: ID
    :ivar description: Description
    :ivar payment_arrangement_code: Payment Arrangement Code
    :ivar tariff_class_code: Tariff Class Code
    :ivar charge_category_code: Charge Category Code
    :ivar service_category_code: Service Category Code
    :ivar disbursement_amount: Disbursement Amount
    :ivar applied_amount: Applied Amount
    :ivar allowance_charge: Allowance/Charge Text
    :ivar paying_party_role_code: Paying Party Role Code
    :ivar calculation_basis_code: Calculation Basis Code
    :ivar calculation_basis: Calculation Basis Text
    :ivar transport_payment_method_code: Transport Payment Method Code
    :ivar payment_place_logistics_location: Payment Place
    :ivar applied_from_logistics_location: Applied From Location
    :ivar applied_to_logistics_location: Applied To Location
    :ivar applied_trade_tax: Trade Tax
    """

    id: Optional[FreightChargeTypeIdtype] = field(
        default=None,
        metadata={
            "name": "ID",
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
    payment_arrangement_code: Optional[TransportServicePaymentArrangementCodeType] = (
        field(
            default=None,
            metadata={
                "name": "PaymentArrangementCode",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    tariff_class_code: Optional[FreightChargeTariffClassCodeType] = field(
        default=None,
        metadata={
            "name": "TariffClassCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    charge_category_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ChargeCategoryCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    service_category_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ServiceCategoryCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    disbursement_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "DisbursementAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applied_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "AppliedAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    allowance_charge: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    paying_party_role_code: Optional[ChargePayingPartyRoleCodeType] = field(
        default=None,
        metadata={
            "name": "PayingPartyRoleCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    calculation_basis_code: Optional[LogisticsChargeCalculationBasisCodeType] = field(
        default=None,
        metadata={
            "name": "CalculationBasisCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    calculation_basis: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CalculationBasis",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    transport_payment_method_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TransportPaymentMethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    payment_place_logistics_location: Optional[LogisticsLocationType] = field(
        default=None,
        metadata={
            "name": "PaymentPlaceLogisticsLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applied_from_logistics_location: Optional[LogisticsLocationType] = field(
        default=None,
        metadata={
            "name": "AppliedFromLogisticsLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applied_to_logistics_location: Optional[LogisticsLocationType] = field(
        default=None,
        metadata={
            "name": "AppliedToLogisticsLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applied_trade_tax: list[TradeTaxType] = field(
        default_factory=list,
        metadata={
            "name": "AppliedTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
