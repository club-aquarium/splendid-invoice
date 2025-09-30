from dataclasses import dataclass, field
from typing import Optional

from .transport_means_type_code_content_type import (
    TransportMeansTypeCodeContentType,
)
from .transport_means_type_code_list_agency_idcontent_type import (
    TransportMeansTypeCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TransportMeansTypeCodeType:
    value: Optional[TransportMeansTypeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: TransportMeansTypeCodeListAgencyIdcontentType = field(
        init=False,
        default=TransportMeansTypeCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
