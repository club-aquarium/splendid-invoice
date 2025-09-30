from dataclasses import dataclass, field
from typing import Optional

from .freight_charge_quantity_unit_basis_code_content_type import (
    FreightChargeQuantityUnitBasisCodeContentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class LogisticsChargeCalculationBasisCodeType:
    value: Optional[FreightChargeQuantityUnitBasisCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: str = field(
        init=False,
        default="6",
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
