"""
Iconik Automations Models
This module contains Pydantic models for the Iconik Automations API.
"""
from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class _TriggerSchemaBase(BaseModel):
    """Represents a _TriggerSchemaBase in the Iconik system."""
    parameters: Optional[Dict[str, Any]] = Field(default_factory=dict)


class _ObjectCollectionTriggerParametersSchema(BaseModel):
    """Represents a _ObjectCollectionTriggerParametersSchema in the Iconik system."""
    collection_ids: List[UUID]
    include_subcollections: Optional[bool] = None
    object_type: str


class _ActionSchemaBase(BaseModel):
    """Represents a _ActionSchemaBase in the Iconik system."""
    parameters: Optional[Dict[str, Any]] = Field(default_factory=dict)


class UpdateACLActionSchema(BaseModel):
    """Represents a UpdateACLActionSchema in the Iconik system."""
    parameters: 'UpdateACLActionParameters'
    type: Literal['UPDATE_ACL']


class UpdateACLAction(BaseModel):
    """Represents a UpdateACLAction in the Iconik system."""
    parameters: 'UpdateACLActionParameters'
    type: Literal['UPDATE_ACL']


class UpdateACLActionParameters(BaseModel):
    """Represents a UpdateACLActionParameters in the Iconik system."""
    objects: List['ACLUpdateSchema']


class TriggersSchema(BaseModel):
    """Represents a TriggersSchema in the Iconik system."""
    objects: Optional[List['TriggerSchema']] = Field(default_factory=list)


class TriggerSchema(BaseModel):
    """Represents a TriggerSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    event_type: Literal['ASSETS', 'COLLECTIONS']
    execute_at: Optional[datetime] = None
    filters: Optional[List['ConditionSchema']] = Field(default_factory=list)
    object_id: Optional[UUID] = None
    operations: Optional[List[Literal['CREATE', 'UPDATE', 'DELETE', 'SHARE',
                                      'DELAYED_TRIGGER']]
                         ] = Field(default_factory=list)
    realm: Optional[Literal['ENTITY', 'METADATA', 'FORMATS', 'FILES', 'SHARES',
                            'JOBS']] = None
    type: Literal['METADATA_UPDATE', 'ASSET_SHARE', 'TRANSFER_TO_STORAGE',
                  'MODIFIED_AT_TRANSITION', 'CREATED_AT_TRANSITION', 'ARCHIVE',
                  'RESTORE', 'ASSET_ONLINE']


class TriggerCustomActionSchema(BaseModel):
    """Represents a TriggerCustomActionSchema in the Iconik system."""
    parameters: 'TriggerCustomActionParameters'
    type: Literal['CUSTOM_ACTION']


class TriggerCustomAction(BaseModel):
    """Represents a TriggerCustomAction in the Iconik system."""
    parameters: 'TriggerCustomActionParameters'
    type: Literal['CUSTOM_ACTION']


class TriggerCustomActionParameters(BaseModel):
    """Represents a TriggerCustomActionParameters in the Iconik system."""
    action_id: UUID
    context: Literal['ASSET', 'COLLECTION']
    metadata_values: Optional[Dict[str, 'MetadataFieldValueSchema']
                              ] = Field(default_factory=dict)


class TransferActionSchema(BaseModel):
    """Represents a TransferActionSchema in the Iconik system."""
    parameters: 'TransferActionParametersSchema'
    type: Literal['TRANSFER']


class TransferActionParametersSchema(BaseModel):
    """Represents a TransferActionParametersSchema in the Iconik system."""
    allow_host_transfer: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_storage_id: UUID
    format_name: str


class TranscribeActionSchema(BaseModel):
    """Represents a TranscribeActionSchema in the Iconik system."""
    parameters: 'TranscribeActionParameters'
    type: Literal['TRANSCRIBE']


class TranscribeAction(BaseModel):
    """Represents a TranscribeAction in the Iconik system."""
    parameters: 'TranscribeActionParameters'
    type: Literal['TRANSCRIBE']


class TranscribeActionParameters(BaseModel):
    """Represents a TranscribeActionParameters in the Iconik system."""
    engine: Optional[str] = None
    force: Optional[bool] = None
    language: Optional[str] = None
    speakers: Optional[int] = Field(None, ge=1, le=100)
    summary: Optional[bool] = None
    topics_extraction: Optional[bool] = None
    translate_languages: Optional[List[str]] = Field(default_factory=list)


class TranscodeActionSchema(BaseModel):
    """Represents a TranscodeActionSchema in the Iconik system."""
    parameters: 'TranscodeActionParametersSchema'
    type: Literal['TRANSCODE']


class TranscodeActionParametersSchema(BaseModel):
    """Represents a TranscodeActionParametersSchema in the Iconik system."""
    format_name: Optional[str] = None
    prefer_any_cloud: Optional[bool] = None
    preferred_storage_id: Optional[UUID] = None
    preferred_storage_method: Optional[Literal['FILE', 'HTTP', 'FTP', 'SFTP',
                                               'S3', 'B2', 'GCS', 'PORTAL',
                                               'CUSTOM', 'AZURE']] = None
    priority: Optional[int] = Field(None, ge=1, le=10)


class TranscodeAction(BaseModel):
    """Represents a TranscodeAction in the Iconik system."""
    parameters: 'TranscodeActionParameters'
    type: Literal['TRANSCODE']


class TranscodeActionParameters(BaseModel):
    """Represents a TranscodeActionParameters in the Iconik system."""
    format_name: Optional[str] = None
    prefer_any_cloud: Optional[bool] = None
    preferred_storage_id: Optional[UUID] = None
    preferred_storage_method: Optional[Literal['FILE', 'HTTP', 'FTP', 'SFTP',
                                               'S3', 'B2', 'GCS', 'PORTAL',
                                               'CUSTOM', 'AZURE']] = None
    priority: Optional[int] = Field(None, ge=1, le=10)


class TermSchema(BaseModel):
    """Represents a TermSchema in the Iconik system."""
    exists: Optional[bool] = None
    missing: Optional[bool] = None
    name: str
    range: Optional['RangeFilterSchema'] = None
    value: Optional[Any] = None
    value_in: Optional[List[str]] = Field(default_factory=list)


class SubtitleAddedTriggerSchema(BaseModel):
    """Represents a SubtitleAddedTriggerSchema in the Iconik system."""
    parameters: 'SubtitleAddedTriggerParameters'
    type: Literal['SUBTITLE_ADDED']


class SubtitleAddedTrigger(BaseModel):
    """Represents a SubtitleAddedTrigger in the Iconik system."""
    parameters: 'SubtitleAddedTriggerParameters'
    type: Literal['SUBTITLE_ADDED']


class SubtitleAddedTriggerParameters(BaseModel):
    """Represents a SubtitleAddedTriggerParameters in the Iconik system."""
    closed_captions: Optional[bool] = None
    language: Optional[str] = None


class ReviewStatusChangedTriggerSchema(BaseModel):
    """Represents a ReviewStatusChangedTriggerSchema in the Iconik system."""
    parameters: 'ReviewStatusChangedTriggerParameters'
    type: Literal['REVIEW_STATUS_CHANGED']


class ReviewStatusChangedTrigger(BaseModel):
    """Represents a ReviewStatusChangedTrigger in the Iconik system."""
    parameters: 'ReviewStatusChangedTriggerParameters'
    type: Literal['REVIEW_STATUS_CHANGED']


class ReviewStatusChangedTriggerParameters(BaseModel):
    """Represents a ReviewStatusChangedTriggerParameters in the Iconik system."""
    statuses: Optional[List[Literal['N/A', 'REQUESTED', 'APPROVED',
                                    'NOT_APPROVED',
                                    'MIXED']]] = Field(default_factory=list)


class RestrictAssetActionSchema(BaseModel):
    """Represents a RestrictAssetActionSchema in the Iconik system."""
    parameters: 'RestrictAssetActionParameters'
    type: Literal['RESTRICT_ASSET']


class RestrictAssetAction(BaseModel):
    """Represents a RestrictAssetAction in the Iconik system."""
    parameters: 'RestrictAssetActionParameters'
    type: Literal['RESTRICT_ASSET']


class RestrictAssetActionParameters(BaseModel):
    """Represents a RestrictAssetActionParameters in the Iconik system."""
    restrict_metadata_field: str
    warning: Optional[str] = None
    warning_metadata_field: Optional[str] = None


class RestoreActionSchema(BaseModel):
    """Represents a RestoreActionSchema in the Iconik system."""
    parameters: 'RestoreActionParameters'
    type: Literal['RESTORE']


class RestoreAction(BaseModel):
    """Represents a RestoreAction in the Iconik system."""
    parameters: 'RestoreActionParameters'
    type: Literal['RESTORE']


class RestoreActionParameters(BaseModel):
    """Represents a RestoreActionParameters in the Iconik system."""
    allow_duplicate_transfers: Optional[bool] = None
    allow_host_transfer: Optional[bool] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_original: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_storage_id: UUID
    keep_collection_structure: Optional[bool] = None
    preferred_original_storage_id: Optional[UUID] = None


class RequestReviewActionSchema(BaseModel):
    """Represents a RequestReviewActionSchema in the Iconik system."""
    parameters: 'RequestReviewActionParameters'
    type: Literal['REQUEST_REVIEW']


class RequestReviewAction(BaseModel):
    """Represents a RequestReviewAction in the Iconik system."""
    parameters: 'RequestReviewActionParameters'
    type: Literal['REQUEST_REVIEW']


class RequestReviewActionParameters(BaseModel):
    """Represents a RequestReviewActionParameters in the Iconik system."""
    externals: Optional[List[str]] = Field(default_factory=list)
    groups: Optional[List[UUID]] = Field(default_factory=list)
    min_number: Optional[int] = Field(None, ge=1)
    share: 'CreateShareActionParameters'
    status: Optional[Literal['N/A', 'REQUESTED', 'APPROVED', 'NOT_APPROVED',
                             'MIXED']] = None
    users: Optional[List[UUID]] = Field(default_factory=list)


class RequestOriginalActionSchema(BaseModel):
    """Represents a RequestOriginalActionSchema in the Iconik system."""
    parameters: 'TransferActionParameters'
    type: Literal['REQUEST_ORIGINAL']


class RequestOriginalAction(BaseModel):
    """Represents a RequestOriginalAction in the Iconik system."""
    parameters: 'TransferActionParameters'
    type: Literal['REQUEST_ORIGINAL']


class TransferAction(BaseModel):
    """Represents a TransferAction in the Iconik system."""
    parameters: 'TransferActionParameters'
    type: Literal['TRANSFER']


class TransferActionParameters(BaseModel):
    """Represents a TransferActionParameters in the Iconik system."""
    allow_host_transfer: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_storage_id: UUID
    format_name: str


class RemoveAssetRestrictionActionSchema(BaseModel):
    """Represents a RemoveAssetRestrictionActionSchema in the Iconik system."""
    parameters: 'RemoveAssetRestrictionActionParameters'
    type: Literal['REMOVE_ASSET_RESTRICTION']


class RemoveAssetRestrictionAction(BaseModel):
    """Represents a RemoveAssetRestrictionAction in the Iconik system."""
    parameters: 'RemoveAssetRestrictionActionParameters'
    type: Literal['REMOVE_ASSET_RESTRICTION']


class RemoveAssetRestrictionActionParameters(BaseModel):
    """Represents a RemoveAssetRestrictionActionParameters in the Iconik system."""
    restrict_metadata_field: str
    warning_metadata_field: Optional[str] = None


class RangeFilterSchema(BaseModel):
    """Represents a RangeFilterSchema in the Iconik system."""
    max: Optional[str] = None
    min: Optional[str] = None
    timezone: Optional[str] = Field(
        None, description="Format: +02:00. Results returned in UTC by default"
    )


class ObjectRemovedFromCollectionTriggerSchema(BaseModel):
    """Represents a ObjectRemovedFromCollectionTriggerSchema in the Iconik system."""
    parameters: '_ObjectCollectionTriggerParameters'
    type: Literal['OBJECT_REMOVED_FROM_COLLECTION']


class ObjectRemovedFromCollectionTrigger(BaseModel):
    """Represents a ObjectRemovedFromCollectionTrigger in the Iconik system."""
    parameters: '_ObjectCollectionTriggerParameters'
    type: Literal['OBJECT_REMOVED_FROM_COLLECTION']


class ObjectAddedToCollectionTriggerSchema(BaseModel):
    """Represents a ObjectAddedToCollectionTriggerSchema in the Iconik system."""
    parameters: '_ObjectCollectionTriggerParameters'
    type: Literal['OBJECT_ADDED_TO_COLLECTION']


class ObjectAddedToCollectionTrigger(BaseModel):
    """Represents a ObjectAddedToCollectionTrigger in the Iconik system."""
    parameters: '_ObjectCollectionTriggerParameters'
    type: Literal['OBJECT_ADDED_TO_COLLECTION']


class _ObjectCollectionTriggerParameters(BaseModel):
    """Represents a _ObjectCollectionTriggerParameters in the Iconik system."""
    collection_ids: List[UUID]
    include_subcollections: Optional[bool] = None
    object_type: str


class ModifiedAtTransitionTriggerSchema(BaseModel):
    """Represents a ModifiedAtTransitionTriggerSchema in the Iconik system."""
    parameters: 'ModifiedAtTransitionTriggerParameters'
    type: Literal['MODIFIED_AT_TRANSITION']


class ModifiedAtTransitionTrigger(BaseModel):
    """Represents a ModifiedAtTransitionTrigger in the Iconik system."""
    parameters: 'ModifiedAtTransitionTriggerParameters'
    type: Literal['MODIFIED_AT_TRANSITION']


class ModifiedAtTransitionTriggerParameters(BaseModel):
    """Represents a ModifiedAtTransitionTriggerParameters in the Iconik system."""
    days_since_modified: int = Field(
        ...,
        ge=1,
        description=
        "Indicates a number of days passed since an objects was modified."
    )


class MetadataUpdateTriggerSchema(BaseModel):
    """Represents a MetadataUpdateTriggerSchema in the Iconik system."""
    parameters: 'MetadataUpdateTriggerParameters'
    type: Literal['METADATA_UPDATE']


class MetadataUpdateTrigger(BaseModel):
    """Represents a MetadataUpdateTrigger in the Iconik system."""
    parameters: 'MetadataUpdateTriggerParameters'
    type: Literal['METADATA_UPDATE']


class MetadataUpdateTriggerParameters(BaseModel):
    """Represents a MetadataUpdateTriggerParameters in the Iconik system."""
    event_type: Literal['ASSETS', 'COLLECTIONS']
    metadata_values: Dict[str, 'MetadataFieldValueSchema']


class MetadataUpdateActionSchema(BaseModel):
    """Represents a MetadataUpdateActionSchema in the Iconik system."""
    parameters: 'MetadataUpdateActionParameters'
    type: Literal['METADATA_UPDATE']


class MetadataUpdateAction(BaseModel):
    """Represents a MetadataUpdateAction in the Iconik system."""
    parameters: 'MetadataUpdateActionParameters'
    type: Literal['METADATA_UPDATE']


class MetadataUpdateActionParameters(BaseModel):
    """Represents a MetadataUpdateActionParameters in the Iconik system."""
    metadata_values: Dict[str, 'MetadataFieldValueUpdateSchema']
    metadata_view_id: UUID


class MetadataFieldValueUpdateSchema(BaseModel):
    """Represents a MetadataFieldValueUpdateSchema in the Iconik system."""
    field_values: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    mode: Optional[Literal['append', 'delete', 'overwrite']] = None


class MetadataFieldValueSchema(BaseModel):
    """Represents a MetadataFieldValueSchema in the Iconik system."""
    field_values: Optional[List[Dict[str, Any]]] = Field(default_factory=list)


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


class ExportActionSchema(BaseModel):
    """Represents a ExportActionSchema in the Iconik system."""
    parameters: 'ExportActionParameters'
    type: Literal['EXPORT']


class ExportAction(BaseModel):
    """Represents a ExportAction in the Iconik system."""
    parameters: 'ExportActionParameters'
    type: Literal['EXPORT']


class ExportActionParameters(BaseModel):
    """Represents a ExportActionParameters in the Iconik system."""
    export_location_id: UUID
    export_metadata: Optional[bool] = None
    export_to_asset_folder: Optional[bool] = None
    file_name: Optional[str] = None
    format_id: Optional[UUID] = None
    metadata_format: Optional[Literal['CSV', 'JSON', 'XML']] = None
    metadata_view: Optional[UUID] = None
    overwrite: Optional[bool] = None
    preferred_original_storage_id: Optional[UUID] = None
    transcode_profile_ids: Optional[List[UUID]] = Field(default_factory=list)


class DeleteActionSchema(BaseModel):
    """Represents a DeleteActionSchema in the Iconik system."""
    parameters: Optional[Dict[str, Any]] = Field(default_factory=dict)
    type: Literal['DELETE_ASSET']


class DeleteAction(BaseModel):
    """Represents a DeleteAction in the Iconik system."""
    parameters: Optional[Dict[str, Any]] = Field(default_factory=dict)
    type: Literal['DELETE_ASSET']


class CreatedAtTransitionTriggerSchema(BaseModel):
    """Represents a CreatedAtTransitionTriggerSchema in the Iconik system."""
    parameters: 'CreatedAtTransitionTriggerParameters'
    type: Literal['CREATED_AT_TRANSITION']


class CreatedAtTransitionTrigger(BaseModel):
    """Represents a CreatedAtTransitionTrigger in the Iconik system."""
    parameters: 'CreatedAtTransitionTriggerParameters'
    type: Literal['CREATED_AT_TRANSITION']


class CreatedAtTransitionTriggerParameters(BaseModel):
    """Represents a CreatedAtTransitionTriggerParameters in the Iconik system."""
    days_since_created: int = Field(
        ...,
        ge=1,
        description=
        "Indicates a number of days passed since an objects was created."
    )


class CreateShareActionSchema(BaseModel):
    """Represents a CreateShareActionSchema in the Iconik system."""
    parameters: 'CreateShareActionParametersSchema'
    type: Literal['CREATE_SHARE']


class CreateShareActionParametersSchema(BaseModel):
    """Represents a CreateShareActionParametersSchema in the Iconik system."""
    allow_approving_comments: bool
    allow_comments: bool
    allow_custom_actions: Optional[bool] = None
    allow_download: bool
    allow_download_proxy: Optional[bool] = None
    allow_setting_approve_status: bool
    allow_upload: Optional[bool] = None
    allow_user_search_for_mentions: Optional[bool] = None
    allow_view_transcriptions: Optional[bool] = None
    allow_view_versions: Optional[bool] = None
    emails: List[str]
    expires_in_days: Optional[int] = Field(None, ge=1)
    has_password: Optional[Any] = None
    message: Optional[str] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    password: Optional[str] = None
    show_watermark: Optional[bool] = None
    title: Optional[str] = None
    upload_storage_id: Optional[UUID] = None
    user_id: UUID


class CreateShareAction(BaseModel):
    """Represents a CreateShareAction in the Iconik system."""
    parameters: 'CreateShareActionParameters'
    type: Literal['CREATE_SHARE']


class CreateShareActionParameters(BaseModel):
    """Represents a CreateShareActionParameters in the Iconik system."""
    allow_approving_comments: bool
    allow_comments: bool
    allow_custom_actions: Optional[bool] = None
    allow_download: bool
    allow_download_proxy: Optional[bool] = None
    allow_setting_approve_status: bool
    allow_upload: Optional[bool] = None
    allow_user_search_for_mentions: Optional[bool] = None
    allow_view_transcriptions: Optional[bool] = None
    allow_view_versions: Optional[bool] = None
    emails: List[str]
    expires_in_days: Optional[int] = Field(None, ge=1)
    has_password: Optional[Any] = None
    message: Optional[str] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    password: Optional[str] = None
    show_watermark: Optional[bool] = None
    title: Optional[str] = None
    upload_storage_id: Optional[UUID] = None
    user_id: UUID


class ConditionSchema(BaseModel):
    """Represents a ConditionSchema in the Iconik system."""
    conditions: Optional[List['ConditionSchema']] = Field(default_factory=list)
    operator: str
    path: Optional[str] = None
    terms: Optional[List['Term']] = Field(default_factory=list)


class AutomationsSchema(BaseModel):
    """Represents a AutomationsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['AutomationSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class AutomationsInternalSchema(BaseModel):
    """Represents a AutomationsInternalSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['AutomationInternalSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class AutomationStatsSchema(BaseModel):
    """Represents a AutomationStatsSchema in the Iconik system."""
    objects: Optional[List['AutomationStatsObjectSchema']
                      ] = Field(default_factory=list)


class AutomationStatsObjectSchema(BaseModel):
    """Represents a AutomationStatsObjectSchema in the Iconik system."""
    name: str
    system_domain_id: UUID
    type: Literal['GAUGE']
    value: int


class AutomationSchema(BaseModel):
    """Represents a AutomationSchema in the Iconik system."""
    actions: List[Any]
    conditions: Optional[List['Condition']] = Field(default_factory=list)
    created_by: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    modified_by: Optional[UUID] = None
    name: str
    status: Optional[Literal['ACTIVE', 'INACTIVE']] = None
    system_domain_id: Optional[UUID] = None
    triggers: List[Any]


class AutomationRunEstimateSchema(BaseModel):
    """Represents a AutomationRunEstimateSchema in the Iconik system."""
    errors: Optional[List[str]] = Field(default_factory=list)
    facets: Optional[Dict[str, 'FacetSchema']] = Field(default_factory=dict)
    total: Optional[int] = None


class FacetSchema(BaseModel):
    """Represents a FacetSchema in the Iconik system."""
    buckets: Optional[List['BucketSchema']] = Field(default_factory=list)
    doc_count_error_upper_bound: Optional[int] = None
    sum_other_doc_count: Optional[int] = None


class BucketSchema(BaseModel):
    """Represents a BucketSchema in the Iconik system."""
    doc_count: Optional[int] = None
    key: Optional[str] = None


class AutomationInternalSchema(BaseModel):
    """Represents a AutomationInternalSchema in the Iconik system."""
    actions: List[Any]
    conditions: Optional[List['Condition']] = Field(default_factory=list)
    created_by: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    modified_by: Optional[UUID] = None
    name: str
    status: Optional[Literal['ACTIVE', 'INACTIVE']] = None
    system_domain_id: Optional[UUID] = None
    triggers: List['Trigger']


class AutomationHistorySchema(BaseModel):
    """Represents a AutomationHistorySchema in the Iconik system."""
    automation_id: UUID
    date_executed: Optional[datetime] = None
    error_message: Optional[str] = None
    job_id: Optional[UUID] = None
    object_id: UUID
    object_type: str
    status: Literal['SUCCEED', 'FAILED']
    system_domain_id: UUID
    version_id: UUID


class AssetTransferredToStorageTriggerSchema(BaseModel):
    """Represents a AssetTransferredToStorageTriggerSchema in the Iconik system."""
    parameters: 'AssetTransferredToStorageParameters'
    type: Literal['TRANSFER_TO_STORAGE']


class AssetTransferredToStorageParameters(BaseModel):
    """Represents a AssetTransferredToStorageParameters in the Iconik system."""
    storage_id: UUID


class AssetSharedTriggerSchema(BaseModel):
    """Represents a AssetSharedTriggerSchema in the Iconik system."""
    parameters: 'AssetSharedTriggerParameters'
    type: Literal['ASSET_SHARE']


class AssetSharedTriggerParameters(BaseModel):
    """Represents a AssetSharedTriggerParameters in the Iconik system."""
    allow_download: Optional[bool] = None


class AssetRestoredTriggerSchema(BaseModel):
    """Represents a AssetRestoredTriggerSchema in the Iconik system."""
    parameters: 'AssetRestoredTriggerParameters'
    type: Literal['RESTORE']


class AssetRestoredTriggerParameters(BaseModel):
    """Represents a AssetRestoredTriggerParameters in the Iconik system."""
    storage_id: Optional[UUID] = None


class AssetOnlineTriggerSchema(BaseModel):
    """Represents a AssetOnlineTriggerSchema in the Iconik system."""
    parameters: 'AssetOnlineTriggerParameters'
    type: Literal['ASSET_ONLINE']


class AssetOnlineTriggerParameters(BaseModel):
    """Represents a AssetOnlineTriggerParameters in the Iconik system."""
    only_first_version: bool
    wait_for_transcode: bool


class AssetArchivedTriggerSchema(BaseModel):
    """Represents a AssetArchivedTriggerSchema in the Iconik system."""
    parameters: 'AssetArchivedTriggerParameters'
    type: Literal['ARCHIVE']


class Trigger(BaseModel):
    """Represents a Trigger in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    event_type: Literal['ASSETS', 'COLLECTIONS']
    execute_at: Optional[datetime] = None
    filters: Optional[List['Condition']] = Field(default_factory=list)
    object_id: Optional[UUID] = None
    operations: Optional[List[Literal['CREATE', 'UPDATE', 'DELETE', 'SHARE',
                                      'DELAYED_TRIGGER']]
                         ] = Field(default_factory=list)
    realm: Optional[Literal['ENTITY', 'METADATA', 'FORMATS', 'FILES', 'SHARES',
                            'JOBS']] = None
    type: Literal['METADATA_UPDATE', 'ASSET_SHARE', 'TRANSFER_TO_STORAGE',
                  'MODIFIED_AT_TRANSITION', 'CREATED_AT_TRANSITION', 'ARCHIVE',
                  'RESTORE', 'ASSET_ONLINE']


class Condition(BaseModel):
    """Represents a Condition in the Iconik system."""
    conditions: Optional[List['Condition']] = Field(default_factory=list)
    operator: str
    path: Optional[str] = None
    terms: Optional[List['Term']] = Field(default_factory=list)


class Term(BaseModel):
    """Represents a Term in the Iconik system."""
    exists: Optional[bool] = None
    missing: Optional[bool] = None
    name: str
    range: Optional['RangeFilter'] = None
    value: Optional[Any] = None
    value_in: Optional[List[str]] = Field(default_factory=list)


class RangeFilter(BaseModel):
    """Represents a RangeFilter in the Iconik system."""
    max: Optional[str] = None
    min: Optional[str] = None
    timezone: Optional[str] = Field(
        None, description="Format: +02:00. Results returned in UTC by default"
    )


class AssetArchivedTriggerParameters(BaseModel):
    """Represents a AssetArchivedTriggerParameters in the Iconik system."""
    storage_id: Optional[UUID] = None


class ArchiveActionSchema(BaseModel):
    """Represents a ArchiveActionSchema in the Iconik system."""
    parameters: 'ArchiveActionParameters'
    type: Literal['ARCHIVE']


class ArchiveActionParameters(BaseModel):
    """Represents a ArchiveActionParameters in the Iconik system."""
    allow_duplicate_transfers: Optional[bool] = None
    allow_host_transfer: Optional[bool] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_original: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_storage_id: UUID
    keep_collection_structure: Optional[bool] = None
    preferred_original_storage_id: Optional[UUID] = None


class AnalyzeActionSchema(BaseModel):
    """Represents a AnalyzeActionSchema in the Iconik system."""
    parameters: 'AnalyzeActionParameters'
    type: Literal['ANALYZE']


class AnalyzeActionParameters(BaseModel):
    """Represents a AnalyzeActionParameters in the Iconik system."""
    force: Optional[bool] = None
    force_type: Optional[Literal['OVERWRITE', 'APPEND']] = None


class AddToCollectionActionSchema(BaseModel):
    """Represents a AddToCollectionActionSchema in the Iconik system."""
    parameters: 'AddToCollectionActionParameters'
    type: Literal['ADD_TO_COLLECTION']


class AddToCollectionActionParameters(BaseModel):
    """Represents a AddToCollectionActionParameters in the Iconik system."""
    collection_id: UUID
    index_immediately: Optional[bool] = None


class ACLUpdateSchema(BaseModel):
    """Represents a ACLUpdateSchema in the Iconik system."""
    group_ids: Optional[List[UUID]] = Field(default_factory=list)
    mode: Literal['APPEND', 'OVERWRITE']
    permissions: List[Literal['read', 'delete', 'change-acl', 'write']]
    user_ids: Optional[List[UUID]] = Field(default_factory=list)


# Update forward references
_TriggerSchemaBase.model_rebuild()
_ObjectCollectionTriggerParametersSchema.model_rebuild()
_ActionSchemaBase.model_rebuild()
UpdateACLActionSchema.model_rebuild()
UpdateACLAction.model_rebuild()
UpdateACLActionParameters.model_rebuild()
TriggersSchema.model_rebuild()
TriggerSchema.model_rebuild()
TriggerCustomActionSchema.model_rebuild()
TriggerCustomAction.model_rebuild()
TriggerCustomActionParameters.model_rebuild()
TransferActionSchema.model_rebuild()
TransferActionParametersSchema.model_rebuild()
TranscribeActionSchema.model_rebuild()
TranscribeAction.model_rebuild()
TranscribeActionParameters.model_rebuild()
TranscodeActionSchema.model_rebuild()
TranscodeActionParametersSchema.model_rebuild()
TranscodeAction.model_rebuild()
TranscodeActionParameters.model_rebuild()
TermSchema.model_rebuild()
SubtitleAddedTriggerSchema.model_rebuild()
SubtitleAddedTrigger.model_rebuild()
SubtitleAddedTriggerParameters.model_rebuild()
ReviewStatusChangedTriggerSchema.model_rebuild()
ReviewStatusChangedTrigger.model_rebuild()
ReviewStatusChangedTriggerParameters.model_rebuild()
RestrictAssetActionSchema.model_rebuild()
RestrictAssetAction.model_rebuild()
RestrictAssetActionParameters.model_rebuild()
RestoreActionSchema.model_rebuild()
RestoreAction.model_rebuild()
RestoreActionParameters.model_rebuild()
RequestReviewActionSchema.model_rebuild()
RequestReviewAction.model_rebuild()
RequestReviewActionParameters.model_rebuild()
RequestOriginalActionSchema.model_rebuild()
RequestOriginalAction.model_rebuild()
TransferAction.model_rebuild()
TransferActionParameters.model_rebuild()
RemoveAssetRestrictionActionSchema.model_rebuild()
RemoveAssetRestrictionAction.model_rebuild()
RemoveAssetRestrictionActionParameters.model_rebuild()
RangeFilterSchema.model_rebuild()
ObjectRemovedFromCollectionTriggerSchema.model_rebuild()
ObjectRemovedFromCollectionTrigger.model_rebuild()
ObjectAddedToCollectionTriggerSchema.model_rebuild()
ObjectAddedToCollectionTrigger.model_rebuild()
_ObjectCollectionTriggerParameters.model_rebuild()
ModifiedAtTransitionTriggerSchema.model_rebuild()
ModifiedAtTransitionTrigger.model_rebuild()
ModifiedAtTransitionTriggerParameters.model_rebuild()
MetadataUpdateTriggerSchema.model_rebuild()
MetadataUpdateTrigger.model_rebuild()
MetadataUpdateTriggerParameters.model_rebuild()
MetadataUpdateActionSchema.model_rebuild()
MetadataUpdateAction.model_rebuild()
MetadataUpdateActionParameters.model_rebuild()
MetadataFieldValueUpdateSchema.model_rebuild()
MetadataFieldValueSchema.model_rebuild()
ListObjectsSchema.model_rebuild()
ExportActionSchema.model_rebuild()
ExportAction.model_rebuild()
ExportActionParameters.model_rebuild()
DeleteActionSchema.model_rebuild()
DeleteAction.model_rebuild()
CreatedAtTransitionTriggerSchema.model_rebuild()
CreatedAtTransitionTrigger.model_rebuild()
CreatedAtTransitionTriggerParameters.model_rebuild()
CreateShareActionSchema.model_rebuild()
CreateShareActionParametersSchema.model_rebuild()
CreateShareAction.model_rebuild()
CreateShareActionParameters.model_rebuild()
ConditionSchema.model_rebuild()
AutomationsSchema.model_rebuild()
AutomationsInternalSchema.model_rebuild()
AutomationStatsSchema.model_rebuild()
AutomationStatsObjectSchema.model_rebuild()
AutomationSchema.model_rebuild()
AutomationRunEstimateSchema.model_rebuild()
FacetSchema.model_rebuild()
BucketSchema.model_rebuild()
AutomationInternalSchema.model_rebuild()
AutomationHistorySchema.model_rebuild()
AssetTransferredToStorageTriggerSchema.model_rebuild()
AssetTransferredToStorageParameters.model_rebuild()
AssetSharedTriggerSchema.model_rebuild()
AssetSharedTriggerParameters.model_rebuild()
AssetRestoredTriggerSchema.model_rebuild()
AssetRestoredTriggerParameters.model_rebuild()
AssetOnlineTriggerSchema.model_rebuild()
AssetOnlineTriggerParameters.model_rebuild()
AssetArchivedTriggerSchema.model_rebuild()
Trigger.model_rebuild()
Condition.model_rebuild()
Term.model_rebuild()
RangeFilter.model_rebuild()
AssetArchivedTriggerParameters.model_rebuild()
ArchiveActionSchema.model_rebuild()
ArchiveActionParameters.model_rebuild()
AnalyzeActionSchema.model_rebuild()
AnalyzeActionParameters.model_rebuild()
AddToCollectionActionSchema.model_rebuild()
AddToCollectionActionParameters.model_rebuild()
ACLUpdateSchema.model_rebuild()
