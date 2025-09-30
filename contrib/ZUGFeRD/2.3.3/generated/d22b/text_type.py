from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100"


@dataclass
class TextType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    language_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "languageID",
            "type": "Attribute",
        },
    )
    language_locale_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "languageLocaleID",
            "type": "Attribute",
        },
    )
