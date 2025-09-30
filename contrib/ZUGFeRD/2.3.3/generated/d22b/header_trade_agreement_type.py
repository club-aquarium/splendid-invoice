from dataclasses import dataclass, field
from typing import Optional

from .logistics_location_type import LogisticsLocationType
from .procuring_project_type import ProcuringProjectType
from .referenced_document_type import ReferencedDocumentType
from .text_type import TextType
from .trade_delivery_terms_type import TradeDeliveryTermsType
from .trade_party_type import TradePartyType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class HeaderTradeAgreementType:
    """
    Header Trade Agreement.

    :ivar reference: Reference Text
    :ivar buyer_reference: Buyer Reference Text
    :ivar seller_trade_party: Seller
    :ivar buyer_trade_party: Buyer
    :ivar sales_agent_trade_party: Sales Agent
    :ivar buyer_requisitioner_trade_party: Buyer Requisitioner
    :ivar buyer_assigned_accountant_trade_party: Buyer Assigned
        Accountant
    :ivar seller_assigned_accountant_trade_party: Seller Assigned
        Accountant
    :ivar buyer_tax_representative_trade_party: Buyer Tax Representative
    :ivar seller_tax_representative_trade_party: Seller Tax
        Representative
    :ivar product_end_user_trade_party: End User
    :ivar applicable_trade_delivery_terms: Trade Delivery Terms
    :ivar seller_order_referenced_document: Seller Order Document
    :ivar buyer_order_referenced_document: Buyer Order Document
    :ivar quotation_referenced_document: Quotation Document
    :ivar order_response_referenced_document: Order Response Document
    :ivar contract_referenced_document: Contract Document
    :ivar demand_forecast_referenced_document: Demand Forecast Document
    :ivar supply_instruction_referenced_document: Supply Instruction
        Document
    :ivar promotional_deal_referenced_document: Promotional Deal
        Document
    :ivar price_list_referenced_document: Price List Document
    :ivar additional_referenced_document: Additional Document
    :ivar requisitioner_referenced_document: Requisitioner Document
    :ivar buyer_agent_trade_party: Buyer Agent
    :ivar purchase_conditions_referenced_document: Purchase Conditions
        Document
    :ivar specified_procuring_project: Procuring Project
    :ivar ultimate_customer_order_referenced_document: Ultimate Customer
        Order Document
    :ivar pricing_base_applicable_logistics_location: Pricing Base
        Applicable Logistics Location
    """

    reference: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_reference: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "BuyerReference",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    seller_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "SellerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "BuyerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sales_agent_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "SalesAgentTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_requisitioner_trade_party: list[TradePartyType] = field(
        default_factory=list,
        metadata={
            "name": "BuyerRequisitionerTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_assigned_accountant_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "BuyerAssignedAccountantTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    seller_assigned_accountant_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "SellerAssignedAccountantTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_tax_representative_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "BuyerTaxRepresentativeTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    seller_tax_representative_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "SellerTaxRepresentativeTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    product_end_user_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "ProductEndUserTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    applicable_trade_delivery_terms: Optional[TradeDeliveryTermsType] = field(
        default=None,
        metadata={
            "name": "ApplicableTradeDeliveryTerms",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    seller_order_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "SellerOrderReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_order_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "BuyerOrderReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    quotation_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "QuotationReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    order_response_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "OrderResponseReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    contract_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "ContractReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    demand_forecast_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "DemandForecastReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    supply_instruction_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "SupplyInstructionReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    promotional_deal_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "PromotionalDealReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    price_list_referenced_document: Optional[ReferencedDocumentType] = field(
        default=None,
        metadata={
            "name": "PriceListReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    additional_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    requisitioner_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "RequisitionerReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    buyer_agent_trade_party: Optional[TradePartyType] = field(
        default=None,
        metadata={
            "name": "BuyerAgentTradeParty",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    purchase_conditions_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseConditionsReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    specified_procuring_project: Optional[ProcuringProjectType] = field(
        default=None,
        metadata={
            "name": "SpecifiedProcuringProject",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    ultimate_customer_order_referenced_document: list[ReferencedDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "UltimateCustomerOrderReferencedDocument",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    pricing_base_applicable_logistics_location: Optional[LogisticsLocationType] = field(
        default=None,
        metadata={
            "name": "PricingBaseApplicableLogisticsLocation",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
