from dataclasses import dataclass, field
from typing import Optional

from .communication_channel_code_list_agency_idcontent_type import (
    CommunicationChannelCodeListAgencyIdcontentType,
)
from .communication_means_type_code_content_type import (
    CommunicationMeansTypeCodeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class CommunicationChannelCodeType:
    value: Optional[CommunicationMeansTypeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: CommunicationChannelCodeListAgencyIdcontentType = field(
        init=False,
        default=CommunicationChannelCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
