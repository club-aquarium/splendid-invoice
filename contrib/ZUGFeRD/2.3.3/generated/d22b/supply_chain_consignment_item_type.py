from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .goods_type_code_type import GoodsTypeCodeType
from .goods_type_extension_code_type import GoodsTypeExtensionCodeType
from .idtype import Idtype
from .note_type import NoteType
from .quantity_type import QuantityType
from .referenced_document_type import ReferencedDocumentType
from .transport_cargo_type import TransportCargoType
from .transport_dangerous_goods_type import TransportDangerousGoodsType
from .weight_unit_measure_type import WeightUnitMeasureType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainConsignmentItemType:
    """
    Supply Chain Consignment Item.

    :ivar type_code: Goods Type Code
    :ivar type_extension_code: Goods Type Extension Code
    :ivar declared_value_for_customs_amount: Declared Value For Customs
        Amount
    :ivar declared_value_for_statistics_amount: Declared Value For
        Statistics Amount
    :ivar invoice_amount: Invoice Amount
    :ivar gross_weight_measure: Gross Weight
    :ivar net_weight_measure: Net Weight
    :ivar tariff_quantity: Tariff Quantity
    :ivar global_id: Global ID
    :ivar nature_identification_transport_cargo: Cargo Nature
        Identification
    :ivar applicable_transport_dangerous_goods: Transport Dangerous
        Goods
    :ivar previous_administrative_referenced_document: Previous
        Administrative Document
    :ivar applicable_note: Applicable Note
    """

    type_code: Optional[GoodsTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_extension_code: Optional[GoodsTypeExtensionCodeType] = field(
        default=None,
        metadata={
            "name": "TypeExtensionCode",
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
    declared_value_for_statistics_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "DeclaredValueForStatisticsAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoice_amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    gross_weight_measure: Optional[WeightUnitMeasureType] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    net_weight_measure: Optional[WeightUnitMeasureType] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    tariff_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "TariffQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    global_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "GlobalID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    nature_identification_transport_cargo: Optional[TransportCargoType] = field(
        default=None,
        metadata={
            "name": "NatureIdentificationTransportCargo",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_transport_dangerous_goods: list[TransportDangerousGoodsType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableTransportDangerousGoods",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    previous_administrative_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "PreviousAdministrativeReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_note: list[NoteType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableNote",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
