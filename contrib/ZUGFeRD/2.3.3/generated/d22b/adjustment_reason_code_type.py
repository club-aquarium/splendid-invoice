from dataclasses import dataclass, field
from typing import Optional

from .adjustment_reason_code_list_agency_idcontent_type import (
    AdjustmentReasonCodeListAgencyIdcontentType,
)
from .adjustment_reason_description_code_content_type import (
    AdjustmentReasonDescriptionCodeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class AdjustmentReasonCodeType:
    value: Optional[AdjustmentReasonDescriptionCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: AdjustmentReasonCodeListAgencyIdcontentType = field(
        init=False,
        default=AdjustmentReasonCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
