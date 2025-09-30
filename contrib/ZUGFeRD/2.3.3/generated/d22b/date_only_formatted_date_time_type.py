from dataclasses import dataclass, field
from typing import Optional

from .date_only_format_code_content_type import DateOnlyFormatCodeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class DateOnlyFormattedDateTimeType:
    date_time_string: Optional["DateOnlyFormattedDateTimeType.DateTimeString"] = field(
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
        format: Optional[DateOnlyFormatCodeContentType] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
