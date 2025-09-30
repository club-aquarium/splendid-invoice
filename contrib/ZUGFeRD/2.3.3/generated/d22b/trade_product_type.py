from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .formatted_date_time_type import FormattedDateTimeType
from .idtype import Idtype
from .indicator_type import IndicatorType
from .material_goods_characteristic_type import MaterialGoodsCharacteristicType
from .measure_type import MeasureType
from .note_type import NoteType
from .product_characteristic_type import ProductCharacteristicType
from .product_classification_type import ProductClassificationType
from .quantity_type import QuantityType
from .referenced_document_type import ReferencedDocumentType
from .referenced_product_type import ReferencedProductType
from .spatial_dimension_type import SpatialDimensionType
from .specified_binary_file_type import SpecifiedBinaryFileType
from .text_type import TextType
from .trade_country_type import TradeCountryType
from .trade_party_type import TradePartyType
from .trade_product_instance_type import TradeProductInstanceType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TradeProductType:
    """
    Trade Product.

    :ivar id: ID
    :ivar global_id: Global ID
    :ivar seller_assigned_id: Seller Assigned ID
    :ivar buyer_assigned_id: Buyer Assigned ID
    :ivar manufacturer_assigned_id: Manufacturer Assigned ID
    :ivar industry_assigned_id: Industry Assigned ID
    :ivar model_id: Model ID
    :ivar name: Name
    :ivar trade_name: Trade Name
    :ivar description: Description
    :ivar type_code: Type Code
    :ivar net_weight_measure: Net Weight
    :ivar gross_weight_measure: Gross Weight
    :ivar status_code: Status Code
    :ivar product_group_id: Product Group ID
    :ivar net_volume_measure: Net Volume
    :ivar gross_volume_measure: Gross Volume
    :ivar end_item_type_code: End Item Type Code
    :ivar end_item_name: End Item Name
    :ivar customer_assigned_id: Customer Assigned ID
    :ivar batch_id: Batch ID
    :ivar area_density_measure: Area Density Measure
    :ivar use_description: Use Description
    :ivar concise_description: Concise Description
    :ivar additional_description: Additional Description
    :ivar brand_name: Brand Name
    :ivar sub_brand_name: Sub-Brand Name
    :ivar drained_net_weight_measure: Drained Net Weight
    :ivar variable_measure_indicator: Variable Measure Indicator
    :ivar configurable_indicator: Configurable Indicator
    :ivar colour_code: Colour Code
    :ivar colour_description: Colour Description
    :ivar recycling_type_code: Recycling Type Code
    :ivar unit_type_code: Unit Type Code
    :ivar content_unit_quantity: Content Unit Quantity
    :ivar common_name: Common Name
    :ivar model_name: Model Name
    :ivar designation: Designation Text
    :ivar formatted_cancellation_announced_launch_date_time: Announced
        Launch Cancellation Formatted Date Time
    :ivar formatted_latest_product_data_change_date_time: Latest Product
        Data Change Formatted Date Time
    :ivar export_indicator: Export Indicator
    :ivar ultimate_customer_assigned_extension_id: Ultimate Customer
        Assigned Extension ID
    :ivar size_code: Size Code
    :ivar applicable_product_characteristic: Characteristic
    :ivar applicable_material_goods_characteristic: Material Goods
        Characteristic
    :ivar designated_product_classification: Classification
    :ivar individual_trade_product_instance: Individual Product Instance
    :ivar certification_evidence_reference_referenced_document:
        Certification Evidence Document
    :ivar inspection_reference_referenced_document: Inspection Document
    :ivar origin_trade_country: Origin Country
    :ivar linear_spatial_dimension: Dimensions
    :ivar minimum_linear_spatial_dimension: Minimum Dimensions
    :ivar maximum_linear_spatial_dimension: Maximum Dimensions
    :ivar manufacturer_trade_party: Manufacturer
    :ivar presentation_specified_binary_file: Presentation Binary File
    :ivar msdsreference_referenced_document: MSDS Document
    :ivar additional_reference_referenced_document: Additional Document
    :ivar legal_rights_owner_trade_party: Legal Rights Owner
    :ivar brand_owner_trade_party: Brand Owner
    :ivar included_referenced_product: Included Product
    :ivar information_note: Information Note
    :ivar buyer_supplied_parts_reference_referenced_document: Buyer
        Supplied Parts Reference Document
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    global_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "GlobalID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    seller_assigned_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SellerAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_assigned_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "BuyerAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    manufacturer_assigned_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ManufacturerAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    industry_assigned_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "IndustryAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    model_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ModelID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    trade_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "TradeName",
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
    type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    net_weight_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    gross_weight_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    status_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    product_group_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "ProductGroupID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    net_volume_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    gross_volume_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    end_item_type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "EndItemTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    end_item_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "EndItemName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    customer_assigned_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAssignedID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    batch_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "BatchID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    area_density_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "AreaDensityMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    use_description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "UseDescription",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    concise_description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "ConciseDescription",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalDescription",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    brand_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "BrandName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sub_brand_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "SubBrandName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    drained_net_weight_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "DrainedNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    variable_measure_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "VariableMeasureIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    configurable_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "ConfigurableIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    colour_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ColourCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    colour_description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "ColourDescription",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    recycling_type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "RecyclingTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    unit_type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "UnitTypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    content_unit_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "ContentUnitQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    common_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CommonName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    model_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ModelName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    designation: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Designation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    formatted_cancellation_announced_launch_date_time: Optional[
        FormattedDateTimeType
    ] = field(
        default=None,
        metadata={
            "name": "FormattedCancellationAnnouncedLaunchDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    formatted_latest_product_data_change_date_time: Optional[FormattedDateTimeType] = (
        field(
            default=None,
            metadata={
                "name": "FormattedLatestProductDataChangeDateTime",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    export_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "ExportIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    ultimate_customer_assigned_extension_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "UltimateCustomerAssignedExtensionID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    size_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "SizeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_product_characteristic: list[ProductCharacteristicType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableProductCharacteristic",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_material_goods_characteristic: list[MaterialGoodsCharacteristicType] = (
        field(
            default_factory=list,
            metadata={
                "name": "ApplicableMaterialGoodsCharacteristic",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
    designated_product_classification: list[ProductClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "DesignatedProductClassification",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    individual_trade_product_instance: list[TradeProductInstanceType] = field(
        default_factory=list,
        metadata={
            "name": "IndividualTradeProductInstance",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    certification_evidence_reference_referenced_document: list[
        ReferencedDocumentType
    ] = field(
        default_factory=list,
        metadata={
            "name": "CertificationEvidenceReferenceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    inspection_reference_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "InspectionReferenceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    origin_trade_country: Optional[TradeCountryType] = field(
        default=None,
        metadata={
            "name": "OriginTradeCountry",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    linear_spatial_dimension: list[SpatialDimensionType] = field(
        default_factory=list,
        metadata={
            "name": "LinearSpatialDimension",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    minimum_linear_spatial_dimension: Optional[SpatialDimensionType] = field(
        default=None,
        metadata={
            "name": "MinimumLinearSpatialDimension",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    maximum_linear_spatial_dimension: Optional[SpatialDimensionType] = field(
        default=None,
        metadata={
            "name": "MaximumLinearSpatialDimension",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    manufacturer_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "ManufacturerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    presentation_specified_binary_file: list[SpecifiedBinaryFileType] = field(
        default_factory=list,
        metadata={
            "name": "PresentationSpecifiedBinaryFile",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    msdsreference_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "MSDSReferenceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_reference_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalReferenceReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    legal_rights_owner_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "LegalRightsOwnerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    brand_owner_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "BrandOwnerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    included_referenced_product: list[ReferencedProductType] = field(
        default_factory=list,
        metadata={
            "name": "IncludedReferencedProduct",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    information_note: list[NoteType] = field(
        default_factory=list,
        metadata={
            "name": "InformationNote",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_supplied_parts_reference_referenced_document: list[ReferencedDocumentType] = (
        field(
            default_factory=list,
            metadata={
                "name": "BuyerSuppliedPartsReferenceReferencedDocument",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
