from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .disposal_instructions_type import DisposalInstructionsType
from .indicator_type import IndicatorType
from .material_goods_characteristic_type import MaterialGoodsCharacteristicType
from .measure_type import MeasureType
from .package_type_code_type import PackageTypeCodeType
from .packaging_marking_type import PackagingMarkingType
from .quantity_type import QuantityType
from .returnable_asset_instructions_type import ReturnableAssetInstructionsType
from .spatial_dimension_type import SpatialDimensionType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class SupplyChainPackagingType:
    """
    Supply Chain Packaging.

    :ivar type_code: Type Code
    :ivar type_value: Type Text
    :ivar description: Description
    :ivar condition_code: Condition Code
    :ivar disposal_method_code: Disposal Method Code
    :ivar weight_measure: Weight
    :ivar maximum_stackability_quantity: Maximum Stackability Quantity
    :ivar maximum_stackability_weight_measure: Maximum Stackability
        Weight
    :ivar customer_facing_total_unit_quantity: Customer Facing Total
        Unit Quantity
    :ivar layer_total_unit_quantity: Layer Total Unit Quantity
    :ivar content_layer_quantity: Content Layer Quantity
    :ivar additional_instruction_code: Additional Instruction Code
    :ivar additional_instruction_indicator: Additional Instruction
        Indicator
    :ivar linear_spatial_dimension: Dimensions
    :ivar minimum_linear_spatial_dimension: Minimum Dimensions
    :ivar maximum_linear_spatial_dimension: Maximum Dimensions
    :ivar specified_packaging_marking: Marking
    :ivar applicable_material_goods_characteristic: Goods Characteristic
    :ivar applicable_disposal_instructions: Disposal Instructions
    :ivar applicable_returnable_asset_instructions: Returnable Asset
        Instructions
    """

    type_code: Optional[PackageTypeCodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_value: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Type",
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
    condition_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ConditionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    disposal_method_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "DisposalMethodCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    weight_measure: list[MeasureType] = field(
        default_factory=list,
        metadata={
            "name": "WeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    maximum_stackability_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "MaximumStackabilityQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    maximum_stackability_weight_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "MaximumStackabilityWeightMeasure",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    customer_facing_total_unit_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "CustomerFacingTotalUnitQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    layer_total_unit_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "LayerTotalUnitQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    content_layer_quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "ContentLayerQuantity",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_instruction_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInstructionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_instruction_indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "AdditionalInstructionIndicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    linear_spatial_dimension: Optional[SpatialDimensionType] = field(
        default=None,
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
    specified_packaging_marking: list[PackagingMarkingType] = field(
        default_factory=list,
        metadata={
            "name": "SpecifiedPackagingMarking",
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
    applicable_disposal_instructions: list[DisposalInstructionsType] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableDisposalInstructions",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_returnable_asset_instructions: list[ReturnableAssetInstructionsType] = (
        field(
            default_factory=list,
            metadata={
                "name": "ApplicableReturnableAssetInstructions",
                "type": "Element",
                "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            },
        )
    )
