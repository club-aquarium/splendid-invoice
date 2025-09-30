from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .measurement_unit_common_code_volume_content_type import (
    MeasurementUnitCommonCodeVolumeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class VolumeUnitMeasureType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit_code: Optional[MeasurementUnitCommonCodeVolumeContentType] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
