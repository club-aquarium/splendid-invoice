from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100"


@dataclass
class IndicatorType:
    indicator_string: Optional["IndicatorType.IndicatorString"] = field(
        default=None,
        metadata={
            "name": "IndicatorString",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100",
        },
    )
    indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100",
        },
    )

    @dataclass
    class IndicatorString:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        format: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
