from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ProductClassificationType:
    class_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
