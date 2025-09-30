from enum import Enum

__NAMESPACE__ = "urn:un:unece:uncefact:codelist:standard:UNECE:DeliveryTermsCode:2020"


class DeliveryTermsCodeContentType(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    CFR = "CFR"
    CIF = "CIF"
    CIP = "CIP"
    CPT = "CPT"
    DAP = "DAP"
    DDP = "DDP"
    DPU = "DPU"
    EXW = "EXW"
    FAS = "FAS"
    FCA = "FCA"
    FOB = "FOB"
