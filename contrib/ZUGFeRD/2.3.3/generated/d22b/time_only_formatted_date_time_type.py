from dataclasses import dataclass, field
from typing import Optional

from .time_only_format_code_content_type import TimeOnlyFormatCodeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TimeOnlyFormattedDateTimeType:
    date_time_string: Optional["TimeOnlyFormattedDateTimeType.DateTimeString"] = field(
        default=None,
        metadata={
            "name": "DateTimeString",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:QualifiedDataType:100",
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
        format: Optional[TimeOnlyFormatCodeContentType] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
