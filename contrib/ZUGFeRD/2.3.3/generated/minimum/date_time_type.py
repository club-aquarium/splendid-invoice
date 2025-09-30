from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100"


@dataclass
class DateTimeType:
    date_time_string: Optional["DateTimeType.DateTimeString"] = field(
        default=None,
        metadata={
            "name": "DateTimeString",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100",
            "required": True,
        },
    )

    @dataclass
    class DateTimeString:
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
                "required": True,
            },
        )
