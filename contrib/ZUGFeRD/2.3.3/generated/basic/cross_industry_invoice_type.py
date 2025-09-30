from dataclasses import dataclass, field
from typing import Optional

from .exchanged_document_context_type import ExchangedDocumentContextType
from .exchanged_document_type import ExchangedDocumentType
from .supply_chain_trade_transaction_type import (
    SupplyChainTradeTransactionType,
)

__NAMESPACE__ = "urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100"


@dataclass
class CrossIndustryInvoiceType:
    exchanged_document_context: Optional[ExchangedDocumentContextType] = field(
        default=None,
        metadata={
            "name": "ExchangedDocumentContext",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100",
            "required": True,
        },
    )
    exchanged_document: Optional[ExchangedDocumentType] = field(
        default=None,
        metadata={
            "name": "ExchangedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100",
            "required": True,
        },
    )
    supply_chain_trade_transaction: Optional[SupplyChainTradeTransactionType] = field(
        default=None,
        metadata={
            "name": "SupplyChainTradeTransaction",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100",
            "required": True,
        },
    )
