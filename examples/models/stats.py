"""
Iconik Stats Models
This module contains Pydantic models for the Iconik Stats API.
"""
from __future__ import annotations
from datetime import date, datetime
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class UserUsagesSchema(BaseModel):
    """Represents a UserUsagesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['UserUsagesElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class UserUsagesElasticSchema(BaseModel):
    """Represents a UserUsagesElasticSchema in the Iconik system."""
    count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[str] = None
    id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None
    type: Optional[str] = None
    user_email: Optional[str] = None
    user_id: Optional[UUID] = None
    user_name: Optional[str] = None


class UserUsagesDetailedSchema(BaseModel):
    """Represents a UserUsagesDetailedSchema in the Iconik system."""
    date: Optional[str] = None
    system_domain_id: Optional[UUID] = None
    type: Optional[str] = None
    user_id: Optional[UUID] = None


class UserAuditSchema(BaseModel):
    """Represents a UserAuditSchema in the Iconik system."""
    app_id: Optional[UUID] = None
    client_ip: Optional[str] = None
    date: Optional[date] = None
    id: Optional[UUID] = None
    is_acting_as_user: Optional[bool] = None
    metadata: Optional[str] = None
    operation_result: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    operation_type: Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
    original_user_id: Optional[UUID] = None
    payload: Optional[str] = None
    request_id: Optional[str] = None
    resource: Optional[str] = None
    share_id: Optional[UUID] = None
    share_user_id: Optional[UUID] = None
    sudo: Optional[bool] = None
    system_domain_id: Optional[UUID] = None
    system_name: str
    time: Optional[datetime] = None
    user_agent: Optional[str] = None
    user_id: Optional[UUID] = None


class UnpublishedUserAuditSchema(BaseModel):
    """Represents a UnpublishedUserAuditSchema in the Iconik system."""
    app_id: Optional[UUID] = None
    client_ip: Optional[str] = None
    date: Optional[date] = None
    id: Optional[UUID] = None
    is_acting_as_user: Optional[bool] = None
    log_recipient_id: UUID
    metadata: Optional[str] = None
    operation_result: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    operation_type: Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
    original_user_id: Optional[UUID] = None
    payload: Optional[str] = None
    request_id: Optional[str] = None
    resource: Optional[str] = None
    share_id: Optional[UUID] = None
    share_user_id: Optional[UUID] = None
    sudo: Optional[bool] = None
    system_domain_id: Optional[UUID] = None
    system_name: str
    time: Optional[datetime] = None
    user_agent: Optional[str] = None
    user_id: Optional[UUID] = None


class TransferStatsSchema(BaseModel):
    """Represents a TransferStatsSchema in the Iconik system."""
    bytes_sent: int = Field(
        ..., ge=-9223372036854775808, le=9223372036854775807
    )
    ip: Optional[str] = None
    object_info: Optional[str] = None
    object_name: Optional[str] = None
    time_taken_us: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class TranscoderUsagesSchema(BaseModel):
    """Represents a TranscoderUsagesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['TranscoderUsagesElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class TranscoderUsagesElasticSchema(BaseModel):
    """Represents a TranscoderUsagesElasticSchema in the Iconik system."""
    count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[str] = None
    destination_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    duration_seconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    id: Optional[UUID] = None
    is_user_transcoder: Optional[bool] = None
    operation_type: Optional[Literal['TRANSCODE', 'TRANSCODE_AUDIO',
                                     'TRANSCODE_VIDEO', 'TRANSCODE_IMAGE',
                                     'TRANSCODE_KEYFRAMES', 'MEDIAINFO',
                                     'CONFORM', 'EXTRACT_AUDIO',
                                     'EXTRACT_IMAGE', 'ANALYZE', 'TRANSCRIBE',
                                     'TRANSCRIBE_HUMAN']] = None
    source_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    system_domain_id: Optional[UUID] = None
    transcoder_type: Literal['VANTAGE', 'FFMPEG', 'FFMPEG_FIRST_FRAME',
                             'IMAGEMAGICK', 'SUBTITLES', 'ENCODING_COM',
                             'ZENCODER', 'TELESTREAM_CLOUD',
                             'GOOGLE_VIDEO_INTELLIGENCE', 'GOOGLE_VISION',
                             'COLLECTION_KEYFRAMES', 'AMAZON_REKOGNITION_IMAGE',
                             'AMAZON_REKOGNITION_VIDEO',
                             'ELEMENTAL_MEDIACONVERT', 'ELEMENTAL_SERVER',
                             'MEDIAINFO', 'ICONIK_EDGE_TRANSCODER', 'NONE',
                             'REV_AI_TRANSCRIPTION', 'GCVI_TRANSCRIPTION',
                             'AMAZON_TRANSCRIBE', 'OPEN_GRAPH']


class TranscoderUsageSchema(BaseModel):
    """Represents a TranscoderUsageSchema in the Iconik system."""
    adjusted_duration_seconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[date] = None
    destination_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    duration_seconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    id: Optional[UUID] = None
    is_user_transcoder: Optional[bool] = None
    job_id: Optional[UUID] = None
    object_id: Optional[UUID] = None
    object_type: Optional[str] = None
    operation_type: Optional[Literal['TRANSCODE', 'TRANSCODE_AUDIO',
                                     'TRANSCODE_VIDEO', 'TRANSCODE_IMAGE',
                                     'TRANSCODE_KEYFRAMES', 'MEDIAINFO',
                                     'CONFORM', 'EXTRACT_AUDIO',
                                     'EXTRACT_IMAGE', 'ANALYZE', 'TRANSCRIBE',
                                     'TRANSCRIBE_HUMAN']] = None
    percent_done: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    source_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Literal['FAILED', 'FINISHED', 'ABORTED']
    system_domain_id: Optional[UUID] = None
    system_name: str
    time: Optional[datetime] = None
    transcoder_type: Literal['VANTAGE', 'FFMPEG', 'FFMPEG_FIRST_FRAME',
                             'IMAGEMAGICK', 'SUBTITLES', 'ENCODING_COM',
                             'ZENCODER', 'TELESTREAM_CLOUD',
                             'GOOGLE_VIDEO_INTELLIGENCE', 'GOOGLE_VISION',
                             'COLLECTION_KEYFRAMES', 'AMAZON_REKOGNITION_IMAGE',
                             'AMAZON_REKOGNITION_VIDEO',
                             'ELEMENTAL_MEDIACONVERT', 'ELEMENTAL_SERVER',
                             'MEDIAINFO', 'ICONIK_EDGE_TRANSCODER', 'NONE',
                             'REV_AI_TRANSCRIPTION', 'GCVI_TRANSCRIPTION',
                             'AMAZON_TRANSCRIBE', 'OPEN_GRAPH']


class StorageUsagesSchema(BaseModel):
    """Represents a StorageUsagesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['StorageUsagesElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class StorageUsagesElasticSchema(BaseModel):
    """Represents a StorageUsagesElasticSchema in the Iconik system."""
    bucket_name: Optional[str] = None
    bytes_stored: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[str] = None
    id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class StorageUsageSchema(BaseModel):
    """Represents a StorageUsageSchema in the Iconik system."""
    bucket_name: str
    bytes_stored: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[datetime] = None
    id: Optional[UUID] = None
    storage_type: Literal['FILE', 'HTTP', 'FTP', 'SFTP', 'S3', 'OMMS', 'GCS',
                          'B2', 'AZURE', 'TRANSFER']
    system_domain_id: Optional[UUID] = None
    system_name: str


class StorageAccessesSchema(BaseModel):
    """Represents a StorageAccessesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['StorageAccessElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class StorageAccessSchema(BaseModel):
    """Represents a StorageAccessSchema in the Iconik system."""
    bucket_name: str
    bytes_received: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    bytes_sent: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[datetime] = None
    id: Optional[UUID] = None
    operation_type: str
    operations: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    storage_type: Literal['FILE', 'HTTP', 'FTP', 'SFTP', 'S3', 'OMMS', 'GCS',
                          'B2', 'AZURE', 'TRANSFER']
    system_domain_id: Optional[UUID] = None
    system_name: str


class StorageAccessElasticSchema(BaseModel):
    """Represents a StorageAccessElasticSchema in the Iconik system."""
    bucket_name: Optional[str] = None
    bytes_received: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    bytes_sent: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[str] = None
    id: Optional[UUID] = None
    operations: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    system_domain_id: Optional[UUID] = None


class PricesSchema(BaseModel):
    """Represents a PricesSchema in the Iconik system."""
    objects: Optional[List['PriceSchema']] = Field(default_factory=list)


class PriceSchema(BaseModel):
    """Represents a PriceSchema in the Iconik system."""
    currency: Literal['EUR', 'USD']
    name: str
    prices: Dict[str, Any]


class LogsRecipientsSchema(BaseModel):
    """Represents a LogsRecipientsSchema in the Iconik system."""
    objects: Optional[List['LogsRecipientSchema']] = Field(default_factory=list)


class LogsRecipientSchema(BaseModel):
    """Represents a LogsRecipientSchema in the Iconik system."""
    id: Optional[UUID] = None
    method: Literal['GOOGLE', 'AMAZON']
    name: str
    settings: Dict[str, Any]


class LogsRecipientReadSchema(BaseModel):
    """Represents a LogsRecipientReadSchema in the Iconik system."""
    id: Optional[UUID] = None
    method: Literal['GOOGLE', 'AMAZON']
    name: str
    settings: Dict[str, Any]


class ListObjectsSchema(BaseModel):
    """Represents a ListObjectsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class DateFilterSchema(BaseModel):
    """Represents a DateFilterSchema in the Iconik system."""
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None


class CurrentUsageSchema(BaseModel):
    """Represents a CurrentUsageSchema in the Iconik system."""
    automation_runs: Optional[int] = None
    edge_transcoders: Optional[int] = None
    images_analyzed: Optional[int] = None
    shield_enabled: Optional[bool] = None
    storage: Optional[Dict[str, Any]] = Field(default_factory=dict)
    transcription_hours: Optional[float] = None
    users: Optional[Dict[str, Any]] = Field(default_factory=dict)
    video_analyzed_hours: Optional[float] = None


class CreditsSchema(BaseModel):
    """Represents a CreditsSchema in the Iconik system."""
    country: Optional[str] = None
    credits: int = Field(..., ge=1)
    currency: Optional[str] = None
    total: Optional[float] = None
    vat: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class CollectionUsagesSchema(BaseModel):
    """Represents a CollectionUsagesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['CollectionUsagesElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class CollectionUsagesElasticSchema(BaseModel):
    """Represents a CollectionUsagesElasticSchema in the Iconik system."""
    count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[str] = None
    id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class CollectionUsageSchema(BaseModel):
    """Represents a CollectionUsageSchema in the Iconik system."""
    collection_id: UUID
    date: Optional[date] = None
    id: Optional[UUID] = None
    metadata: Optional[str] = None
    operation_source: Optional[Literal['COLLECTION', 'SEARCH',
                                       'NOTIFICATION']] = None
    operation_type: Literal['VIEW', 'DELETE', 'CREATE', 'RENAME']
    system_domain_id: Optional[UUID] = None
    system_name: str
    time: Optional[datetime] = None
    user_id: UUID


class BillingsSchema(BaseModel):
    """Represents a BillingsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['BillingSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class BillingStatsSchema(BaseModel):
    """Represents a BillingStatsSchema in the Iconik system."""
    current_balance: Optional[float] = None
    invoice_end_of_month: Optional[bool] = None
    new_billing_enabled: Optional[bool] = None
    stripe_id: Optional[bool] = None
    system_domain_status: Optional[Literal['USD', 'EUR']] = None
    system_domain_type: str
    system_domain_warning_message: str


class BillingSettingsSchema(BaseModel):
    """Represents a BillingSettingsSchema in the Iconik system."""
    auto_refill_amount: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    enable_auto_top_up: Optional[bool] = None
    low_balance_trigger: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )


class BillingSchema(BaseModel):
    """Represents a BillingSchema in the Iconik system."""
    balance: Optional[float] = None
    consumption_subtype: Optional[str] = None
    consumption_type: Optional[str] = None
    currency: Optional[Literal['USD', 'EUR']] = None
    date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None
    id: Optional[UUID] = None
    label: str
    price_list: Optional[str] = None
    system_domain_id: UUID
    value: float


class BillingRecipientsSchema(BaseModel):
    """Represents a BillingRecipientsSchema in the Iconik system."""
    emails: Optional[List[str]] = Field(default_factory=list)


class BillingReceiptSchema(BaseModel):
    """Represents a BillingReceiptSchema in the Iconik system."""
    receipt_url: Optional[str] = None


class BillingExpirationUpdateSchema(BaseModel):
    """Represents a BillingExpirationUpdateSchema in the Iconik system."""
    expiration_date: datetime


class BillingCustomerShippingSchema(BaseModel):
    """Represents a BillingCustomerShippingSchema in the Iconik system."""
    address: 'BillingCustomerShippingAddressSchema'
    name: str
    phone: Optional[str] = None


class BillingCustomerShippingAddressSchema(BaseModel):
    """Represents a BillingCustomerShippingAddressSchema in the Iconik system."""
    city: str
    country: str
    line1: str
    line2: Optional[str] = None
    postal_code: str
    state: Optional[str] = None


class BillingCustomerSchema(BaseModel):
    """Represents a BillingCustomerSchema in the Iconik system."""
    business_vat_id: Optional[str] = None
    email: Optional[str] = None
    enable_subscription: Optional[bool] = None
    shipping: 'BillingCustomerShipping'


class BillingCustomerShipping(BaseModel):
    """Represents a BillingCustomerShipping in the Iconik system."""
    address: 'BillingCustomerShippingAddress'
    name: str
    phone: Optional[str] = None


class BillingCustomerShippingAddress(BaseModel):
    """Represents a BillingCustomerShippingAddress in the Iconik system."""
    city: str
    country: str
    line1: str
    line2: Optional[str] = None
    postal_code: str
    state: Optional[str] = None


class BillingCustomerCardSchema(BaseModel):
    """Represents a BillingCustomerCardSchema in the Iconik system."""
    source: str


class BillingCreditsVerifySchema(BaseModel):
    """Represents a BillingCreditsVerifySchema in the Iconik system."""
    charge: Optional[str] = None
    invoice_id: str
    system_domain_id: Optional[UUID] = None


class BillingCreditsSchema(BaseModel):
    """Represents a BillingCreditsSchema in the Iconik system."""
    auto_pay: Optional[bool] = None
    country: Optional[str] = None
    credits: int = Field(..., ge=1)
    currency: Optional[str] = None
    custom_message: Optional[str] = None
    system_domain_id: Optional[UUID] = None
    total: Optional[str] = None
    vat: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class AutomationRunsSchema(BaseModel):
    """Represents a AutomationRunsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['AutomationRunSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class AutomationRunSchema(BaseModel):
    """Represents a AutomationRunSchema in the Iconik system."""
    count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[date] = None
    system_domain_id: Optional[UUID] = None


class AssetUsagesSchema(BaseModel):
    """Represents a AssetUsagesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['AssetUsagesElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class AssetUsagesElasticSchema(BaseModel):
    """Represents a AssetUsagesElasticSchema in the Iconik system."""
    count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    date: Optional[str] = None
    id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class AssetUsageSchema(BaseModel):
    """Represents a AssetUsageSchema in the Iconik system."""
    asset_id: UUID
    asset_type: Optional[Literal['ASSET', 'SEQUENCE', 'NLE_PROJECT',
                                 'PLACEHOLDER']] = None
    date: Optional[date] = None
    id: Optional[UUID] = None
    metadata: Optional[str] = None
    operation_source: Optional[Literal['COLLECTION', 'SEARCH', 'NOTIFICATION',
                                       'DISCOVERY', 'SHARE', 'EXTERNAL_SHARE',
                                       '']] = None
    operation_type: Literal['VIEW', 'PLAY', 'PAUSE', 'DELETE', 'CREATE',
                            'APPROVE', 'REJECT', 'COMMENT', 'RENAME', 'EXIT',
                            'UNFOCUS', 'REFOCUS', 'SEEK']
    system_domain_id: Optional[UUID] = None
    system_name: str
    time: Optional[datetime] = None
    user_id: UUID


# Update forward references
UserUsagesSchema.model_rebuild()
UserUsagesElasticSchema.model_rebuild()
UserUsagesDetailedSchema.model_rebuild()
UserAuditSchema.model_rebuild()
UnpublishedUserAuditSchema.model_rebuild()
TransferStatsSchema.model_rebuild()
TranscoderUsagesSchema.model_rebuild()
TranscoderUsagesElasticSchema.model_rebuild()
TranscoderUsageSchema.model_rebuild()
StorageUsagesSchema.model_rebuild()
StorageUsagesElasticSchema.model_rebuild()
StorageUsageSchema.model_rebuild()
StorageAccessesSchema.model_rebuild()
StorageAccessSchema.model_rebuild()
StorageAccessElasticSchema.model_rebuild()
PricesSchema.model_rebuild()
PriceSchema.model_rebuild()
LogsRecipientsSchema.model_rebuild()
LogsRecipientSchema.model_rebuild()
LogsRecipientReadSchema.model_rebuild()
ListObjectsSchema.model_rebuild()
DateFilterSchema.model_rebuild()
CurrentUsageSchema.model_rebuild()
CreditsSchema.model_rebuild()
CollectionUsagesSchema.model_rebuild()
CollectionUsagesElasticSchema.model_rebuild()
CollectionUsageSchema.model_rebuild()
BillingsSchema.model_rebuild()
BillingStatsSchema.model_rebuild()
BillingSettingsSchema.model_rebuild()
BillingSchema.model_rebuild()
BillingRecipientsSchema.model_rebuild()
BillingReceiptSchema.model_rebuild()
BillingExpirationUpdateSchema.model_rebuild()
BillingCustomerShippingSchema.model_rebuild()
BillingCustomerShippingAddressSchema.model_rebuild()
BillingCustomerSchema.model_rebuild()
BillingCustomerShipping.model_rebuild()
BillingCustomerShippingAddress.model_rebuild()
BillingCustomerCardSchema.model_rebuild()
BillingCreditsVerifySchema.model_rebuild()
BillingCreditsSchema.model_rebuild()
AutomationRunsSchema.model_rebuild()
AutomationRunSchema.model_rebuild()
AssetUsagesSchema.model_rebuild()
AssetUsagesElasticSchema.model_rebuild()
AssetUsageSchema.model_rebuild()
