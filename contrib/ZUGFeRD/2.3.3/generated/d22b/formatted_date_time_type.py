from dataclasses import dataclass, field
from typing import Optional

from .time_point_format_code_content_type import TimePointFormatCodeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class FormattedDateTimeType:
    date_time_string: Optional["FormattedDateTimeType.DateTimeString"] = field(
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
        format: Optional[TimePointFormatCodeContentType] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
