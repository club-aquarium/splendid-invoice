from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .measurement_unit_common_code_weight_content_type import (
    MeasurementUnitCommonCodeWeightContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class WeightUnitMeasureType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit_code: Optional[MeasurementUnitCommonCodeWeightContentType] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
