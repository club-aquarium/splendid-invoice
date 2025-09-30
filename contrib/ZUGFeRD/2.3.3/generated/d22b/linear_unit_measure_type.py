from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .measurement_unit_common_code_linear_content_type import (
    MeasurementUnitCommonCodeLinearContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class LinearUnitMeasureType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit_code: Optional[MeasurementUnitCommonCodeLinearContentType] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
