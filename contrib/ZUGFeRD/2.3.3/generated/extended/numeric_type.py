from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100"


@dataclass
class NumericType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
