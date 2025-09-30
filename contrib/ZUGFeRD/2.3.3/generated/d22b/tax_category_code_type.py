from dataclasses import dataclass, field
from typing import Optional

from .dutyor_taxor_fee_category_code_content_type import (
    DutyorTaxorFeeCategoryCodeContentType,
)
from .tax_category_code_list_agency_idcontent_type import (
    TaxCategoryCodeListAgencyIdcontentType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:QualifiedDataType:100"


@dataclass
class TaxCategoryCodeType:
    value: Optional[DutyorTaxorFeeCategoryCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    list_agency_id: TaxCategoryCodeListAgencyIdcontentType = field(
        init=False,
        default=TaxCategoryCodeListAgencyIdcontentType.VALUE_6,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
