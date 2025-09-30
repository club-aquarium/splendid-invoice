from dataclasses import dataclass, field
from typing import Optional

from .duty_tax_fee_type_code_content_type import DutyTaxFeeTypeCodeContentType
from .tax_type_code_list_agency_idcontent_type import (
    TaxTypeCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TaxTypeCodeType:
    value: Optional[DutyTaxFeeTypeCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: TaxTypeCodeListAgencyIdcontentType = field(
        init=False,
        default=TaxTypeCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
