from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100"


@dataclass
class MeasureType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
    unit_code_list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListVersionID",
            "type": "Attribute",
        },
    )
