from dataclasses import dataclass, field

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100"


@dataclass
class TextType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
