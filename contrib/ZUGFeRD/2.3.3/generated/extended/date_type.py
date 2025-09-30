from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100"


@dataclass
class DateType:
    date_string: Optional["DateType.DateString"] = field(
        default=None,
        metadata={
            "name": "DateString",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100",
            "required": True,
        },
    )

    @dataclass
    class DateString:
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
