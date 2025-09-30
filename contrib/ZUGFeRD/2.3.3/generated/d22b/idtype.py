from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100"


@dataclass
class Idtype:
    class Meta:
        name = "IDType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    scheme_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeID",
            "type": "Attribute",
        },
    )
    scheme_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeName",
            "type": "Attribute",
        },
    )
    scheme_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeAgencyID",
            "type": "Attribute",
        },
    )
    scheme_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeAgencyName",
            "type": "Attribute",
        },
    )
    scheme_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeVersionID",
            "type": "Attribute",
        },
    )
    scheme_data_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeDataURI",
            "type": "Attribute",
        },
    )
    scheme_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeURI",
            "type": "Attribute",
        },
    )
