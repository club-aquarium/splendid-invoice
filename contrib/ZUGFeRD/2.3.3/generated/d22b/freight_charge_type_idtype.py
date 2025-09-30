from dataclasses import dataclass, field
from typing import Optional

from .freight_charge_type_idscheme_agency_idcontent_type import (
    FreightChargeTypeIdschemeAgencyIdcontentType,
)
from .freight_cost_code_content_type import FreightCostCodeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class FreightChargeTypeIdtype:
    class Meta:
        name = "FreightChargeTypeIDType"

    value: Optional[FreightCostCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    scheme_agency_id: Optional[FreightChargeTypeIdschemeAgencyIdcontentType] = field(
        default=None,
        metadata={
            "name": "schemeAgencyID",
            "type": "Attribute",
        },
    )
