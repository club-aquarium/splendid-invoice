from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType
from .dangerous_goods_packaging_level_code_type import (
    DangerousGoodsPackagingLevelCodeType,
)
from .dangerous_goods_regulation_code_type import (
    DangerousGoodsRegulationCodeType,
)
from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class TransportDangerousGoodsType:
    """
    Transport Dangerous Goods.

    :ivar undgidentification_code: UNDG ID
    :ivar regulation_code: Regulation Code
    :ivar regulation_name: Regulation Name
    :ivar technical_name: Technical Name
    :ivar emsid: EMS ID
    :ivar packaging_danger_level_code: Packaging Danger Level Code
    :ivar hazard_classification_id: Hazard Classification ID
    :ivar additional_hazard_classification_id: Additional Hazard
        Classification ID
    :ivar proper_shipping_name: Proper Shipping Name
    """

    undgidentification_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "UNDGIdentificationCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    regulation_code: Optional[DangerousGoodsRegulationCodeType] = field(
        default=None,
        metadata={
            "name": "RegulationCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    regulation_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "RegulationName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    technical_name: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "TechnicalName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    emsid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "EMSID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    packaging_danger_level_code: Optional[DangerousGoodsPackagingLevelCodeType] = field(
        default=None,
        metadata={
            "name": "PackagingDangerLevelCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    hazard_classification_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "HazardClassificationID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_hazard_classification_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "AdditionalHazardClassificationID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    proper_shipping_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ProperShippingName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
