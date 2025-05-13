"""
Iconik Files Models
This module contains Pydantic models for the Iconik Files API.
"""
from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field, HttpUrl


class ZencoderSettingsSchema(BaseModel):
    """Represents a ZencoderSettingsSchema in the Iconik system."""
    api_key: str
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=10)


class WildmokaSettingsSchema(BaseModel):
    """Represents a WildmokaSettingsSchema in the Iconik system."""
    audio_bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    scaling_method: Optional[Literal['fast_bilinear', 'bilinear', 'bicubic',
                                     'experimental', 'neighbor', 'area',
                                     'bicublin', 'gauss', 'sinc', 'lanczos',
                                     'spline', 'accurate_rnd',
                                     'full_chroma_int', 'full_chroma_inp',
                                     'bitexact']] = None
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class WatchFolderVideoTranscoderSchema(BaseModel):
    """Represents a WatchFolderVideoTranscoderSchema in the Iconik system."""
    create_web_proxy_from_edit_proxy: Optional[bool] = None
    edit_proxy_local_storage_path: Optional[str] = None
    edit_proxy_upload_storage_id: Optional[str] = None
    edit_proxy_upload_storage_path: Optional[str] = None
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    file_grow_threshold: int = Field(..., ge=5)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    keep_as_edit_proxy: Optional[bool] = None
    keyframe_folder_name: str
    keyframe_map_folder_name: str
    local: Optional[bool] = None
    proxy_folder_name: str
    proxy_timeout: Optional[int] = Field(None, ge=10, le=86400)
    use_symlink: Optional[bool] = Field(
        None,
        description=
        "If enabled a soft link is used to add original to the watch folder, if disabled a hard link is used with a fallback to copy."
    )
    use_unique_sub_folder_workflow: Optional[bool] = Field(
        None,
        description=
        "A sub-folder is created with a unique name inside the watch folder per job."
    )
    watch_folder_location: str


class VantageSettingsSchema(BaseModel):
    """Represents a VantageSettingsSchema in the Iconik system."""
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    host: str
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    port: int = Field(..., ge=-2147483648, le=2147483647)
    priority: Optional[int] = Field(None, ge=1, le=10)
    share_name: str
    temp_proxy_folder: str
    workflow_id: str


class UploadIconikStorageGatewayLogsSchema(BaseModel):
    """Represents a UploadIconikStorageGatewayLogsSchema in the Iconik system."""
    filename: str = Field(..., max_length=100)


class UploadFilesSchema(BaseModel):
    """Represents a UploadFilesSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    asset_title: Optional[str] = None
    collection_id: Optional[UUID] = None
    create_keyframes: Optional[bool] = None
    file_name: str
    format_metadata: Optional[List[Dict[str,
                                        Any]]] = Field(default_factory=list)
    format_name: Optional[str] = None
    storage_id: UUID
    version_id: Optional[UUID] = None


class TransfersToStorageSchema(BaseModel):
    """Represents a TransfersToStorageSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['TransferToStorageReadSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class TransfersFromStorageSchema(BaseModel):
    """Represents a TransfersFromStorageSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['TransferFromStorageReadSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class TransferToStorageSchema(BaseModel):
    """Represents a TransferToStorageSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    asset_paths: Optional[List[str]] = Field(default_factory=list)
    collection_storage_id: Optional[UUID] = None
    component_ids: Optional[List[UUID]] = Field(default_factory=list)
    delete_only_from_source_folder: Optional[bool] = None
    delete_remote_file_set_after_download: Optional[bool] = None
    delete_source_file_set_after_download: Optional[bool] = None
    destination_base_directory: Optional[str] = None
    destination_directory_path: str
    destination_file_set_name: str
    destination_filename: Optional[str] = None
    file_set_id: Optional[UUID] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    job_id: Optional[UUID] = None
    job_steps: Optional[Dict[str, Any]] = Field(default_factory=dict)
    local_storage_id: Optional[UUID] = None
    original_storage_id: Optional[UUID] = None
    original_url: Optional[HttpUrl] = None
    parent_job_id: Optional[UUID] = None
    temporary_file_set_source: Optional[bool] = None
    transfer_type: Optional[str] = None


class TransferToStorageReadSchema(BaseModel):
    """Represents a TransferToStorageReadSchema in the Iconik system."""
    add_file_set: Optional[bool] = None
    asset_id: Optional[UUID] = None
    asset_paths: Optional[List[str]] = Field(default_factory=list)
    collection_storage_id: Optional[UUID] = None
    component_ids: Optional[List[UUID]] = Field(default_factory=list)
    delete_only_from_source_folder: Optional[bool] = None
    delete_remote_file_set_after_download: Optional[bool] = None
    delete_source_file_set_after_download: Optional[bool] = None
    destination_base_directory: Optional[str] = None
    destination_directory_path: str
    destination_file_set_name: str
    destination_filename: Optional[str] = None
    export_metadata_format: Optional[str] = None
    export_metadata_view: Optional[UUID] = None
    export_original: Optional[bool] = None
    export_posters: Optional[bool] = None
    export_proxy: Optional[bool] = None
    export_transcription_format: Optional[str] = None
    file_set_id: Optional[UUID] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    include_original_extension: Optional[bool] = None
    job_id: Optional[UUID] = None
    job_steps: Optional[Dict[str, Any]] = Field(default_factory=dict)
    local_storage_id: Optional[UUID] = None
    original_storage_id: Optional[UUID] = None
    original_url: Optional[HttpUrl] = None
    overwrite: Optional[bool] = None
    parent_job_id: Optional[UUID] = None
    temporary_file_set_source: Optional[bool] = None
    transfer_type: Optional[str] = None


class TransferSignedURLSchema(BaseModel):
    """Represents a TransferSignedURLSchema in the Iconik system."""
    url: Optional[HttpUrl] = None


class TransferFromStorageSchema(BaseModel):
    """Represents a TransferFromStorageSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    asset_paths: Optional[List[str]] = Field(default_factory=list)
    collection_storage_id: Optional[UUID] = None
    component_ids: Optional[List[UUID]] = Field(default_factory=list)
    delete_local_file_set_after_upload: Optional[bool] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_source_file_set_after_download: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_file_set_name: Optional[str] = None
    destination_filename: Optional[str] = None
    destination_storage_id: Optional[UUID] = None
    destination_storage_method: Optional[str] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    job_id: Optional[UUID] = None
    job_steps: Optional[Dict[str, Any]] = Field(default_factory=dict)
    original_file_set_id: Optional[UUID] = None
    original_storage_id: Optional[UUID] = None
    original_url: Optional[HttpUrl] = None
    parent_job_id: Optional[UUID] = None
    temporary_file_set_source: Optional[bool] = None
    transfer_type: Optional[str] = None


class TransferFromStorageReadSchema(BaseModel):
    """Represents a TransferFromStorageReadSchema in the Iconik system."""
    add_file_set: Optional[bool] = None
    asset_id: Optional[UUID] = None
    asset_paths: Optional[List[str]] = Field(default_factory=list)
    collection_storage_id: Optional[UUID] = None
    component_ids: Optional[List[UUID]] = Field(default_factory=list)
    delete_local_file_set_after_upload: Optional[bool] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_source_file_set_after_download: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_file_set_name: Optional[str] = None
    destination_filename: Optional[str] = None
    destination_storage_id: Optional[UUID] = None
    destination_storage_method: Optional[str] = None
    export_metadata_format: Optional[str] = None
    export_metadata_view: Optional[UUID] = None
    export_original: Optional[bool] = None
    export_posters: Optional[bool] = None
    export_proxy: Optional[bool] = None
    export_transcription_format: Optional[str] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    include_original_extension: Optional[bool] = None
    job_id: Optional[UUID] = None
    job_steps: Optional[Dict[str, Any]] = Field(default_factory=dict)
    original_file_set_id: Optional[UUID] = None
    original_storage_id: Optional[UUID] = None
    original_url: Optional[HttpUrl] = None
    overwrite: Optional[bool] = None
    parent_job_id: Optional[UUID] = None
    temporary_file_set_source: Optional[bool] = None
    transfer_type: Optional[str] = None


class TransferCloudSchema(BaseModel):
    """Represents a TransferCloudSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    asset_paths: Optional[List[str]] = Field(default_factory=list)
    celery_task_id: Optional[UUID] = None
    collection_storage_id: Optional[UUID] = None
    component_ids: Optional[List[UUID]] = Field(default_factory=list)
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_original: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_filename: Optional[str] = None
    destination_storage_id: Optional[UUID] = None
    id: Optional[UUID] = None
    job_id: Optional[UUID] = None
    job_steps: Optional[Dict[str, Any]] = Field(default_factory=dict)
    original_file_set_id: Optional[UUID] = None
    original_storage_id: Optional[UUID] = None
    original_url: Optional[HttpUrl] = None
    parent_job_id: Optional[UUID] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    status: Optional[Literal['Q', 'U', 'E', 'D']] = None
    success: Optional[str] = None
    transfer_type: Optional[UUID] = None
    user_id: Optional[UUID] = None


class TranscodersSchema(BaseModel):
    """Represents a TranscodersSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['TranscoderReadSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class TranscodersQueryParamsSchema(BaseModel):
    """Represents a TranscodersQueryParamsSchema in the Iconik system."""
    page: Optional[int] = Field(
        None, ge=1, le=10000, description="Which page number to fetch"
    )
    per_page: Optional[int] = Field(
        None, ge=0, le=1000, description="The number of items for each page"
    )
    sort: Optional[str] = Field(
        None,
        description="A comma separated list of fieldnames with order (asc/desc)"
    )


class TranscodersByStorageSchema(BaseModel):
    """Represents a TranscodersByStorageSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['TranscoderByStorageReadSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class TranscoderSchema(BaseModel):
    """Represents a TranscoderSchema in the Iconik system."""
    id: Optional[UUID] = None
    name: str
    settings: Dict[str, Any]
    type: Literal['VANTAGE', 'FFMPEG', 'EDIT_PROXY', 'IMAGEMAGICK',
                  'ENCODING_COM', 'ZENCODER', 'TELESTREAM_CLOUD',
                  'ELEMENTAL_MEDIACONVERT', 'ELEMENTAL_SERVER', 'REDLINE',
                  'ICONIK_EDGE_TRANSCODER', 'WATCH_FOLDER_VIDEO', 'EDITREADY',
                  'FLICS', 'WILDMOKA']


class TranscoderReadSchema(BaseModel):
    """Represents a TranscoderReadSchema in the Iconik system."""
    id: Optional[UUID] = None
    name: str
    settings: Dict[str, Any]
    type: Literal['VANTAGE', 'FFMPEG', 'EDIT_PROXY', 'IMAGEMAGICK',
                  'ENCODING_COM', 'ZENCODER', 'TELESTREAM_CLOUD',
                  'ELEMENTAL_MEDIACONVERT', 'ELEMENTAL_SERVER', 'REDLINE',
                  'ICONIK_EDGE_TRANSCODER', 'WATCH_FOLDER_VIDEO', 'EDITREADY',
                  'FLICS', 'WILDMOKA']


class TranscoderByStorageReadSchema(BaseModel):
    """Represents a TranscoderByStorageReadSchema in the Iconik system."""
    id: Optional[UUID] = None
    name: Optional[str] = None
    settings: Optional[Dict[str, Any]] = Field(default_factory=dict)
    storage_id: Optional[UUID] = None
    type: Optional[Literal['VANTAGE', 'FFMPEG', 'EDIT_PROXY', 'IMAGEMAGICK',
                           'ENCODING_COM', 'ZENCODER', 'TELESTREAM_CLOUD',
                           'ELEMENTAL_MEDIACONVERT', 'ELEMENTAL_SERVER',
                           'REDLINE', 'ICONIK_EDGE_TRANSCODER',
                           'WATCH_FOLDER_VIDEO', 'EDITREADY', 'FLICS',
                           'WILDMOKA']] = None


class TranscoderBaseSchema(BaseModel):
    """Represents a TranscoderBaseSchema in the Iconik system."""


class TranscodeResponseSchema(BaseModel):
    """Represents a TranscodeResponseSchema in the Iconik system."""
    job_id: Optional[UUID] = None


class TranscodeRequestSchema(BaseModel):
    """Represents a TranscodeRequestSchema in the Iconik system."""
    priority: Optional[int] = Field(None, ge=1, le=10)
    set_as_custom_keyframe: Optional[bool] = None
    update_proxy_mediainfo: Optional[bool] = None
    use_storage_transcode_ignore_pattern: Optional[bool] = None


class TimeCodeTypeSchema(BaseModel):
    """Represents a TimeCodeTypeSchema in the Iconik system."""
    frames_number: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    is_drop_frame: Optional[bool] = None
    time_base: Optional['TimeBaseTypeSchema'] = None


class TimeBaseTypeSchema(BaseModel):
    """Represents a TimeBaseTypeSchema in the Iconik system."""
    denominator: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    numerator: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class TemporaryFileSetSchema(BaseModel):
    """Represents a TemporaryFileSetSchema in the Iconik system."""
    archive_file_set_id: Optional[UUID] = None
    asset_id: Optional[UUID] = None
    base_dir: str
    component_ids: List[UUID]
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    file_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    format_id: UUID
    id: Optional[UUID] = None
    is_archive: Optional[bool] = None
    job_id: UUID
    name: str
    original_storage_id: Optional[UUID] = None
    status: Optional[Literal['ACTIVE', 'ARCHIVED', 'DELETED']] = None
    storage_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class TemporaryFileCreateSchema(BaseModel):
    """Represents a TemporaryFileCreateSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    checksum: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    directory_path: str
    file_date_created: Optional[datetime] = None
    file_date_modified: Optional[datetime] = None
    file_set_id: Optional[UUID] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    multipart_upload_url: Optional[str] = None
    name: Optional[str] = Field(
        None,
        description=
        "If not specified, name will be autogenerated based on `id` and `original_name`"
    )
    original_name: str
    parent_id: Optional[UUID] = None
    path_exist: Optional[bool] = None
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    storage_method: Optional[str] = None
    type: Literal['FILE', 'DIRECTORY', 'SYMLINK']
    upload_credentials: Optional[Dict[str, Any]] = Field(default_factory=dict)
    upload_filename: Optional[str] = None
    upload_method: Optional[str] = None
    upload_url: Optional[str] = None
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class TelestreamCloudSchema(BaseModel):
    """Represents a TelestreamCloudSchema in the Iconik system."""
    access_key: str
    api_host: Optional[str] = None
    api_port: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    factory_id: str
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    keyframes_profile_id: str
    local: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    proxy_profile_id: str
    secret_key: str
    storage_id: str


class SubtitlesSchema(BaseModel):
    """Represents a SubtitlesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['Subtitle']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class SubtitleSchema(BaseModel):
    """Represents a SubtitleSchema in the Iconik system."""
    asset_id: UUID
    closed_captions: bool
    content: Optional[str] = None
    format_id: UUID
    id: UUID
    language: str
    name: Optional[str] = None
    version_id: Optional[UUID] = None


class SubtitleRequestSchema(BaseModel):
    """Represents a SubtitleRequestSchema in the Iconik system."""
    create_transcription: Optional[bool] = None
    delete_old_transcriptions: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=10)


class Subtitle(BaseModel):
    """Represents a Subtitle in the Iconik system."""
    asset_id: UUID
    closed_captions: bool
    format_id: UUID
    id: UUID
    language: str
    name: Optional[str] = None
    version_id: Optional[UUID] = None


class StoragesReadSchema(BaseModel):
    """Represents a StoragesReadSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['StorageReadSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class StoragesQueryParamsSchema(BaseModel):
    """Represents a StoragesQueryParamsSchema in the Iconik system."""
    page: Optional[int] = Field(
        None, ge=1, le=10000, description="Which page number to fetch"
    )
    per_page: Optional[int] = Field(
        None, ge=0, le=1000, description="The number of items for each page"
    )
    sort: Optional[str] = Field(
        None,
        description="A comma separated list of fieldnames with order (asc/desc)"
    )


class StorageValidationSchema(BaseModel):
    """Represents a StorageValidationSchema in the Iconik system."""
    method: Literal['FILE', 'HTTP', 'FTP', 'SFTP', 'S3', 'B2', 'GCS', 'PORTAL',
                    'CUSTOM', 'AZURE']
    settings: Dict[str, Any]


class StorageScanSchema(BaseModel):
    """Represents a StorageScanSchema in the Iconik system."""
    files: Optional[List[str]] = Field(default_factory=list)
    ignore_already_active: Optional[bool] = Field(
        None,
        description=
        "Will force scanning even if the scan is already active if any of `paths` or `files` are specified."
    )
    paths: Optional[List[str]] = Field(default_factory=list)


class StorageReadSchema(BaseModel):
    """Represents a StorageReadSchema in the Iconik system."""
    default: Optional[bool] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    isg_version: Optional[str] = None
    last_scanned: Optional[datetime] = None
    method: Literal['FILE', 'HTTP', 'FTP', 'SFTP', 'S3', 'B2', 'GCS', 'PORTAL',
                    'CUSTOM', 'AZURE']
    name: str
    purpose: Literal['KEYFRAMES', 'FILES', 'PROXIES', 'EXPORTS', 'ARCHIVE',
                     'FACES']
    scanner_status: Optional[str] = None
    settings: Dict[str, Any]
    status: Optional[Literal['ACTIVE', 'INACTIVE', 'FAILING']] = None
    status_message: Optional[str] = None
    version: Optional[str] = None


class StoragePrivateDataSchema(BaseModel):
    """Represents a StoragePrivateDataSchema in the Iconik system."""
    bucket_location: Optional[str] = None
    default: Optional[bool] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    last_scanned: Optional[datetime] = None
    method: Literal['FILE', 'HTTP', 'FTP', 'SFTP', 'S3', 'B2', 'GCS', 'PORTAL',
                    'CUSTOM', 'AZURE']
    name: str
    purpose: Literal['KEYFRAMES', 'FILES', 'PROXIES', 'EXPORTS', 'ARCHIVE',
                     'FACES']
    scanner_status: Optional[str] = None
    settings: Dict[str, Any]
    status: Optional[Literal['ACTIVE', 'INACTIVE', 'FAILING']] = None
    status_message: Optional[str] = None
    version: Optional[str] = None


class StoragePermissionsSchema(BaseModel):
    """Represents a StoragePermissionsSchema in the Iconik system."""
    method: Literal['FILE', 'HTTP', 'FTP', 'SFTP', 'S3', 'B2', 'GCS', 'PORTAL',
                    'CUSTOM', 'AZURE']
    purpose: Literal['KEYFRAMES', 'FILES', 'PROXIES', 'EXPORTS', 'ARCHIVE',
                     'FACES']
    settings: Dict[str, Any]


class StorageFilesQueryParamsSchema(BaseModel):
    """Represents a StorageFilesQueryParamsSchema in the Iconik system."""
    include_parent_statuses: Optional[bool] = None
    page: Optional[int] = Field(
        None, ge=1, le=10000, description="Which page number to fetch"
    )
    per_page: Optional[int] = Field(
        None, ge=0, le=1000, description="The number of items for each page"
    )
    scroll: Optional[bool] = None
    scroll_id: Optional[UUID] = None
    sort: Optional[str] = Field(
        None,
        description="A comma separated list of fieldnames with order (asc/desc)"
    )


class StorageFilesDeleteBulkSchema(BaseModel):
    """Represents a StorageFilesDeleteBulkSchema in the Iconik system."""
    object_ids: List[UUID]
    object_type: str


class StorageFileUpdateSchema(BaseModel):
    """Represents a StorageFileUpdateSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    checksum: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    directory_path: str
    file_date_created: Optional[datetime] = None
    file_date_modified: Optional[datetime] = None
    file_set_id: Optional[UUID] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    name: str
    original_name: Optional[str] = None
    parent_id: Optional[UUID] = None
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    type: Optional[Literal['FILE', 'DIRECTORY', 'SYMLINK']] = None
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class StorageFileSchema(BaseModel):
    """Represents a StorageFileSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    checksum: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    destination_storage_id: Optional[UUID] = None
    directory_path: str
    file_date_created: Optional[datetime] = None
    file_date_modified: Optional[datetime] = None
    file_set_id: Optional[UUID] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    name: Optional[str] = Field(
        None,
        description=
        "If not specified, name will be autogenerated based on `id` and `original_name`"
    )
    original_name: str
    parent_id: Optional[UUID] = None
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = Field(
        None,
        description="Deprecated field. Use destination_storage_id instead"
    )
    type: Literal['FILE', 'DIRECTORY', 'SYMLINK']
    url: Optional[str] = None
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class StorageBaseSchema(BaseModel):
    """Represents a StorageBaseSchema in the Iconik system."""


class StorageAutoScanSchema(BaseModel):
    """Represents a StorageAutoScanSchema in the Iconik system."""
    hours_interval: Optional[int] = Field(None, ge=1)


class StorageAccessSchema(BaseModel):
    """Represents a StorageAccessSchema in the Iconik system."""
    method: Literal['FILE', 'HTTP', 'FTP', 'SFTP', 'S3', 'B2', 'GCS', 'PORTAL',
                    'CUSTOM', 'AZURE']
    settings: Dict[str, Any]


class SftpSettingsSchema(BaseModel):
    """Represents a SftpSettingsSchema in the Iconik system."""
    address: str
    delete: Optional[bool] = None
    is_system: Optional[bool] = None
    password: str
    read: Optional[bool] = None
    scan: Optional[bool] = None
    user: str
    write: Optional[bool] = None


class S3SettingsSchema(BaseModel):
    """Represents a S3SettingsSchema in the Iconik system."""
    access_group_id: Optional[UUID] = None
    access_key: Optional[str] = None
    acl_template_id: Optional[UUID] = None
    add_uuid_to_filenames: Optional[bool] = None
    aggregate_identical_files: Optional[bool] = None
    aggregate_ignore: Optional[List[str]] = Field(default_factory=list)
    aggregate_only_on_same_storage: Optional[bool] = None
    bucket: str
    delete: Optional[bool] = None
    enable_collection_directory_mapping: Optional[bool] = None
    endpoint: str
    filename_is_external_id: Optional[bool] = None
    folder_name_tags_metadata_field_name: Optional[str] = None
    folder_name_tags_metadata_view_id: Optional[UUID] = None
    glacier_restore_timeout: Optional[int] = Field(
        None,
        ge=-2147483648,
        le=2147483647,
        description=
        "Keep restored assets online for this many days to allow them to be copied before going back to Glacier"
    )
    is_system: Optional[bool] = None
    metadata_conversion_url: Optional[str] = None
    metadata_conversion_url_headers: Optional[str] = None
    metadata_view_id: Optional[UUID] = None
    notification_sqs_url: Optional[str] = None
    path: str
    preload_edge_jobs: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    presign_md5_checksum: Optional[bool] = None
    read: Optional[bool] = None
    region: str
    root_collection_id: Optional[UUID] = None
    scan: Optional[bool] = None
    scan_directories: Optional[List[str]] = Field(default_factory=list)
    scan_ignore: Optional[List[str]] = Field(default_factory=list)
    secret_key: Optional[str] = None
    session_token: Optional[str] = None
    sidecar_metadata_required: Optional[bool] = None
    title_includes_extension: Optional[bool] = None
    transcode_ignore: Optional[List[str]] = Field(default_factory=list)
    use_acceleration: Optional[bool] = None
    write: Optional[bool] = None


class ResolutionTypeSchema(BaseModel):
    """Represents a ResolutionTypeSchema in the Iconik system."""
    height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class ReindexTranscoderSchema(BaseModel):
    """Represents a ReindexTranscoderSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexStorageSchema(BaseModel):
    """Represents a ReindexStorageSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexFormatSchema(BaseModel):
    """Represents a ReindexFormatSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexFileSetSchema(BaseModel):
    """Represents a ReindexFileSetSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexFileSchema(BaseModel):
    """Represents a ReindexFileSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexExportLocationSchema(BaseModel):
    """Represents a ReindexExportLocationSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class RedlineSchema(BaseModel):
    """Represents a RedlineSchema in the Iconik system."""
    default_lut3d_file: Optional[str] = None
    edit_proxy_local_storage_path: Optional[str] = None
    edit_proxy_upload_storage_id: Optional[str] = None
    edit_proxy_upload_storage_path: Optional[str] = None
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    format: Optional[Literal['QT transcode', 'Apple ProRes', '']] = None
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    keep_redline_proxy: Optional[bool] = None
    local: Optional[bool] = None
    opencl_device_indexes: Optional[List[str]] = Field(default_factory=list)
    prcodec: Optional[Literal['Apple_ProRes_422_HQ', 'Apple_ProRes_422',
                              'Apple_ProRes_422_LT', 'Apple_ProRes_422_Proxy',
                              'Apple_ProRes_4444',
                              'Apple_ProRes_4444_XQ']] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    qt_codec: Optional[Literal['H264', 'H263', 'AVID_1080P_DNxHD_36_8-bit',
                               'AVID_1080P_DNxHD_115/120_8-bit',
                               'AVID_1080P_DNxHD_175/185_8-bit',
                               'AVID_1080P_DNxHD_175/185_10-bit',
                               'AVID_720P_DNxHD_60/75_8-bit',
                               'AVID_720P_DNxHD_90/110_8-bit',
                               'AVID_720P_DNxHD_90/110_10-bit',
                               'AVID_720P_DNxHD_120/145_8-bit',
                               'AVID_720P_DNxHD_185/220_8-bit',
                               'AVID_720P_DNxHD_185/220_10-bit',
                               'Apple_ProRes_422_HQ', 'Apple_ProRes_422',
                               'Apple_ProRes_4444', 'Apple_ProRes_422_LT',
                               'Apple_ProRes_422_Proxy', '']] = None
    render_resolution: Optional[int] = Field(None, ge=1, le=8)
    use_metadata_cube_file_in_proxy: Optional[bool] = None
    use_rmd: Optional[int] = Field(None, ge=1, le=2)


class ProxyUpdateSchema(BaseModel):
    """Represents a ProxyUpdateSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    audio_bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    bit_rate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    codec: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    frame_rate: Optional[str] = None
    id: Optional[UUID] = None
    is_drop_frame: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    start_time_code: Optional[str] = None
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    url: Optional[str] = None
    version_id: Optional[UUID] = None


class ProxySchema(BaseModel):
    """Represents a ProxySchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    audio_bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    bit_rate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    codec: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    frame_rate: Optional[str] = None
    id: Optional[UUID] = None
    is_drop_frame: Optional[bool] = None
    is_public: Optional[bool] = None
    multipart_upload_url: Optional[str] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    start_time_code: Optional[str] = None
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    storage_method: Optional[str] = None
    upload_credentials: Optional[Dict[str, Any]] = Field(default_factory=dict)
    upload_method: Optional[str] = None
    upload_url: Optional[str] = None
    url: Optional[str] = None
    version_id: Optional[UUID] = None


class ProxyDownloadURLSchema(BaseModel):
    """Represents a ProxyDownloadURLSchema in the Iconik system."""
    url: Optional[str] = None


class ProxyCreateSchema(BaseModel):
    """Represents a ProxyCreateSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    audio_bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    bit_rate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    codec: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    frame_rate: Optional[str] = None
    id: Optional[UUID] = None
    is_drop_frame: Optional[bool] = None
    is_public: Optional[bool] = None
    multipart_upload_url: Optional[str] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    start_time_code: Optional[str] = None
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    storage_method: Optional[str] = None
    upload_credentials: Optional[Dict[str, Any]] = Field(default_factory=dict)
    upload_method: Optional[str] = None
    upload_url: Optional[str] = None
    url: Optional[str] = None
    version_id: Optional[UUID] = None


class ProxyBaseSchema(BaseModel):
    """Represents a ProxyBaseSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    audio_bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    bit_rate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    codec: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    frame_rate: Optional[str] = None
    id: Optional[UUID] = None
    is_drop_frame: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    start_time_code: Optional[str] = None
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    url: Optional[str] = None
    version_id: Optional[UUID] = None


class ProxiesSchema(BaseModel):
    """Represents a ProxiesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['Proxy']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class PrioDirSchema(BaseModel):
    """Represents a PrioDirSchema in the Iconik system."""
    directory: Optional[str] = None
    priority: Optional[int] = None


class PortalSettingsSchema(BaseModel):
    """Represents a PortalSettingsSchema in the Iconik system."""
    delete: Optional[bool] = None
    is_system: Optional[bool] = None
    read: Optional[bool] = None
    scan: Optional[bool] = None
    write: Optional[bool] = None


class MultipartUploadSchema(BaseModel):
    """Represents a MultipartUploadSchema in the Iconik system."""
    parts_group: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    parts_range: List[str]


class MultipartUploadProxyCleanupSchema(BaseModel):
    """Represents a MultipartUploadProxyCleanupSchema in the Iconik system."""
    abort_upload: Optional[bool] = None
    upload_id: Optional[str] = None


class MultipartUploadComposeSchema(BaseModel):
    """Represents a MultipartUploadComposeSchema in the Iconik system."""
    content_type: Optional[str] = None
    parts_group: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class MultipartUploadCleanupSchema(BaseModel):
    """Represents a MultipartUploadCleanupSchema in the Iconik system."""
    abort_upload: Optional[bool] = None
    parts_group_number: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    parts_number: Optional[int] = Field(None, ge=1)
    temporary: Optional[bool] = None
    upload_id: Optional[str] = None


class MultipartB2StartUpload(BaseModel):
    """Represents a MultipartB2StartUpload in the Iconik system."""
    authorization_token: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[str] = None
    status: Optional[str] = None
    upload_file_id: Optional[str] = None
    upload_url: Optional[str] = None


class MultipartB2FinishUpload(BaseModel):
    """Represents a MultipartB2FinishUpload in the Iconik system."""
    sha1_list: List[str]
    upload_file_id: str


class MultipartB2CancelUpload(BaseModel):
    """Represents a MultipartB2CancelUpload in the Iconik system."""
    upload_file_id: str


class MultiPartUploadURLsSchema(BaseModel):
    """Represents a MultiPartUploadURLsSchema in the Iconik system."""
    objects: Optional[List['MultiPartUploadURLSchema']
                      ] = Field(default_factory=list)


class MultiPartUploadURLSchema(BaseModel):
    """Represents a MultiPartUploadURLSchema in the Iconik system."""
    delete_url: Optional[str] = None
    download_url: Optional[str] = None
    key: Optional[str] = None
    number: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    url: Optional[str] = None


class MultiPartUploadComposeURLSchema(BaseModel):
    """Represents a MultiPartUploadComposeURLSchema in the Iconik system."""
    compose_url: Optional[str] = None
    delete_url: Optional[str] = None
    key: Optional[str] = None
    url: Optional[str] = None


class MultiPartURLsSchema(BaseModel):
    """Represents a MultiPartURLsSchema in the Iconik system."""
    abort_url: Optional[str] = None
    complete_url: Optional[str] = None
    list_parts_url: Optional[List[str]] = Field(default_factory=list)


class MultiPartS3UrlPartsSchema(BaseModel):
    """Represents a MultiPartS3UrlPartsSchema in the Iconik system."""
    parts: List['MultiPartS3UrlPartSchema']
    upload_id: str


class MultiPartS3UrlPartSchema(BaseModel):
    """Represents a MultiPartS3UrlPartSchema in the Iconik system."""
    checksum: Optional[str] = Field(
        None, description="base64-encoded md5 digest"
    )
    part_number: Optional[int] = Field(None, ge=1, le=10000)
    url: Optional[str] = None


class MoveAssetResourceSchema(BaseModel):
    """Represents a MoveAssetResourceSchema in the Iconik system."""
    destination_asset_id: UUID
    destination_version_id: UUID
    exclude_format_ids: Optional[List[str]] = Field(default_factory=list)
    source_version_id: UUID


class ListObjectsSchema(BaseModel):
    """Represents a ListObjectsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class KeyframesSchema(BaseModel):
    """Represents a KeyframesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['KeyframeSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class KeyframeUpdateSchema(BaseModel):
    """Represents a KeyframeUpdateSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    is_custom_keyframe: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    time_code: Optional['TimeCodeType'] = None
    type: Literal['KEYFRAME_MAP', 'KEYFRAME', 'POSTER']
    url: Optional[str] = None


class KeyframeCreateSchema(BaseModel):
    """Represents a KeyframeCreateSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    collection_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    id: Optional[UUID] = None
    is_custom_keyframe: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    storage_method: Optional[str] = None
    time_code: Optional['TimeCodeType'] = None
    type: Literal['KEYFRAME_MAP', 'KEYFRAME', 'POSTER']
    upload_credentials: Optional[Dict[str, Any]] = Field(default_factory=dict)
    upload_method: Optional[str] = None
    upload_url: Optional[str] = None
    url: Optional[str] = None
    version_id: Optional[UUID] = None


class KeyframeBaseSchema(BaseModel):
    """Represents a KeyframeBaseSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    is_custom_keyframe: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    time_code: Optional['TimeCodeType'] = None
    type: Literal['KEYFRAME_MAP', 'KEYFRAME', 'POSTER']
    url: Optional[str] = None


class JobsStateSchema(BaseModel):
    """Represents a JobsStateSchema in the Iconik system."""
    action: Literal['RESTART', 'ABORT']
    job_ids: List[UUID]


class JobsPrioritySchema(BaseModel):
    """Represents a JobsPrioritySchema in the Iconik system."""
    job_ids: List[UUID]
    priority: int = Field(..., ge=1, le=10)


class ImageMagickSettingsSchema(BaseModel):
    """Represents a ImageMagickSettingsSchema in the Iconik system."""
    data: Optional[str] = None
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    height: Optional[int] = Field(None, ge=1, le=16000)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    overlay_coordinates: Optional[str] = None
    overlay_url: Optional[str] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    width: Optional[int] = Field(None, ge=1, le=16000)


class IconikStorageGatewayEventsSchema(BaseModel):
    """Represents a IconikStorageGatewayEventsSchema in the Iconik system."""
    objects: Optional[List['IconikStorageGatewayEventSchema']
                      ] = Field(default_factory=list)


class IconikStorageGatewayEventsPurgeSchema(BaseModel):
    """Represents a IconikStorageGatewayEventsPurgeSchema in the Iconik system."""
    event_ids: List[UUID]


class IconikStorageGatewayEventSchema(BaseModel):
    """Represents a IconikStorageGatewayEventSchema in the Iconik system."""
    data: Optional[Dict[str, Any]] = Field(default_factory=dict)
    date_created: Optional[datetime] = None
    id: Optional[UUID] = None
    type: Literal['RESTART', 'DOWNLOAD', 'DOWNLOAD_ABORT',
                  'DOWNLOAD_CHANGE_PRIORITY', 'UPLOAD', 'UPLOAD_ABORT',
                  'UPLOAD_CHANGE_PRIORITY', 'INGEST_UPLOAD', 'DELETE',
                  'TRANSCODE', 'ASSET_MERGED', 'TRANSCODE_ABORT',
                  'TRANSCODE_CHANGE_PRIORITY', 'REQUEST_COLLECTION_MAP',
                  'ABORT_COLLECTION_MAP', 'COLLECTION_DELETED',
                  'RESET_INGEST_VALIDATION', 'SCHEDULE_CHECKSUM_CALCULATION',
                  'ABORT_JOBS_BULK', 'MARK_MISSING_OUTSIDE_SCAN_DIRS']


class IconikEdgeTranscoderSchema(BaseModel):
    """Represents a IconikEdgeTranscoderSchema in the Iconik system."""
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    max_transcoding_jobs: Optional[int] = Field(None, ge=1)
    priority: Optional[int] = Field(None, ge=1, le=10)


class ISGHandlerURLSchema(BaseModel):
    """Represents a ISGHandlerURLSchema in the Iconik system."""
    url: Optional[str] = None


class HttpSettingsSchema(BaseModel):
    """Represents a HttpSettingsSchema in the Iconik system."""
    address: str
    auto: Optional[bool] = None
    delete: Optional[bool] = None
    is_system: Optional[bool] = None
    read: Optional[bool] = None
    scan: Optional[bool] = None


class GoogleCloudStorageSettingsSchema(BaseModel):
    """Represents a GoogleCloudStorageSettingsSchema in the Iconik system."""
    access_group_id: Optional[UUID] = None
    acl_template_id: Optional[UUID] = None
    add_uuid_to_filenames: Optional[bool] = None
    aggregate_identical_files: Optional[bool] = None
    aggregate_ignore: Optional[List[str]] = Field(default_factory=list)
    aggregate_only_on_same_storage: Optional[bool] = None
    bucket: str
    delete: Optional[bool] = None
    enable_collection_directory_mapping: Optional[bool] = None
    filename_is_external_id: Optional[bool] = None
    folder_name_tags_metadata_field_name: Optional[str] = None
    folder_name_tags_metadata_view_id: Optional[UUID] = None
    is_system: Optional[bool] = None
    json_key: str
    metadata_conversion_url: Optional[str] = None
    metadata_conversion_url_headers: Optional[str] = None
    metadata_view_id: Optional[UUID] = None
    path: str
    preload_edge_jobs: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    project: str
    read: Optional[bool] = None
    root_collection_id: Optional[UUID] = None
    scan: Optional[bool] = None
    scan_directories: Optional[List[str]] = Field(default_factory=list)
    scan_ignore: Optional[List[str]] = Field(default_factory=list)
    sidecar_metadata_required: Optional[bool] = None
    title_includes_extension: Optional[bool] = None
    transcode_ignore: Optional[List[str]] = Field(default_factory=list)
    write: Optional[bool] = None


class GatewayStatusSchema(BaseModel):
    """Represents a GatewayStatusSchema in the Iconik system."""
    status: Optional[str] = None


class GatewayReportSchema(BaseModel):
    """Represents a GatewayReportSchema in the Iconik system."""
    await_checksum_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    date_reported: Optional[datetime] = None
    empty_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    error_log_lines: Optional[List[str]] = Field(default_factory=list)
    exported_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    faulty_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    host_info: Optional[str] = Field(None, max_length=1000)
    host_name: Optional[str] = Field(None, max_length=1000)
    id: Optional[UUID] = None
    ingested_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    ingested_files_uploads_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    ingesting_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    last_scan_time: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    log_lines: Optional[List[str]] = Field(default_factory=list)
    logs_url: Optional[str] = None
    missing_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    scanned_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    skipped_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    start_last_date: Optional[datetime] = None
    start_status: Optional[Literal['SUCCESS', 'FAILED']] = None
    start_status_message: Optional[str] = Field(None, max_length=1000)
    status: Optional[Literal['OFFLINE', 'LIVE', 'UNKNOWN']] = None
    storage_id: Optional[UUID] = None
    total_files_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    total_folders_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    version: Optional[str] = Field(None, max_length=100)
    waiting_preview_transcode_jobs_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    waiting_transcode_jobs_number: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )


class FtpSettingsSchema(BaseModel):
    """Represents a FtpSettingsSchema in the Iconik system."""
    address: str
    delete: Optional[bool] = None
    is_system: Optional[bool] = None
    password: str
    read: Optional[bool] = None
    scan: Optional[bool] = None
    user: str
    write: Optional[bool] = None


class FormatsSchema(BaseModel):
    """Represents a FormatsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['FormatSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class FormatsElasticSchema(BaseModel):
    """Represents a FormatsElasticSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['FormatElasticSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class FormatSchema(BaseModel):
    """Represents a FormatSchema in the Iconik system."""
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    asset_id: Optional[UUID] = None
    components: Optional[List['ComponentSchema']] = Field(default_factory=list)
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    id: Optional[UUID] = None
    is_online: Optional[bool] = None
    metadata: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    name: str
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    storage_methods: Optional[List[str]] = Field(default_factory=list)
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None
    warnings: Optional[List[str]] = Field(default_factory=list)


class FormatRestoreSchema(BaseModel):
    """Represents a FormatRestoreSchema in the Iconik system."""
    destination_directory_path: Optional[str] = None
    destination_storage_id: Optional[UUID] = None
    storage_id: Optional[UUID] = Field(
        None,
        description="Deprecated field. Use destination_storage_id instead"
    )


class FormatElasticSchema(BaseModel):
    """Represents a FormatElasticSchema in the Iconik system."""
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    asset_id: Optional[UUID] = None
    components: Optional[List['ComponentSchema']] = Field(default_factory=list)
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    id: Optional[UUID] = None
    is_online: Optional[bool] = None
    metadata: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    name: str
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    storage_methods: Optional[List[str]] = Field(default_factory=list)
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None
    warnings: Optional[List[str]] = Field(default_factory=list)


class FormatDeleteArchiveSchema(BaseModel):
    """Represents a FormatDeleteArchiveSchema in the Iconik system."""
    file_set_id: Optional[UUID] = None


class FormatArchiveSchema(BaseModel):
    """Represents a FormatArchiveSchema in the Iconik system."""
    delete_original: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_file_set_name: Optional[str] = None
    destination_storage_id: Optional[UUID] = None
    destination_storage_method: Optional[str] = None
    format_id: Optional[UUID] = None
    original_file_set_id: Optional[UUID] = None


class FlicsTranscoderSchema(BaseModel):
    """Represents a FlicsTranscoderSchema in the Iconik system."""
    create_edit_proxy: Optional[bool] = None
    delete_after_upload: Optional[bool] = None
    edit_proxy_local_storage_path: Optional[str] = None
    edit_proxy_upload_storage_id: Optional[str] = None
    edit_proxy_upload_storage_path: Optional[str] = None
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    host: Optional[str] = None
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    storage_id_path_mapping: Optional[Any] = None
    template_id: Optional[str] = None


class FilesetTransferBaseSchema(BaseModel):
    """Represents a FilesetTransferBaseSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    asset_paths: Optional[List[str]] = Field(default_factory=list)
    collection_storage_id: Optional[UUID] = None
    component_ids: Optional[List[UUID]] = Field(default_factory=list)
    delete_only_from_source_folder: Optional[bool] = None
    destination_filename: Optional[str] = None
    id: Optional[UUID] = None
    job_id: Optional[UUID] = None
    job_steps: Optional[Dict[str, Any]] = Field(default_factory=dict)
    original_storage_id: Optional[UUID] = None
    original_url: Optional[HttpUrl] = None
    parent_job_id: Optional[UUID] = None
    transfer_type: Optional[str] = None


class FilesSchema(BaseModel):
    """Represents a FilesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['FileSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class FilesElasticSchema(BaseModel):
    """Represents a FilesElasticSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['FileElasticSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class FileShareUploadEditSchema(BaseModel):
    """Represents a FileShareUploadEditSchema in the Iconik system."""
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None


class FileSettingsSchema(BaseModel):
    """Represents a FileSettingsSchema in the Iconik system."""
    access_group_id: Optional[UUID] = None
    acl_template_id: Optional[UUID] = None
    aggregate_identical_files: Optional[bool] = None
    aggregate_ignore: Optional[List[str]] = Field(default_factory=list)
    aggregate_only_on_same_storage: Optional[bool] = None
    allow_access_outside_scan_directories: Optional[bool] = None
    asset_versions_suffix: Optional[str] = None
    auto_version_ignore: Optional[List[str]] = Field(default_factory=list)
    auto_version_ingest_throttle_value: Optional[int] = Field(None, ge=0)
    delete: Optional[bool] = None
    directory_assets_original_patterns: Optional[List[str]] = Field(
        default_factory=list
    )
    directory_assets_transcode_patterns: Optional[List[str]] = Field(
        default_factory=list
    )
    enable_auto_versioning: Optional[bool] = None
    enable_collection_directory_mapping: Optional[bool] = None
    enable_directory_assets: Optional[bool] = None
    filename_is_external_id: Optional[bool] = None
    folder_name_tags_metadata_field_name: Optional[str] = None
    folder_name_tags_metadata_view_id: Optional[UUID] = None
    gateway_user_id: Optional[UUID] = None
    growing_files_threshold: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    is_system: Optional[bool] = None
    local_keyframe_creation: Optional[bool] = None
    local_proxy_creation: Optional[bool] = None
    metadata_conversion_url: Optional[str] = None
    metadata_conversion_url_headers: Optional[str] = None
    metadata_view_id: Optional[UUID] = None
    mount_point: str
    prio_dirs: Optional[List['PrioDir']] = Field(default_factory=list)
    public_identity: Optional[str] = None
    read: Optional[bool] = None
    remote_path: Optional[str] = None
    remote_storage_id: Optional[UUID] = None
    scan: Optional[bool] = None
    scan_directories: Optional[List[str]] = Field(default_factory=list)
    scan_ignore: Optional[List[str]] = Field(default_factory=list)
    scan_include: Optional[List[str]] = Field(default_factory=list)
    scan_interval_seconds: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    sidecar_metadata_required: Optional[bool] = None
    skip_upload_on_any_remote_copy_found: Optional[bool] = None
    storage_addr: Optional[str] = None
    title_includes_extension: Optional[bool] = None
    transcode_ignore: Optional[List[str]] = Field(default_factory=list)
    transcode_include: Optional[List[str]] = Field(default_factory=list)
    upload_files: Optional[bool] = None
    upload_ignore: Optional[List[str]] = Field(default_factory=list)
    write: Optional[bool] = None


class PrioDir(BaseModel):
    """Represents a PrioDir in the Iconik system."""
    directory: Optional[str] = None
    priority: Optional[int] = None


class FileSetsSchema(BaseModel):
    """Represents a FileSetsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['FileSetSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class FileSetsElasticSchema(BaseModel):
    """Represents a FileSetsElasticSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['FileSetElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class FileSetSourcesSchema(BaseModel):
    """Represents a FileSetSourcesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['FileSetSourceSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class FileSetSourceSchema(BaseModel):
    """Represents a FileSetSourceSchema in the Iconik system."""
    archive_file_set_id: Optional[UUID] = None
    asset_id: Optional[UUID] = None
    base_dir: str
    component_ids: List[UUID]
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    file_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    format_id: UUID
    id: Optional[UUID] = None
    is_archive: Optional[bool] = None
    name: str
    original_storage_id: Optional[UUID] = None
    status: Optional[Literal['ACTIVE', 'ARCHIVED', 'DELETED']] = None
    storage_id: UUID
    storage_method: str
    version_id: Optional[UUID] = None


class FileSetSchema(BaseModel):
    """Represents a FileSetSchema in the Iconik system."""
    archive_file_set_id: Optional[UUID] = None
    asset_id: Optional[UUID] = None
    base_dir: str
    component_ids: List[UUID]
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    file_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    format_id: UUID
    id: Optional[UUID] = None
    is_archive: Optional[bool] = None
    name: str
    original_storage_id: Optional[UUID] = None
    status: Optional[Literal['ACTIVE', 'ARCHIVED', 'DELETED']] = None
    storage_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class FileSetElasticSchema(BaseModel):
    """Represents a FileSetElasticSchema in the Iconik system."""
    archive_file_set_id: Optional[UUID] = None
    asset_id: Optional[UUID] = None
    base_dir: str
    component_ids: List[UUID]
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    file_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    format_id: UUID
    id: Optional[UUID] = None
    is_archive: Optional[bool] = None
    name: str
    original_storage_id: Optional[UUID] = None
    status: Optional[Literal['ACTIVE', 'ARCHIVED', 'DELETED']] = None
    storage_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class FileSchema(BaseModel):
    """Represents a FileSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    checksum: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    directory_path: str
    file_date_created: Optional[datetime] = None
    file_date_modified: Optional[datetime] = None
    file_set_id: UUID
    file_set_status: Optional[str] = None
    format_id: Optional[UUID] = None
    format_status: Optional[str] = None
    id: Optional[UUID] = None
    multipart_upload_url: Optional[str] = None
    name: Optional[str] = Field(
        None,
        description=
        "If not specified, name will be autogenerated based on `id` and `original_name`"
    )
    original_name: str
    parent_id: Optional[UUID] = None
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    storage_method: Optional[str] = None
    system_domain_id: Optional[UUID] = None
    type: Literal['FILE', 'DIRECTORY', 'SYMLINK']
    upload_credentials: Optional[Dict[str, Any]] = Field(default_factory=dict)
    upload_filename: Optional[str] = None
    upload_method: Optional[str] = None
    upload_url: Optional[str] = Field(
        None,
        description=
        "On a file creation for Backblaze B2 storage in case when request to Backblaze failed, upload_url field will be empty. You can try getting upload_url again by requesting created file with `generate_signed_post_url` set to true. "
    )
    url: Optional[str] = None
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class FileExistenceCheckSchema(BaseModel):
    """Represents a FileExistenceCheckSchema in the Iconik system."""
    directory_path: str
    file_name: str


class FileElasticSchema(BaseModel):
    """Represents a FileElasticSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    checksum: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    directory_path: str
    file_date_created: Optional[datetime] = None
    file_date_modified: Optional[datetime] = None
    file_set_id: Optional[UUID] = None
    file_set_status: Optional[str] = None
    format_id: Optional[UUID] = None
    format_status: Optional[str] = None
    id: Optional[UUID] = None
    name: Optional[str] = Field(
        None,
        description=
        "If not specified, name will be autogenerated based on `id` and `original_name`"
    )
    original_name: str
    parent_id: Optional[UUID] = None
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    type: Literal['FILE', 'DIRECTORY', 'SYMLINK']
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class FileDownloadURLSchema(BaseModel):
    """Represents a FileDownloadURLSchema in the Iconik system."""
    url: Optional[str] = None


class FileDeletionsSchema(BaseModel):
    """Represents a FileDeletionsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['FileDeletionFromLocalStorageSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class StorageSchema(BaseModel):
    """Represents a StorageSchema in the Iconik system."""
    default: Optional[bool] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    last_scanned: Optional[datetime] = None
    method: Literal['FILE', 'HTTP', 'FTP', 'SFTP', 'S3', 'B2', 'GCS', 'PORTAL',
                    'CUSTOM', 'AZURE']
    name: str
    purpose: Literal['KEYFRAMES', 'FILES', 'PROXIES', 'EXPORTS', 'ARCHIVE',
                     'FACES']
    scanner_status: Optional[str] = None
    settings: Dict[str, Any]
    status: Optional[Literal['ACTIVE', 'INACTIVE', 'FAILING']] = None
    status_message: Optional[str] = None
    version: Optional[str] = None


class FileDeletionFromLocalStorageSchema(BaseModel):
    """Represents a FileDeletionFromLocalStorageSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    directory_path: Optional[str] = None
    file_id: UUID
    filename: str
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    job_id: UUID
    keep_source: Optional[bool] = None
    storage_id: UUID
    version_id: Optional[UUID] = None


class FileCreateSchema(BaseModel):
    """Represents a FileCreateSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    checksum: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    directory_path: str
    file_date_created: Optional[datetime] = None
    file_date_modified: Optional[datetime] = None
    file_set_id: Optional[UUID] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    multipart_upload_url: Optional[str] = None
    name: Optional[str] = Field(
        None,
        description=
        "If not specified, name will be autogenerated based on `id` and `original_name`"
    )
    original_name: str
    parent_id: Optional[UUID] = None
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    storage_method: Optional[str] = None
    type: Literal['FILE', 'DIRECTORY', 'SYMLINK']
    upload_credentials: Optional[Dict[str, Any]] = Field(default_factory=dict)
    upload_filename: Optional[str] = None
    upload_method: Optional[str] = None
    upload_url: Optional[str] = None
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class FileBaseSchema(BaseModel):
    """Represents a FileBaseSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    checksum: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    directory_path: str
    file_date_created: Optional[datetime] = None
    file_date_modified: Optional[datetime] = None
    file_set_id: Optional[UUID] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    name: Optional[str] = Field(
        None,
        description=
        "If not specified, name will be autogenerated based on `id` and `original_name`"
    )
    original_name: str
    parent_id: Optional[UUID] = None
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    type: Literal['FILE', 'DIRECTORY', 'SYMLINK']
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class FFmpegSettingsSchema(BaseModel):
    """Represents a FFmpegSettingsSchema in the Iconik system."""
    audio_bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    data: Optional[str] = None
    edit_proxy_folder: Optional[str] = None
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    hdr_brightness: Optional[float] = Field(None, ge=-1, le=1)
    hdr_contrast: Optional[float] = Field(None, ge=0, le=2)
    hdr_gamma: Optional[float] = Field(None, ge=0, le=10)
    hdr_saturation: Optional[float] = Field(None, ge=0, le=3)
    hdr_tonemap_desat: Optional[float] = Field(None, ge=0, le=100)
    hdr_tonemap_peak: Optional[float] = Field(None, ge=0, le=1000)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    overlay_coordinates: Optional[str] = None
    overlay_url: Optional[str] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    scaling_method: Optional[Literal['fast_bilinear', 'bilinear', 'bicubic',
                                     'experimental', 'neighbor', 'area',
                                     'bicublin', 'gauss', 'sinc', 'lanczos',
                                     'spline', 'accurate_rnd',
                                     'full_chroma_int', 'full_chroma_inp',
                                     'bitexact']] = None
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class ExportLocationsSchema(BaseModel):
    """Represents a ExportLocationsSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['ExportLocationSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class ExportLocationSchema(BaseModel):
    """Represents a ExportLocationSchema in the Iconik system."""
    description: Optional[str] = None
    export_metadata: Optional[bool] = None
    export_original: Optional[bool] = None
    export_posters: Optional[bool] = None
    export_proxy: Optional[bool] = None
    export_to_asset_folder: Optional[bool] = None
    export_transcriptions: Optional[bool] = None
    id: Optional[UUID] = None
    include_original_extension: Optional[bool] = None
    metadata_format: Optional[Literal['CSV', 'JSON', 'XML']] = None
    metadata_view: Optional[UUID] = None
    name: str
    path: str
    storage_id: UUID
    system_domain_id: Optional[UUID] = None
    transcode_profile_ids: Optional[List[UUID]] = Field(default_factory=list)
    transcription_format: Optional[Literal['WEBVTT', 'SRT']] = None


class EncodingComSettingsSchema(BaseModel):
    """Represents a EncodingComSettingsSchema in the Iconik system."""
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    user_id: str
    user_key: str


class ElementalServerSchema(BaseModel):
    """Represents a ElementalServerSchema in the Iconik system."""
    api_key: str
    base_url: str
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    keyframe_map_output_group_order: Optional[int] = Field(None, ge=1)
    keyframe_output_group_order: Optional[int] = Field(None, ge=1)
    local: Optional[bool] = None
    mount_point: str
    priority: Optional[int] = Field(None, ge=1, le=10)
    profile: int = Field(..., ge=-2147483648, le=2147483647)
    proxy_output_group_order: Optional[int] = Field(None, ge=1)
    username: str


class ElementalMediaConvertSchema(BaseModel):
    """Represents a ElementalMediaConvertSchema in the Iconik system."""
    access_key: str
    edit_proxy_directory_path: Optional[str] = None
    edit_proxy_storage_id: Optional[UUID] = None
    endpoint_url: str
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    file_group_custom_name: str
    iam_role: str
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    job_template_name: str
    keyframe_storage_id: Optional[UUID] = None
    local: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    proxy_storage_id: Optional[UUID] = None
    queue_name: Optional[str] = None
    region_name: str
    s3_endpoint_url: str
    s3_region_name: Optional[str] = None
    secret_key: str
    temp_upload_path: Optional[str] = None


class EditReadyTranscoderSchema(BaseModel):
    """Represents a EditReadyTranscoderSchema in the Iconik system."""
    apply_color_conversion: Optional[bool] = None
    bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    create_edit_proxy: Optional[bool] = None
    delete_after_upload: Optional[bool] = None
    edit_proxy_height: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    edit_proxy_local_storage_path: Optional[str] = None
    edit_proxy_upload_storage_id: Optional[str] = None
    edit_proxy_upload_storage_path: Optional[str] = None
    edit_proxy_width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    editready_preset: Optional[str] = None
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    min_height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    min_width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    overwrite_edit_proxy: Optional[bool] = None
    videocodec: Optional[Literal['Apple_ProRes_422_HQ', 'Apple_ProRes_422',
                                 'Apple_ProRes_4444', 'Apple_ProRes_422_LT',
                                 'Apple_ProRes_422_Proxy']] = None
    width: int = Field(..., ge=-2147483648, le=2147483647)


class Proxy(BaseModel):
    """Represents a Proxy in the Iconik system."""
    asset_id: Optional[UUID] = None
    audio_bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    bit_rate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    codec: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    frame_rate: Optional[str] = None
    id: Optional[UUID] = None
    is_drop_frame: Optional[bool] = None
    is_public: Optional[bool] = None
    multipart_upload_url: Optional[str] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    start_time_code: Optional[str] = None
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    storage_method: Optional[str] = None
    upload_credentials: Optional[Dict[str, Any]] = Field(default_factory=dict)
    upload_method: Optional[str] = None
    upload_url: Optional[str] = None
    url: Optional[str] = None
    version_id: Optional[UUID] = None


class EditProxySettingsSchema(BaseModel):
    """Represents a EditProxySettingsSchema in the Iconik system."""
    audio_bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    audio_codec: Optional[str] = None
    bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    codec: Optional[str] = None
    data: Optional[str] = None
    delete_after_upload: Optional[bool] = None
    destination_path: Optional[str] = None
    exclude_patterns: Optional[List[str]] = Field(default_factory=list)
    height: int = Field(..., ge=-2147483648, le=2147483647)
    include_patterns: Optional[List[str]] = Field(default_factory=list)
    local: Optional[bool] = None
    local_destination_path: Optional[str] = None
    min_height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    min_width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    priority: Optional[int] = Field(None, ge=1, le=10)
    storage_id: Optional[UUID] = None
    width: int = Field(..., ge=-2147483648, le=2147483647)


class EditProxySchema(BaseModel):
    """Represents a EditProxySchema in the Iconik system."""
    allow_mxf: Optional[bool] = None
    directory_path: str
    file_suffix: Optional[str] = None
    force_storage_id: Optional[bool] = None
    height: int = Field(..., ge=-2147483648, le=2147483647)
    ignore_transcoder_settings: Optional[bool] = None
    name: str
    storage_id: UUID
    version_id: UUID
    width: int = Field(..., ge=-2147483648, le=2147483647)


class EditProxyResponseSchema(BaseModel):
    """Represents a EditProxyResponseSchema in the Iconik system."""
    audio_bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    audio_codec: Optional[str] = None
    bitrate: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    codec: Optional[str] = None
    directory_path: Optional[str] = None
    file_set_id: Optional[UUID] = None
    format_id: Optional[UUID] = None
    height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    id: Optional[UUID] = None
    name: Optional[str] = None
    transcoder_id: Optional[UUID] = None
    type: Optional[str] = None
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class DeleteQueueSchema(BaseModel):
    """Represents a DeleteQueueSchema in the Iconik system."""
    ids: List[UUID]


class DeleteQueueFormatsQueryParamsSchema(BaseModel):
    """Represents a DeleteQueueFormatsQueryParamsSchema in the Iconik system."""
    page: Optional[int] = Field(
        None, ge=1, le=10000, description="Which page number to fetch"
    )
    per_page: Optional[int] = Field(
        None, ge=0, le=1000, description="The number of items for each page"
    )
    sort: Optional[str] = Field(
        None,
        description="A comma separated list of fieldnames with order (asc/desc)"
    )


class DeleteQueueFileSetsQueryParamsSchema(BaseModel):
    """Represents a DeleteQueueFileSetsQueryParamsSchema in the Iconik system."""
    page: Optional[int] = Field(
        None, ge=1, le=10000, description="Which page number to fetch"
    )
    per_page: Optional[int] = Field(
        None, ge=0, le=1000, description="The number of items for each page"
    )
    sort: Optional[str] = Field(
        None,
        description="A comma separated list of fieldnames with order (asc/desc)"
    )


class CustomSettingsSchema(BaseModel):
    """Represents a CustomSettingsSchema in the Iconik system."""
    custom: Optional[str] = None
    delete: Optional[bool] = None
    is_system: Optional[bool] = None
    read: Optional[bool] = None
    write: Optional[bool] = None


class ComponentsSchema(BaseModel):
    """Represents a ComponentsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['ComponentSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class ComponentSchema(BaseModel):
    """Represents a ComponentSchema in the Iconik system."""
    id: Optional[UUID] = None
    metadata: Optional[Dict[str, str]] = Field(default_factory=dict)
    name: str
    type: Literal['VIDEO', 'AUDIO', 'IMAGE', 'TEXT', 'OTHER', 'NON_MEDIA',
                  'EXIF', 'IPTC', 'XMP', 'GENERAL']


class CompleteExportToLocalStorageSchema(BaseModel):
    """Represents a CompleteExportToLocalStorageSchema in the Iconik system."""
    add_file_set: Optional[bool] = None
    asset_id: Optional[UUID] = None
    asset_paths: Optional[List[str]] = Field(default_factory=list)
    collection_storage_id: Optional[UUID] = None
    component_ids: Optional[List[UUID]] = Field(default_factory=list)
    delete_only_from_source_folder: Optional[bool] = None
    delete_remote_file_set_after_download: Optional[bool] = None
    delete_source_file_set_after_download: Optional[bool] = None
    destination_base_directory: Optional[str] = None
    destination_directory_path: str
    destination_file_set_name: str
    destination_filename: Optional[str] = None
    export_metadata_format: Optional[str] = None
    export_metadata_view: Optional[UUID] = None
    export_original: Optional[bool] = None
    export_posters: Optional[bool] = None
    export_proxy: Optional[bool] = None
    export_transcription_format: Optional[str] = None
    file_set_id: Optional[UUID] = None
    format_id: Optional[UUID] = None
    id: Optional[UUID] = None
    include_original_extension: Optional[bool] = None
    job_id: Optional[UUID] = None
    job_steps: Optional[Dict[str, Any]] = Field(default_factory=dict)
    local_storage_id: Optional[UUID] = None
    original_storage_id: Optional[UUID] = None
    original_url: Optional[HttpUrl] = None
    overwrite: Optional[bool] = None
    parent_job_id: Optional[UUID] = None
    temporary_file_set_source: Optional[bool] = None
    transfer_type: Optional[str] = None


class CollectionKeyframesSchema(BaseModel):
    """Represents a CollectionKeyframesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['CollectionKeyframeSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class KeyframeSchema(BaseModel):
    """Represents a KeyframeSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    collection_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    id: Optional[UUID] = None
    is_custom_keyframe: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    storage_method: Optional[str] = None
    time_code: Optional['TimeCodeType'] = None
    type: Literal['KEYFRAME_MAP', 'KEYFRAME', 'POSTER']
    upload_credentials: Optional[Dict[str, Any]] = Field(default_factory=dict)
    upload_method: Optional[str] = None
    upload_url: Optional[str] = None
    url: Optional[str] = None
    version_id: Optional[UUID] = None


class CollectionKeyframeUpdateSchema(BaseModel):
    """Represents a CollectionKeyframeUpdateSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    is_custom_keyframe: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    time_code: Optional['TimeCodeType'] = None
    type: Literal['KEYFRAME_MAP', 'KEYFRAME', 'POSTER']
    url: Optional[str] = None


class CollectionKeyframeSchema(BaseModel):
    """Represents a CollectionKeyframeSchema in the Iconik system."""
    collection_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    id: Optional[UUID] = None
    is_custom_keyframe: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    time_code: Optional['TimeCodeType'] = None
    type: Literal['KEYFRAME_MAP', 'KEYFRAME', 'POSTER']
    url: Optional[str] = None


class CollectionKeyframeCreateSchema(BaseModel):
    """Represents a CollectionKeyframeCreateSchema in the Iconik system."""
    collection_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    id: Optional[UUID] = None
    is_custom_keyframe: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    resolution: Optional['ResolutionType'] = None
    rotation: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['OPEN', 'GROWING', 'AWAITED', 'CLOSED', 'FAILED',
                             'ARCHIVED', 'MISSING', 'REDISCOVERED',
                             'DELETED']] = None
    storage_id: Optional[UUID] = None
    time_code: Optional['TimeCodeType'] = None
    type: Literal['KEYFRAME_MAP', 'KEYFRAME', 'POSTER']
    upload_credentials: Optional[Dict[str, Any]] = Field(default_factory=dict)
    upload_method: Optional[str] = None
    upload_url: Optional[str] = None
    url: Optional[str] = None


class ResolutionType(BaseModel):
    """Represents a ResolutionType in the Iconik system."""
    height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class TimeCodeType(BaseModel):
    """Represents a TimeCodeType in the Iconik system."""
    frames_number: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    is_drop_frame: Optional[bool] = None
    time_base: Optional['TimeBaseType'] = None


class TimeBaseType(BaseModel):
    """Represents a TimeBaseType in the Iconik system."""
    denominator: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    numerator: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class CollectionExportSchema(BaseModel):
    """Represents a CollectionExportSchema in the Iconik system."""
    delete_original: Optional[bool] = None
    export_metadata: Optional[bool] = None
    export_to_asset_folder: Optional[bool] = None
    keep_collection_structure: Optional[bool] = None
    metadata_format: Optional[Literal['CSV', 'JSON', 'XML']] = None
    metadata_view: Optional[UUID] = None
    overwrite: Optional[bool] = None
    preferred_original_storage_id: Optional[UUID] = None


class CollectionCopyKeyframesResponseSchema(BaseModel):
    """Represents a CollectionCopyKeyframesResponseSchema in the Iconik system."""
    custom_keyframe: Optional[UUID] = None
    custom_poster: Optional[UUID] = None


class CollectionCopyKeyframesRequestSchema(BaseModel):
    """Represents a CollectionCopyKeyframesRequestSchema in the Iconik system."""
    custom_keyframe: Optional[UUID] = None
    custom_poster: Optional[UUID] = None
    id: UUID


class CheckAssetHasFilesSchema(BaseModel):
    """Represents a CheckAssetHasFilesSchema in the Iconik system."""
    asset_id: UUID
    version_id: UUID


class BulkTransferToStorageSchema(BaseModel):
    """Represents a BulkTransferToStorageSchema in the Iconik system."""
    allow_duplicate_transfers: Optional[bool] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_original: Optional[bool] = None
    file_path: Optional[str] = None
    format_name: Optional[str] = None
    keep_collection_structure: Optional[bool] = None
    keep_parent_collection_structure: Optional[bool] = None
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']
    overwrite: Optional[bool] = None
    preferred_original_storage_id: Optional[UUID] = None


class BulkTransferSchema(BaseModel):
    """Represents a BulkTransferSchema in the Iconik system."""
    allow_duplicate_transfers: Optional[bool] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_original: Optional[bool] = None
    keep_collection_structure: Optional[bool] = None
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']
    preferred_original_storage_id: Optional[UUID] = None


class BulkTranscodeSchema(BaseModel):
    """Represents a BulkTranscodeSchema in the Iconik system."""
    format_name: Optional[str] = None
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']
    prefer_any_cloud: Optional[bool] = None
    preferred_storage_id: Optional[UUID] = None
    preferred_storage_method: Optional[Literal['FILE', 'HTTP', 'FTP', 'SFTP',
                                               'S3', 'B2', 'GCS', 'PORTAL',
                                               'CUSTOM', 'AZURE']] = None
    priority: Optional[int] = Field(None, ge=1, le=10)


class BulkFilesetRestoreSchema(BaseModel):
    """Represents a BulkFilesetRestoreSchema in the Iconik system."""
    allow_duplicate_transfers: Optional[bool] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_original: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_storage_id: Optional[UUID] = None
    keep_collection_structure: Optional[bool] = None
    keep_parent_collection_structure: Optional[bool] = None
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']
    preferred_original_storage_id: Optional[UUID] = None


class BulkFilesetExportSchema(BaseModel):
    """Represents a BulkFilesetExportSchema in the Iconik system."""
    allow_duplicate_transfers: Optional[bool] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_original: Optional[bool] = None
    export_metadata: Optional[bool] = None
    export_to_asset_folder: Optional[bool] = None
    keep_collection_structure: Optional[bool] = None
    metadata_format: Optional[Literal['CSV', 'JSON', 'XML']] = None
    metadata_view: Optional[UUID] = None
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections']
    overwrite: Optional[bool] = None
    preferred_original_storage_id: Optional[UUID] = None


class BulkFilesetArchiveSchema(BaseModel):
    """Represents a BulkFilesetArchiveSchema in the Iconik system."""
    allow_duplicate_transfers: Optional[bool] = None
    delete_only_from_source_folder: Optional[bool] = None
    delete_original: Optional[bool] = None
    destination_directory_path: Optional[str] = None
    destination_storage_id: Optional[str] = None
    keep_collection_structure: Optional[bool] = None
    keep_parent_collection_structure: Optional[bool] = None
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']
    preferred_original_storage_id: Optional[UUID] = None


class BulkCheckAssetHasFilesSchema(BaseModel):
    """Represents a BulkCheckAssetHasFilesSchema in the Iconik system."""
    objects: List['CheckAssetHasFiles']


class CheckAssetHasFiles(BaseModel):
    """Represents a CheckAssetHasFiles in the Iconik system."""
    asset_id: UUID
    version_id: UUID


class BulkAssetIdsWithFiles(BaseModel):
    """Represents a BulkAssetIdsWithFiles in the Iconik system."""
    asset_ids: Optional[List[UUID]] = Field(default_factory=list)


class BulkActionSchema(BaseModel):
    """Represents a BulkActionSchema in the Iconik system."""
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']


class BaseQueryParamsSchema(BaseModel):
    """Represents a BaseQueryParamsSchema in the Iconik system."""
    page: Optional[int] = Field(
        None, ge=1, le=10000, description="Which page number to fetch"
    )
    per_page: Optional[int] = Field(
        None, ge=0, le=1000, description="The number of items for each page"
    )
    sort: Optional[str] = Field(
        None,
        description="A comma separated list of fieldnames with order (asc/desc)"
    )


class BaseExportSchema(BaseModel):
    """Represents a BaseExportSchema in the Iconik system."""
    export_metadata: Optional[bool] = None
    export_to_asset_folder: Optional[bool] = None
    metadata_format: Optional[Literal['CSV', 'JSON', 'XML']] = None
    metadata_view: Optional[UUID] = None
    overwrite: Optional[bool] = None
    preferred_original_storage_id: Optional[UUID] = None


class B2SettingsSchema(BaseModel):
    """Represents a B2SettingsSchema in the Iconik system."""
    access_group_id: Optional[UUID] = None
    account_id: str
    acl_template_id: Optional[UUID] = None
    add_uuid_to_filenames: Optional[bool] = None
    aggregate_identical_files: Optional[bool] = None
    aggregate_ignore: Optional[List[str]] = Field(default_factory=list)
    aggregate_only_on_same_storage: Optional[bool] = None
    authorization_token: str
    bucket_id: str
    bucket_name: str
    delete: Optional[bool] = None
    enable_collection_directory_mapping: Optional[bool] = None
    filename_is_external_id: Optional[bool] = None
    folder_name_tags_metadata_field_name: Optional[str] = None
    folder_name_tags_metadata_view_id: Optional[UUID] = None
    is_system: Optional[bool] = None
    metadata_conversion_url: Optional[str] = None
    metadata_conversion_url_headers: Optional[str] = None
    metadata_view_id: Optional[UUID] = None
    path: str
    preload_edge_jobs: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    read: Optional[bool] = None
    root_collection_id: Optional[UUID] = None
    scan: Optional[bool] = None
    scan_directories: Optional[List[str]] = Field(default_factory=list)
    scan_ignore: Optional[List[str]] = Field(default_factory=list)
    sidecar_metadata_required: Optional[bool] = None
    title_includes_extension: Optional[bool] = None
    transcode_ignore: Optional[List[str]] = Field(default_factory=list)
    write: Optional[bool] = None


class AzureSettingsSchema(BaseModel):
    """Represents a AzureSettingsSchema in the Iconik system."""
    access_group_id: Optional[UUID] = None
    acl_template_id: Optional[UUID] = None
    add_uuid_to_filenames: Optional[bool] = None
    aggregate_identical_files: Optional[bool] = None
    aggregate_ignore: Optional[List[str]] = Field(default_factory=list)
    aggregate_only_on_same_storage: Optional[bool] = None
    connection_string: str
    container: str
    delete: Optional[bool] = None
    enable_collection_directory_mapping: Optional[bool] = None
    filename_is_external_id: Optional[bool] = None
    folder_name_tags_metadata_field_name: Optional[str] = None
    folder_name_tags_metadata_view_id: Optional[UUID] = None
    is_system: Optional[bool] = None
    metadata_conversion_url: Optional[str] = None
    metadata_conversion_url_headers: Optional[str] = None
    metadata_view_id: Optional[UUID] = None
    path: str
    preload_edge_jobs: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    read: Optional[bool] = None
    root_collection_id: Optional[UUID] = None
    scan: Optional[bool] = None
    scan_directories: Optional[List[str]] = Field(default_factory=list)
    scan_ignore: Optional[List[str]] = Field(default_factory=list)
    sidecar_metadata_required: Optional[bool] = None
    title_includes_extension: Optional[bool] = None
    transcode_ignore: Optional[List[str]] = Field(default_factory=list)
    write: Optional[bool] = None


class AssetSubclipKeyframesSchema(BaseModel):
    """Represents a AssetSubclipKeyframesSchema in the Iconik system."""
    asset_id: UUID
    filename: Optional[str] = None
    name: Optional[str] = None
    original_asset_id: UUID
    original_segment_id: Optional[UUID] = None
    original_version_id: UUID
    time_end_milliseconds: int = Field(
        ..., ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: int = Field(
        ..., ge=-9223372036854775808, le=9223372036854775807
    )
    version_id: UUID


class AssetLinkProxySchema(BaseModel):
    """Represents a AssetLinkProxySchema in the Iconik system."""
    asset_id: UUID
    filename: Optional[str] = None
    name: Optional[str] = None
    url: HttpUrl
    version_id: UUID


class AssetExportSchema(BaseModel):
    """Represents a AssetExportSchema in the Iconik system."""
    export_metadata: Optional[bool] = None
    export_to_asset_folder: Optional[bool] = None
    file_name: Optional[str] = None
    format_id: Optional[UUID] = None
    metadata_format: Optional[Literal['CSV', 'JSON', 'XML']] = None
    metadata_view: Optional[UUID] = None
    overwrite: Optional[bool] = None
    preferred_original_storage_id: Optional[UUID] = None
    transcode_profile_ids: Optional[List[UUID]] = Field(default_factory=list)


class AssetBatchExportSchema(BaseModel):
    """Represents a AssetBatchExportSchema in the Iconik system."""
    assets: List['AssetBatchExportItemSchema']
    export_metadata: Optional[bool] = None
    export_to_asset_folder: Optional[bool] = None
    metadata_format: Optional[Literal['CSV', 'JSON', 'XML']] = None
    metadata_view: Optional[UUID] = None
    overwrite: Optional[bool] = None
    preferred_original_storage_id: Optional[UUID] = None
    transcode_profile_ids: Optional[List[UUID]] = Field(default_factory=list)


class AssetBatchExportItemSchema(BaseModel):
    """Represents a AssetBatchExportItemSchema in the Iconik system."""
    asset_id: UUID
    file_name: Optional[str] = None
    format_id: Optional[UUID] = None


class AnalysisServiceAccountsSchema(BaseModel):
    """Represents a AnalysisServiceAccountsSchema in the Iconik system."""
    objects: Optional[List['AnalysisServiceAccountReadSchema']
                      ] = Field(default_factory=list)


class AnalysisServiceAccountSchema(BaseModel):
    """Represents a AnalysisServiceAccountSchema in the Iconik system."""
    id: Optional[UUID] = None
    method: Literal['GOOGLE_AI', 'AMAZON', 'REV_AI', 'ICONIK']
    name: str
    settings: Dict[str, Any]


class AnalysisServiceAccountReadSchema(BaseModel):
    """Represents a AnalysisServiceAccountReadSchema in the Iconik system."""
    id: Optional[UUID] = None
    method: Literal['GOOGLE_AI', 'AMAZON', 'REV_AI', 'ICONIK']
    name: str
    settings: Dict[str, Any]


class AnalysisServiceAccountBaseSchema(BaseModel):
    """Represents a AnalysisServiceAccountBaseSchema in the Iconik system."""


class AnalysisRevAISettingsSchema(BaseModel):
    """Represents a AnalysisRevAISettingsSchema in the Iconik system."""
    access_token: str
    custom_vocabulary: Optional[List[str]] = Field(default_factory=list)
    is_system: Optional[bool] = None
    metadata_view_id: Optional[str] = Field(
        None,
        description="View in which to save topic extraction time-based metadata"
    )
    summary_metadata_field: Optional[str] = Field(
        None,
        description=
        "If a transcription summary is requested, save it to this metadata field"
    )
    topics_metadata_field: Optional[str] = Field(
        None,
        description=
        "If topics extraction is requested, save result to this metadata field"
    )


class AnalysisProfilesSchema(BaseModel):
    """Represents a AnalysisProfilesSchema in the Iconik system."""
    objects: Optional[List['AnalysisProfileSchema']
                      ] = Field(default_factory=list)


class AnalysisProfileSettingsSchema(BaseModel):
    """Represents a AnalysisProfileSettingsSchema in the Iconik system."""
    is_system: Optional[bool] = None


class AnalysisProfileServiceIdSchema(BaseModel):
    """Represents a AnalysisProfileServiceIdSchema in the Iconik system."""
    analysis_service_account_id: UUID


class AnalysisProfileSchema(BaseModel):
    """Represents a AnalysisProfileSchema in the Iconik system."""
    analysis_service_account_id: UUID
    enabled: Optional[bool] = None
    id: Optional[UUID] = None
    is_default: Optional[bool] = None
    media_type: Literal['image', 'video', 'transcription', 'face_image',
                        'face_video']
    name: str
    service_type: Optional[Literal['GOOGLE_VISION', 'GOOGLE_VIDEO_INTELLIGENCE',
                                   'AMAZON_REKOGNITION', 'REV_AI', 'ICONIK',
                                   'ICONIK_FACE_RECOGNITION']] = None
    settings: Optional[Dict[str, Any]] = Field(default_factory=dict)


class AnalysisProfileRevAISettingsSchema(BaseModel):
    """Represents a AnalysisProfileRevAISettingsSchema in the Iconik system."""
    is_system: Optional[bool] = None
    min_confidence: Optional[float] = Field(None, ge=0, le=1)


class AnalysisProfileIconikFaceRecognitionSettingsSchema(BaseModel):
    """Represents a AnalysisProfileIconikFaceRecognitionSettingsSchema in the Iconik system."""
    confirmed_face_match_threshold: Optional[float] = Field(None, ge=0, le=1)
    detection_threshold: Optional[float] = Field(None, ge=0, le=1)
    directory_path: str
    is_system: Optional[bool] = None
    storage_id: UUID
    unconfirmed_face_match_threshold: Optional[float] = Field(None, ge=0, le=1)


class AnalysisProfileGoogleVisionSettingsSchema(BaseModel):
    """Represents a AnalysisProfileGoogleVisionSettingsSchema in the Iconik system."""
    is_system: Optional[bool] = None
    min_confidence: Optional[float] = Field(None, ge=0, le=1)


class AnalysisProfileGoogleVideoIntelligenceSettingsSchema(BaseModel):
    """Represents a AnalysisProfileGoogleVideoIntelligenceSettingsSchema in the Iconik system."""
    frame_confidence_threshold: Optional[float] = Field(None, ge=0.1, le=0.9)
    is_system: Optional[bool] = None
    video_confidence_threshold: Optional[float] = Field(None, ge=0.1, le=0.9)


class AnalysisProfileBaseSchema(BaseModel):
    """Represents a AnalysisProfileBaseSchema in the Iconik system."""


class AnalysisProfileAmazonRekognitionSettingsSchema(BaseModel):
    """Represents a AnalysisProfileAmazonRekognitionSettingsSchema in the Iconik system."""
    is_system: Optional[bool] = None
    min_confidence: Optional[int] = Field(None, ge=0, le=100)


class AnalysisIconikSettingsSchema(BaseModel):
    """Represents a AnalysisIconikSettingsSchema in the Iconik system."""
    is_system: Optional[bool] = None


class AnalysisGoogleAISettingsSchema(BaseModel):
    """Represents a AnalysisGoogleAISettingsSchema in the Iconik system."""
    bucket_name: str
    is_system: Optional[bool] = None
    json_key: str


class AnalysisAmazonRekognitionSettingsSchema(BaseModel):
    """Represents a AnalysisAmazonRekognitionSettingsSchema in the Iconik system."""
    access_key: str
    bucket: str
    endpoint: str
    is_system: Optional[bool] = None
    path: str
    region: str
    secret_key: str


# Update forward references
ZencoderSettingsSchema.model_rebuild()
WildmokaSettingsSchema.model_rebuild()
WatchFolderVideoTranscoderSchema.model_rebuild()
VantageSettingsSchema.model_rebuild()
UploadIconikStorageGatewayLogsSchema.model_rebuild()
UploadFilesSchema.model_rebuild()
TransfersToStorageSchema.model_rebuild()
TransfersFromStorageSchema.model_rebuild()
TransferToStorageSchema.model_rebuild()
TransferToStorageReadSchema.model_rebuild()
TransferSignedURLSchema.model_rebuild()
TransferFromStorageSchema.model_rebuild()
TransferFromStorageReadSchema.model_rebuild()
TransferCloudSchema.model_rebuild()
TranscodersSchema.model_rebuild()
TranscodersQueryParamsSchema.model_rebuild()
TranscodersByStorageSchema.model_rebuild()
TranscoderSchema.model_rebuild()
TranscoderReadSchema.model_rebuild()
TranscoderByStorageReadSchema.model_rebuild()
TranscoderBaseSchema.model_rebuild()
TranscodeResponseSchema.model_rebuild()
TranscodeRequestSchema.model_rebuild()
TimeCodeTypeSchema.model_rebuild()
TimeBaseTypeSchema.model_rebuild()
TemporaryFileSetSchema.model_rebuild()
TemporaryFileCreateSchema.model_rebuild()
TelestreamCloudSchema.model_rebuild()
SubtitlesSchema.model_rebuild()
SubtitleSchema.model_rebuild()
SubtitleRequestSchema.model_rebuild()
Subtitle.model_rebuild()
StoragesReadSchema.model_rebuild()
StoragesQueryParamsSchema.model_rebuild()
StorageValidationSchema.model_rebuild()
StorageScanSchema.model_rebuild()
StorageReadSchema.model_rebuild()
StoragePrivateDataSchema.model_rebuild()
StoragePermissionsSchema.model_rebuild()
StorageFilesQueryParamsSchema.model_rebuild()
StorageFilesDeleteBulkSchema.model_rebuild()
StorageFileUpdateSchema.model_rebuild()
StorageFileSchema.model_rebuild()
StorageBaseSchema.model_rebuild()
StorageAutoScanSchema.model_rebuild()
StorageAccessSchema.model_rebuild()
SftpSettingsSchema.model_rebuild()
S3SettingsSchema.model_rebuild()
ResolutionTypeSchema.model_rebuild()
ReindexTranscoderSchema.model_rebuild()
ReindexStorageSchema.model_rebuild()
ReindexFormatSchema.model_rebuild()
ReindexFileSetSchema.model_rebuild()
ReindexFileSchema.model_rebuild()
ReindexExportLocationSchema.model_rebuild()
RedlineSchema.model_rebuild()
ProxyUpdateSchema.model_rebuild()
ProxySchema.model_rebuild()
ProxyDownloadURLSchema.model_rebuild()
ProxyCreateSchema.model_rebuild()
ProxyBaseSchema.model_rebuild()
ProxiesSchema.model_rebuild()
PrioDirSchema.model_rebuild()
PortalSettingsSchema.model_rebuild()
MultipartUploadSchema.model_rebuild()
MultipartUploadProxyCleanupSchema.model_rebuild()
MultipartUploadComposeSchema.model_rebuild()
MultipartUploadCleanupSchema.model_rebuild()
MultipartB2StartUpload.model_rebuild()
MultipartB2FinishUpload.model_rebuild()
MultipartB2CancelUpload.model_rebuild()
MultiPartUploadURLsSchema.model_rebuild()
MultiPartUploadURLSchema.model_rebuild()
MultiPartUploadComposeURLSchema.model_rebuild()
MultiPartURLsSchema.model_rebuild()
MultiPartS3UrlPartsSchema.model_rebuild()
MultiPartS3UrlPartSchema.model_rebuild()
MoveAssetResourceSchema.model_rebuild()
ListObjectsSchema.model_rebuild()
KeyframesSchema.model_rebuild()
KeyframeUpdateSchema.model_rebuild()
KeyframeCreateSchema.model_rebuild()
KeyframeBaseSchema.model_rebuild()
JobsStateSchema.model_rebuild()
JobsPrioritySchema.model_rebuild()
ImageMagickSettingsSchema.model_rebuild()
IconikStorageGatewayEventsSchema.model_rebuild()
IconikStorageGatewayEventsPurgeSchema.model_rebuild()
IconikStorageGatewayEventSchema.model_rebuild()
IconikEdgeTranscoderSchema.model_rebuild()
ISGHandlerURLSchema.model_rebuild()
HttpSettingsSchema.model_rebuild()
GoogleCloudStorageSettingsSchema.model_rebuild()
GatewayStatusSchema.model_rebuild()
GatewayReportSchema.model_rebuild()
FtpSettingsSchema.model_rebuild()
FormatsSchema.model_rebuild()
FormatsElasticSchema.model_rebuild()
FormatSchema.model_rebuild()
FormatRestoreSchema.model_rebuild()
FormatElasticSchema.model_rebuild()
FormatDeleteArchiveSchema.model_rebuild()
FormatArchiveSchema.model_rebuild()
FlicsTranscoderSchema.model_rebuild()
FilesetTransferBaseSchema.model_rebuild()
FilesSchema.model_rebuild()
FilesElasticSchema.model_rebuild()
FileShareUploadEditSchema.model_rebuild()
FileSettingsSchema.model_rebuild()
PrioDir.model_rebuild()
FileSetsSchema.model_rebuild()
FileSetsElasticSchema.model_rebuild()
FileSetSourcesSchema.model_rebuild()
FileSetSourceSchema.model_rebuild()
FileSetSchema.model_rebuild()
FileSetElasticSchema.model_rebuild()
FileSchema.model_rebuild()
FileExistenceCheckSchema.model_rebuild()
FileElasticSchema.model_rebuild()
FileDownloadURLSchema.model_rebuild()
FileDeletionsSchema.model_rebuild()
StorageSchema.model_rebuild()
FileDeletionFromLocalStorageSchema.model_rebuild()
FileCreateSchema.model_rebuild()
FileBaseSchema.model_rebuild()
FFmpegSettingsSchema.model_rebuild()
ExportLocationsSchema.model_rebuild()
ExportLocationSchema.model_rebuild()
EncodingComSettingsSchema.model_rebuild()
ElementalServerSchema.model_rebuild()
ElementalMediaConvertSchema.model_rebuild()
EditReadyTranscoderSchema.model_rebuild()
Proxy.model_rebuild()
EditProxySettingsSchema.model_rebuild()
EditProxySchema.model_rebuild()
EditProxyResponseSchema.model_rebuild()
DeleteQueueSchema.model_rebuild()
DeleteQueueFormatsQueryParamsSchema.model_rebuild()
DeleteQueueFileSetsQueryParamsSchema.model_rebuild()
CustomSettingsSchema.model_rebuild()
ComponentsSchema.model_rebuild()
ComponentSchema.model_rebuild()
CompleteExportToLocalStorageSchema.model_rebuild()
CollectionKeyframesSchema.model_rebuild()
KeyframeSchema.model_rebuild()
CollectionKeyframeUpdateSchema.model_rebuild()
CollectionKeyframeSchema.model_rebuild()
CollectionKeyframeCreateSchema.model_rebuild()
ResolutionType.model_rebuild()
TimeCodeType.model_rebuild()
TimeBaseType.model_rebuild()
CollectionExportSchema.model_rebuild()
CollectionCopyKeyframesResponseSchema.model_rebuild()
CollectionCopyKeyframesRequestSchema.model_rebuild()
CheckAssetHasFilesSchema.model_rebuild()
BulkTransferToStorageSchema.model_rebuild()
BulkTransferSchema.model_rebuild()
BulkTranscodeSchema.model_rebuild()
BulkFilesetRestoreSchema.model_rebuild()
BulkFilesetExportSchema.model_rebuild()
BulkFilesetArchiveSchema.model_rebuild()
BulkCheckAssetHasFilesSchema.model_rebuild()
CheckAssetHasFiles.model_rebuild()
BulkAssetIdsWithFiles.model_rebuild()
BulkActionSchema.model_rebuild()
BaseQueryParamsSchema.model_rebuild()
BaseExportSchema.model_rebuild()
B2SettingsSchema.model_rebuild()
AzureSettingsSchema.model_rebuild()
AssetSubclipKeyframesSchema.model_rebuild()
AssetLinkProxySchema.model_rebuild()
AssetExportSchema.model_rebuild()
AssetBatchExportSchema.model_rebuild()
AssetBatchExportItemSchema.model_rebuild()
AnalysisServiceAccountsSchema.model_rebuild()
AnalysisServiceAccountSchema.model_rebuild()
AnalysisServiceAccountReadSchema.model_rebuild()
AnalysisServiceAccountBaseSchema.model_rebuild()
AnalysisRevAISettingsSchema.model_rebuild()
AnalysisProfilesSchema.model_rebuild()
AnalysisProfileSettingsSchema.model_rebuild()
AnalysisProfileServiceIdSchema.model_rebuild()
AnalysisProfileSchema.model_rebuild()
AnalysisProfileRevAISettingsSchema.model_rebuild()
AnalysisProfileIconikFaceRecognitionSettingsSchema.model_rebuild()
AnalysisProfileGoogleVisionSettingsSchema.model_rebuild()
AnalysisProfileGoogleVideoIntelligenceSettingsSchema.model_rebuild()
AnalysisProfileBaseSchema.model_rebuild()
AnalysisProfileAmazonRekognitionSettingsSchema.model_rebuild()
AnalysisIconikSettingsSchema.model_rebuild()
AnalysisGoogleAISettingsSchema.model_rebuild()
AnalysisAmazonRekognitionSettingsSchema.model_rebuild()
