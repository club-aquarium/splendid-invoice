from dataclasses import dataclass, field
from typing import Optional

from .branch_financial_institution_type import BranchFinancialInstitutionType
from .financial_institution_address_type import FinancialInstitutionAddressType
from .idtype import Idtype
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class CreditorFinancialInstitutionType:
    """
    Creditor Financial Institution.

    :ivar bicid: BIC ID
    :ivar chipsuniversal_id: CHIPS Universal ID
    :ivar new_zealand_nccid: New Zealand NCC ID
    :ivar irish_nscid: Irish NSC ID
    :ivar uksort_code_id: UK Sort Code ID
    :ivar chipsparticipant_id: CHIPS Participant ID
    :ivar swiss_bcid: Swiss BC ID
    :ivar fedwire_routing_number_id: Fedwire Routing Number ID
    :ivar portuguese_nccid: Portuguese NCC ID
    :ivar russian_central_bank_id: Russian Central Bank ID
    :ivar italian_domestic_id: Italian Domestic ID
    :ivar austrian_bankleitzahl_id: Austrian Bankleitzahl ID
    :ivar canadian_payments_association_id: Canadian Payments
        Association ID
    :ivar sicid: SIC ID
    :ivar german_bankleitzahl_id: German Bankleitzahl ID
    :ivar spanish_domestic_interbanking_id: Spanish Domestic
        Interbanking ID
    :ivar south_african_nccid: South African NCC ID
    :ivar hong_kong_bank_id: Hong Kong Bank ID
    :ivar australian_bsbid: Australian BSB ID
    :ivar indian_financial_system_id: Indian Financial System ID
    :ivar hellenic_bank_id: Hellenic Bank ID
    :ivar polish_national_clearing_id: Polish National Clearing ID
    :ivar name: Name
    :ivar clearing_system_name: Clearing System Name
    :ivar japan_financial_institution_common_id: Japan Financial
        Institution Common ID
    :ivar location_financial_institution_address: Address
    :ivar sub_division_branch_financial_institution: Branch
    """

    bicid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "BICID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    chipsuniversal_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "CHIPSUniversalID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    new_zealand_nccid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "NewZealandNCCID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    irish_nscid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "IrishNSCID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    uksort_code_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "UKSortCodeID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    chipsparticipant_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "CHIPSParticipantID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    swiss_bcid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SwissBCID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    fedwire_routing_number_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "FedwireRoutingNumberID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    portuguese_nccid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "PortugueseNCCID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    russian_central_bank_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "RussianCentralBankID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    italian_domestic_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ItalianDomesticID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    austrian_bankleitzahl_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "AustrianBankleitzahlID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    canadian_payments_association_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "CanadianPaymentsAssociationID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sicid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SICID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    german_bankleitzahl_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "GermanBankleitzahlID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    spanish_domestic_interbanking_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SpanishDomesticInterbankingID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    south_african_nccid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SouthAfricanNCCID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    hong_kong_bank_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "HongKongBankID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    australian_bsbid: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "AustralianBSBID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    indian_financial_system_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "IndianFinancialSystemID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    hellenic_bank_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "HellenicBankID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    polish_national_clearing_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "PolishNationalClearingID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    clearing_system_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ClearingSystemName",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    japan_financial_institution_common_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "JapanFinancialInstitutionCommonID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    location_financial_institution_address: Optional[
        FinancialInstitutionAddressType
    ] = field(
        default=None,
        metadata={
            "name": "LocationFinancialInstitutionAddress",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    sub_division_branch_financial_institution: Optional[
        BranchFinancialInstitutionType
    ] = field(
        default=None,
        metadata={
            "name": "SubDivisionBranchFinancialInstitution",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
