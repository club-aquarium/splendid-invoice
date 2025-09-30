from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .cross_border_customs_valuation_type import (
    CrossBorderCustomsValuationType,
)
from .cross_border_regulatory_procedure_type import (
    CrossBorderRegulatoryProcedureType,
)
from .idtype import Idtype
from .logistics_location_type import LogisticsLocationType
from .logistics_transport_equipment_type import LogisticsTransportEquipmentType
from .logistics_transport_movement_type import LogisticsTransportMovementType
from .quantity_type import QuantityType
from .referenced_document_type import ReferencedDocumentType
from .supply_chain_consignment_item_type import SupplyChainConsignmentItemType
from .trade_party_type import TradePartyType
from .transport_cargo_insurance_type import TransportCargoInsuranceType
from .volume_unit_measure_type import VolumeUnitMeasureType
from .weight_unit_measure_type import WeightUnitMeasureType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainConsignmentType:
    """
    Supply Chain Consignment.

    :ivar id: ID
    :ivar gross_weight_measure: Gross Weight
    :ivar net_weight_measure: Net Weight
    :ivar gross_volume_measure: Gross Volume
    :ivar chargeable_weight_measure: Chargeable Weight
    :ivar insurance_premium_amount: Insurance Premium Amount
    :ivar associated_invoice_amount: Associated Invoice Amount
    :ivar total_charge_amount: Total Charge Amount
    :ivar declared_value_for_customs_amount: Declared Value For Customs
        Amount
    :ivar package_quantity: Number Of Packages
    :ivar net_volume_measure: Net Volume Measure
    :ivar consignor_trade_party: Consignor
    :ivar consignee_trade_party: Consignee
    :ivar carrier_trade_party: Carrier
    :ivar freight_forwarder_trade_party: Freight Forwarder
    :ivar delivery_trade_party: Delivery Party
    :ivar customs_import_agent_trade_party: Customs Import Agent
    :ivar customs_export_agent_trade_party: Customs Export Agent
    :ivar grouping_centre_trade_party: Grouping Centre
    :ivar transit_logistics_location: Transit Location
    :ivar transport_contract_referenced_document: Transport Contract
        Document
    :ivar associated_referenced_document: Associated Document
    :ivar included_supply_chain_consignment_item: Included Consignment
        Item
    :ivar utilized_logistics_transport_equipment: Used Transport
        Equipment
    :ivar specified_logistics_transport_movement: Specified Transport
        Movement
    :ivar applicable_transport_cargo_insurance: Cargo Insurance
    :ivar applicable_cross_border_regulatory_procedure: Regulatory
        Procedure
    :ivar applicable_cross_border_customs_valuation: Customs Valuation
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    gross_weight_measure: list[WeightUnitMeasureType] = field(
        default_factory=list,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    net_weight_measure: list[WeightUnitMeasureType] = field(
        default_factory=list,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    gross_volume_measure: list[VolumeUnitMeasureType] = field(
        default_factory=list,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    chargeable_weight_measure: Optional[WeightUnitMeasureType] = field(
        default=None,
        metadata={
            "name": "ChargeableWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    insurance_premium_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "InsurancePremiumAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    associated_invoice_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedInvoiceAmount",
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
    declared_value_for_customs_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "DeclaredValueForCustomsAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    package_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "PackageQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    net_volume_measure: list[VolumeUnitMeasureType] = field(
        default_factory=list,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    consignor_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "ConsignorTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    consignee_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "ConsigneeTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    carrier_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "CarrierTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    freight_forwarder_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "FreightForwarderTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    delivery_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "DeliveryTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    customs_import_agent_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "CustomsImportAgentTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    customs_export_agent_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "CustomsExportAgentTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    grouping_centre_trade_party: list[TradePartyType] = field(
        default_factory=list,
        metadata={
            "name": "GroupingCentreTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    transit_logistics_location: list[LogisticsLocationType] = field(
        default_factory=list,
        metadata={
            "name": "TransitLogisticsLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    transport_contract_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "TransportContractReferencedDocument",
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
    included_supply_chain_consignment_item: list[SupplyChainConsignmentItemType] = (
        field(
            default_factory=list,
            metadata={
                "name": "IncludedSupplyChainConsignmentItem",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    utilized_logistics_transport_equipment: list[LogisticsTransportEquipmentType] = (
        field(
            default_factory=list,
            metadata={
                "name": "UtilizedLogisticsTransportEquipment",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    specified_logistics_transport_movement: list[LogisticsTransportMovementType] = (
        field(
            default_factory=list,
            metadata={
                "name": "SpecifiedLogisticsTransportMovement",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    applicable_transport_cargo_insurance: Optional[TransportCargoInsuranceType] = field(
        default=None,
        metadata={
            "name": "ApplicableTransportCargoInsurance",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_cross_border_regulatory_procedure: list[
        CrossBorderRegulatoryProcedureType
    ] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableCrossBorderRegulatoryProcedure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_cross_border_customs_valuation: list[CrossBorderCustomsValuationType] = (
        field(
            default_factory=list,
            metadata={
                "name": "ApplicableCrossBorderCustomsValuation",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
