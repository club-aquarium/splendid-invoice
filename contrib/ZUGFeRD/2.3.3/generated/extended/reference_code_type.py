from dataclasses import dataclass, field

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class ReferenceCodeType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
