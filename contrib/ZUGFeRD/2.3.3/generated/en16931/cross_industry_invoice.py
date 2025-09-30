from dataclasses import dataclass

from .cross_industry_invoice_type import CrossIndustryInvoiceType

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100"


@dataclass
class CrossIndustryInvoice(CrossIndustryInvoiceType):
    class Meta:
        namespace = "urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100"
