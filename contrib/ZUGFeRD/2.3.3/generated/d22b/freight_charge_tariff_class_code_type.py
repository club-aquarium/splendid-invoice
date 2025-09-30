from dataclasses import dataclass, field
from typing import Optional

from .freight_charge_tariff_class_code_list_agency_idcontent_type import (
    FreightChargeTariffClassCodeListAgencyIdcontentType,
)
from .freight_charge_tariff_code_content_type import (
    FreightChargeTariffCodeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class FreightChargeTariffClassCodeType:
    value: Optional[FreightChargeTariffCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: FreightChargeTariffClassCodeListAgencyIdcontentType = field(
        init=False,
        default=FreightChargeTariffClassCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
