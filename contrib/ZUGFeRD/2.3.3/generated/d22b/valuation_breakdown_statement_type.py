from dataclasses import dataclass, field
from typing import Optional

from .basic_work_item_type import BasicWorkItemType
from .calculated_price_type import CalculatedPriceType
from .code_type import CodeType
from .currency_code_type import CurrencyCodeType
from .date_time_type import DateTimeType
from .grouped_work_item_type import GroupedWorkItemType
from .idtype import Idtype
from .recorded_status_type import RecordedStatusType
from .specified_binary_file_type import SpecifiedBinaryFileType
from .text_type import TextType

__NAMESPACE__ = (
    "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
)


@dataclass
class ValuationBreakdownStatementType:
    """
    Valuation Breakdown Statement.

    :ivar id: ID
    :ivar name: Name
    :ivar description: Description
    :ivar measurement_method_id: Measurement Method ID
    :ivar creation_date_time: Creation Date Time
    :ivar default_currency_code: Default Currency Code
    :ivar default_language_code: Default Language Code
    :ivar comment: Comment
    :ivar type_code: Type Code
    :ivar requested_action_code: Requested Action Code
    :ivar price_list_id: Price List ID
    :ivar contractual_language_code: Contractual Language Code
    :ivar item_grouped_work_item: Grouped Work Item
    :ivar item_basic_work_item: Basic Work Item
    :ivar total_calculated_price: Total Calculated Price
    :ivar changed_recorded_status: Changed Recorded Status
    :ivar creation_specified_binary_file: Creation Binary File
    :ivar reader_specified_binary_file: Reader Binary File
    :ivar referenced_specified_binary_file: Referenced Binary File
    """

    id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    description: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    measurement_method_id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementMethodID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    creation_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "CreationDateTime",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    default_currency_code: Optional[CurrencyCodeType] = field(
        default=None,
        metadata={
            "name": "DefaultCurrencyCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    default_language_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "DefaultLanguageCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
            "required": True,
        },
    )
    comment: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    type_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    requested_action_code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "RequestedActionCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    price_list_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "PriceListID",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    contractual_language_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ContractualLanguageCode",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    item_grouped_work_item: list[GroupedWorkItemType] = field(
        default_factory=list,
        metadata={
            "name": "ItemGroupedWorkItem",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    item_basic_work_item: list[BasicWorkItemType] = field(
        default_factory=list,
        metadata={
            "name": "ItemBasicWorkItem",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    total_calculated_price: list[CalculatedPriceType] = field(
        default_factory=list,
        metadata={
            "name": "TotalCalculatedPrice",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    changed_recorded_status: list[RecordedStatusType] = field(
        default_factory=list,
        metadata={
            "name": "ChangedRecordedStatus",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    creation_specified_binary_file: list[SpecifiedBinaryFileType] = field(
        default_factory=list,
        metadata={
            "name": "CreationSpecifiedBinaryFile",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    reader_specified_binary_file: list[SpecifiedBinaryFileType] = field(
        default_factory=list,
        metadata={
            "name": "ReaderSpecifiedBinaryFile",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
    referenced_specified_binary_file: list[SpecifiedBinaryFileType] = field(
        default_factory=list,
        metadata={
            "name": "ReferencedSpecifiedBinaryFile",
            "type": "Element",
            "namespace": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100",
        },
    )
