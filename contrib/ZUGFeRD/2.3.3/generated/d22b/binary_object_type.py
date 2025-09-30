from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100"


@dataclass
class BinaryObjectType:
    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        },
    )
    encoding_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "encodingCode",
            "type": "Attribute",
        },
    )
    character_set_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "characterSetCode",
            "type": "Attribute",
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
