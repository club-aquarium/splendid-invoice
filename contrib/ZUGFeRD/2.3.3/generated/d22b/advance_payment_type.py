from dataclasses import dataclass, field
from typing import Optional

from .amount_type import AmountType
from .formatted_date_time_type import FormattedDateTimeType
from .referenced_document_type import ReferencedDocumentType
from .trade_tax_type import TradeTaxType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class AdvancePaymentType:
    """
    Advance Payment.

    :ivar paid_amount: Paid Amount
    :ivar formatted_received_date_time: Formatted Received Date Time
    :ivar included_trade_tax: Included Tax
    :ivar invoice_specified_referenced_document: Invoice Document
    """

    paid_amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "PaidAmount",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    formatted_received_date_time: Optional[FormattedDateTimeType] = field(
        default=None,
        metadata={
            "name": "FormattedReceivedDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    included_trade_tax: list[TradeTaxType] = field(
        default_factory=list,
        metadata={
            "name": "IncludedTradeTax",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    invoice_specified_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceSpecifiedReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
