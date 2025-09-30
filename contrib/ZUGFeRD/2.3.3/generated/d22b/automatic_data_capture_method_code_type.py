from dataclasses import dataclass, field
from typing import Optional

from .automatic_data_capture_method_code_content_type import (
    AutomaticDataCaptureMethodCodeContentType,
)
from .automatic_data_capture_method_code_list_agency_idcontent_type import (
    AutomaticDataCaptureMethodCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class AutomaticDataCaptureMethodCodeType:
    value: Optional[AutomaticDataCaptureMethodCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: AutomaticDataCaptureMethodCodeListAgencyIdcontentType = field(
        init=False,
        default=AutomaticDataCaptureMethodCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
