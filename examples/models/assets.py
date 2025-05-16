# pylint: disable=line-too-long
"""
Iconik Assets Models
This module contains Pydantic models for the Iconik Assets API.
"""
from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID
from pydantic import BaseModel, Field, HttpUrl


class TranscriptionTypeSchema(BaseModel):
    """Represents a TranscriptionTypeSchema in the Iconik system."""
    speaker: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    words: List['TranscriptionElementTypeSchema']


class TranscriptionElementTypeSchema(BaseModel):
    """Represents a TranscriptionElementTypeSchema in the Iconik system."""
    end_ms: int = Field(..., ge=-9223372036854775808, le=9223372036854775807)
    score: Optional[float] = None
    start_ms: int = Field(..., ge=-9223372036854775808, le=9223372036854775807)
    value: str


class SynchronizeCollectionKeyframesSchema(BaseModel):
    """Represents a SynchronizeCollectionKeyframesSchema in the Iconik system."""
    asset_ids: Optional[List[str]] = Field(default_factory=list)


class SyncSessionSchema(BaseModel):
    """Represents a SyncSessionSchema in the Iconik system."""
    current_dc_url: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    dc_url: Optional[str] = None
    id: Optional[UUID] = None
    node: Optional[str] = None


class SyncSessionCreateSchema(BaseModel):
    """Represents a SyncSessionCreateSchema in the Iconik system."""
    current_dc_url: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    dc_url: Optional[str] = None
    id: Optional[UUID] = None
    node: Optional[str] = None


class StorageContentInfoSchema(BaseModel):
    """Represents a StorageContentInfoSchema in the Iconik system."""
    assets_count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    file_count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    storage_id: Optional[UUID] = None
    total_duration_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    total_size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class SharesSchema(BaseModel):
    """Represents a SharesSchema in the Iconik system."""
    objects: Optional[List['ShareSchema']] = Field(default_factory=list)


class SharesElasticSchema(BaseModel):
    """Represents a SharesElasticSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['ShareElasticSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class ShareUsersSchema(BaseModel):
    """Represents a ShareUsersSchema in the Iconik system."""
    objects: Optional[List['ShareUserSchema']] = Field(default_factory=list)


class UserSchema(BaseModel):
    """Represents a UserSchema in the Iconik system."""
    email: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[UUID] = None
    last_name: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None


class ShareUsersElasticSchema(BaseModel):
    """Represents a ShareUsersElasticSchema in the Iconik system."""
    access_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    email: Optional[str] = None
    id: Optional[UUID] = None
    last_access_date: Optional[datetime] = None


class ShareUserSchema(BaseModel):
    """Represents a ShareUserSchema in the Iconik system."""
    access_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    email: str
    first_name: Optional[str] = None
    id: Optional[str] = None
    internal_user_id: Optional[str] = None
    last_access_date: Optional[datetime] = None
    last_name: Optional[str] = None
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    password: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    share_id: Optional[str] = None


class ShareURLSchema(BaseModel):
    """Represents a ShareURLSchema in the Iconik system."""
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
    date_created: Optional[datetime] = None
    expires: Optional[datetime] = None
    has_password: Optional[bool] = None
    id: Optional[str] = None
    is_approval: Optional[bool] = None
    message: Optional[str] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    owner_id: Optional[str] = None
    project_id: Optional[UUID] = Field(
        None, description="Project ID if the share is created from a project"
    )
    show_watermark: Optional[bool] = None
    system_domain_id: Optional[str] = None
    title: Optional[str] = None
    upload_storage_id: Optional[UUID] = None
    url: Optional[str] = None


class ShareURLCreateSchema(BaseModel):
    """Represents a ShareURLCreateSchema in the Iconik system."""
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
    expires: Optional[datetime] = None
    is_approval: Optional[bool] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    owner_id: Optional[str] = None
    password: Optional[str] = None
    show_watermark: Optional[bool] = None
    system_domain_id: Optional[str] = None
    title: Optional[str] = None
    upload_storage_id: Optional[UUID] = None


class ShareTokenSchema(BaseModel):
    """Represents a ShareTokenSchema in the Iconik system."""
    app_id: str
    email: str
    expires: datetime
    object_id: str
    object_type: str
    roles: List[str]
    share_id: str
    share_user_id: str
    system_domain_id: str
    token: str
    user_id: str


class ShareSchema(BaseModel):
    """Represents a ShareSchema in the Iconik system."""
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
    date_created: Optional[datetime] = None
    expires: Optional[datetime] = None
    has_password: Optional[bool] = None
    id: Optional[str] = None
    is_approval: Optional[bool] = None
    message: Optional[str] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    owner_id: Optional[str] = None
    project_id: Optional[UUID] = Field(
        None, description="Project ID if the share is created from a project"
    )
    show_watermark: Optional[bool] = None
    system_domain_id: Optional[str] = None
    title: Optional[str] = None
    upload_storage_id: Optional[UUID] = None
    url: Optional[str] = None


class ShareRoles(BaseModel):
    """Represents a ShareRoles in the Iconik system."""
    roles: Optional[List[str]] = Field(default_factory=list)


class ShareOptionsBaseSchema(BaseModel):
    """Represents a ShareOptionsBaseSchema in the Iconik system."""
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
    is_approval: Optional[bool] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    show_watermark: Optional[bool] = None
    upload_storage_id: Optional[UUID] = None


class ShareLoginSchema(BaseModel):
    """Represents a ShareLoginSchema in the Iconik system."""
    app_id: Optional[str] = None
    hash: str
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    password: Optional[str] = None
    token: Optional[str] = None


class ShareElasticSchema(BaseModel):
    """Represents a ShareElasticSchema in the Iconik system."""
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
    approval: Optional[Dict[str, Any]] = Field(default_factory=dict)
    date_created: Optional[datetime] = None
    expires: Optional[datetime] = None
    has_password: Optional[bool] = None
    id: Optional[str] = None
    is_approval: Optional[bool] = None
    message: Optional[str] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    object_id: Optional[str] = None
    object_title: Optional[str] = None
    object_type: Optional[str] = None
    owner_id: Optional[str] = None
    personal_url: Optional[str] = None
    project_id: Optional[UUID] = Field(
        None, description="Project ID if the share is created from a project"
    )
    show_watermark: Optional[bool] = None
    system_domain_id: Optional[str] = None
    title: Optional[str] = None
    upload_storage_id: Optional[UUID] = None
    url: Optional[str] = None
    users: Optional[List['ShareUsersElastic']] = Field(default_factory=list)


class ShareUsersElastic(BaseModel):
    """Represents a ShareUsersElastic in the Iconik system."""
    access_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    email: Optional[str] = None
    id: Optional[UUID] = None
    last_access_date: Optional[datetime] = None


class ShareCreateSchema(BaseModel):
    """Represents a ShareCreateSchema in the Iconik system."""
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
    expires: Optional[datetime] = None
    id: Optional[str] = None
    is_approval: Optional[bool] = None
    message: Optional[str] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    owner_id: Optional[str] = None
    password: Optional[str] = None
    project_id: Optional[UUID] = Field(
        None, description="Project ID if the share is created from a project"
    )
    show_watermark: Optional[bool] = None
    system_domain_id: Optional[str] = None
    title: Optional[str] = None
    upload_storage_id: Optional[UUID] = None


class ShareBaseSchema(BaseModel):
    """Represents a ShareBaseSchema in the Iconik system."""
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
    date_created: Optional[datetime] = None
    expires: Optional[datetime] = None
    has_password: Optional[bool] = None
    id: Optional[str] = None
    is_approval: Optional[bool] = None
    message: Optional[str] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    owner_id: Optional[str] = None
    project_id: Optional[UUID] = Field(
        None, description="Project ID if the share is created from a project"
    )
    show_watermark: Optional[bool] = None
    system_domain_id: Optional[str] = None
    title: Optional[str] = None
    upload_storage_id: Optional[UUID] = None
    url: Optional[str] = None


class SequencesSchema(BaseModel):
    """Represents a SequencesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['SequenceSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class SequencesQueryParamsSchema(BaseModel):
    """Represents a SequencesQueryParamsSchema in the Iconik system."""
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


class SequenceSchema(BaseModel):
    """Represents a SequenceSchema in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    name: str
    system_domain_id: Optional[UUID] = None


class SequenceItemsSchema(BaseModel):
    """Represents a SequenceItemsSchema in the Iconik system."""
    objects: Optional[List['SequenceItemSchema']] = Field(default_factory=list)


class SequenceItemsQueryParamsSchema(BaseModel):
    """Represents a SequenceItemsQueryParamsSchema in the Iconik system."""
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


class SequenceItemUpdatePositionSchema(BaseModel):
    """Represents a SequenceItemUpdatePositionSchema in the Iconik system."""
    position: Optional[int] = Field(
        None,
        ge=-2147483648,
        le=2147483647,
        description=
        "New position of the item in the sequence.If not provided, the item will be appended to the end of the sequence"
    )


class SequenceItemSchema(BaseModel):
    """Represents a SequenceItemSchema in the Iconik system."""
    id: Optional[UUID] = None
    object_id: UUID
    object_type: Literal['assets', 'collections']
    position: Optional[int] = Field(
        None,
        ge=-2147483648,
        le=2147483647,
        description=
        "Position of the item in the sequence.If not provided, the item will be appended to the end of the sequence"
    )
    version_id: Optional[UUID] = None


class SequenceCreateSchema(BaseModel):
    """Represents a SequenceCreateSchema in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    name: str
    system_domain_id: Optional[UUID] = None


class SequenceBaseSchema(BaseModel):
    """Represents a SequenceBaseSchema in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    name: str
    system_domain_id: Optional[UUID] = None


class SegmentsSchema(BaseModel):
    """Represents a SegmentsSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['SegmentElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class SegmentSchema(BaseModel):
    """Represents a SegmentSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    drawing: Optional[Any] = None
    external_id: Optional[str] = None
    face_bounding_boxes: Optional[List['FaceBoundingBoxSchema']
                                  ] = Field(default_factory=list)
    has_drawing: Optional[bool] = None
    id: Optional[UUID] = None
    keyframe_id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    path: Optional[str] = None
    person_id: Optional[UUID] = None
    project_id: Optional[UUID] = Field(
        None,
        description="ID of a project if the segment is created from a project"
    )
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = None
    segment_text: Optional[str] = None
    segment_track: Optional[str] = None
    segment_type: Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                          'TRANSCRIPTION', 'SCENE', 'PERSON']
    share_id: Optional[UUID] = Field(
        None,
        description="ID of a share if the segment is created from a share"
    )
    share_user_email: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    subclip_id: Optional[UUID] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    top_level: Optional[bool] = None
    transcription: Optional['TranscriptionType'] = None
    transcription_id: Optional[UUID] = None
    user_first_name: Optional[str] = None
    user_id: Optional[UUID] = None
    user_info: Optional['User'] = None
    user_last_name: Optional[str] = None
    user_photo: Optional[str] = None
    version_id: Optional[UUID] = None


class SegmentQueryParamsSchema(BaseModel):
    """Represents a SegmentQueryParamsSchema in the Iconik system."""
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


class SegmentElasticSchema(BaseModel):
    """Represents a SegmentElasticSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    drawing: Optional[Any] = None
    external_id: Optional[str] = None
    face_bounding_boxes: Optional[List['FaceBoundingBoxSchema']
                                  ] = Field(default_factory=list)
    has_drawing: Optional[bool] = None
    id: Optional[UUID] = None
    keyframe_id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    path: Optional[str] = None
    person_id: Optional[UUID] = None
    project_id: Optional[UUID] = Field(
        None,
        description="ID of a project if the segment is created from a project"
    )
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = None
    segment_text: Optional[str] = None
    segment_track: Optional[str] = None
    segment_type: Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                          'TRANSCRIPTION', 'SCENE', 'PERSON']
    share_id: Optional[UUID] = Field(
        None,
        description="ID of a share if the segment is created from a share"
    )
    share_user_email: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    subclip_id: Optional[UUID] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    top_level: Optional[bool] = None
    transcription: Optional['TranscriptionType'] = None
    transcription_id: Optional[UUID] = None
    user_first_name: Optional[str] = None
    user_id: Optional[UUID] = None
    user_info: Optional['User'] = None
    user_last_name: Optional[str] = None
    user_photo: Optional[str] = None
    version_id: Optional[UUID] = None


class SegmentBaseSchema(BaseModel):
    """Represents a SegmentBaseSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    drawing: Optional[Any] = None
    external_id: Optional[str] = None
    face_bounding_boxes: Optional[List['FaceBoundingBoxSchema']
                                  ] = Field(default_factory=list)
    id: Optional[UUID] = None
    keyframe_id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    path: Optional[str] = None
    person_id: Optional[UUID] = None
    project_id: Optional[UUID] = Field(
        None,
        description="ID of a project if the segment is created from a project"
    )
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = None
    segment_text: Optional[str] = None
    segment_track: Optional[str] = None
    segment_type: Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                          'TRANSCRIPTION', 'SCENE', 'PERSON']
    share_id: Optional[UUID] = Field(
        None,
        description="ID of a share if the segment is created from a share"
    )
    share_user_email: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    subclip_id: Optional[UUID] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    top_level: Optional[bool] = None
    transcription: Optional['TranscriptionType'] = None
    transcription_id: Optional[UUID] = None
    user_first_name: Optional[str] = None
    user_id: Optional[UUID] = None
    user_info: Optional['User'] = None
    user_last_name: Optional[str] = None
    user_photo: Optional[str] = None
    version_id: Optional[UUID] = None


class SchedulePersonActionSchema(BaseModel):
    """Represents a SchedulePersonActionSchema in the Iconik system."""
    job_id: UUID
    new_person_id: Optional[UUID] = None
    queue_name: str


class RelationsSchema(BaseModel):
    """Represents a RelationsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['RelationSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class RelationsQueryParamsSchema(BaseModel):
    """Represents a RelationsQueryParamsSchema in the Iconik system."""
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


class RelationTypesSchema(BaseModel):
    """Represents a RelationTypesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['RelationTypeSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class RelationTypeSchema(BaseModel):
    """Represents a RelationTypeSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    destination_label: str
    is_directional: Optional[bool] = None
    is_system: Optional[bool] = None
    name: str
    source_label: str


class RelationSchema(BaseModel):
    """Represents a RelationSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    related_to_asset_id: UUID
    relation_type: str


class RelationElasticSchema(BaseModel):
    """Represents a RelationElasticSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    related_from_asset_id: Optional[UUID] = None
    related_to_asset_id: Optional[UUID] = None
    relation_type: Optional[str] = None


class ReindexShareSchema(BaseModel):
    """Represents a ReindexShareSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexSequenceSchema(BaseModel):
    """Represents a ReindexSequenceSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexSegmentsSchema(BaseModel):
    """Represents a ReindexSegmentsSchema in the Iconik system."""
    ignore_comments: Optional[bool] = None
    realms: Optional[List[str]] = Field(default_factory=list)
    segment_ids: List[UUID]
    sync_to_another_dc: Optional[bool] = None


class ReindexSegmentSchema(BaseModel):
    """Represents a ReindexSegmentSchema in the Iconik system."""
    ignore_comments: Optional[bool] = None
    realms: Optional[List[str]] = Field(default_factory=list)
    sync_to_another_dc: Optional[bool] = None


class ReindexProjectSchema(BaseModel):
    """Represents a ReindexProjectSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexPlaylistSchema(BaseModel):
    """Represents a ReindexPlaylistSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexInheritedCollectionsACLSchema(BaseModel):
    """Represents a ReindexInheritedCollectionsACLSchema in the Iconik system."""
    collection_ids: List[UUID]
    content: Optional[bool] = None
    recursive: Optional[bool] = None


class ReindexCollectionSchema(BaseModel):
    """Represents a ReindexCollectionSchema in the Iconik system."""
    realms: Optional[List[str]] = Field(default_factory=list)
    sync_to_another_dc: Optional[bool] = None


class ReindexCollectionContentSchema(BaseModel):
    """Represents a ReindexCollectionContentSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexBulkActionSchema(BaseModel):
    """Represents a ReindexBulkActionSchema in the Iconik system."""
    include_assets: Optional[bool] = None
    include_collections: Optional[bool] = None
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']
    realms: Optional[List[str]] = Field(default_factory=list)
    sync_to_another_dc: Optional[bool] = None


class ReindexAssetSchema(BaseModel):
    """Represents a ReindexAssetSchema in the Iconik system."""
    realms: Optional[List[str]] = Field(default_factory=list)
    sync_to_another_dc: Optional[bool] = None


class ReindexAssetHistorySchema(BaseModel):
    """Represents a ReindexAssetHistorySchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexAllSegmentsSchema(BaseModel):
    """Represents a ReindexAllSegmentsSchema in the Iconik system."""
    asset_ids: List[UUID]
    ignore_comments: Optional[bool] = None
    realms: Optional[List[str]] = Field(default_factory=list)
    sync_to_another_dc: Optional[bool] = None


class ReindexAllCollectionsSchema(BaseModel):
    """Represents a ReindexAllCollectionsSchema in the Iconik system."""
    collection_ids: List[UUID]
    realms: Optional[List[str]] = Field(default_factory=list)


class ReindexAllAssetsSchema(BaseModel):
    """Represents a ReindexAllAssetsSchema in the Iconik system."""
    asset_ids: Optional[List[UUID]] = Field(default_factory=list)
    realms: Optional[List[str]] = Field(default_factory=list)
    sync_to_another_dc: Optional[bool] = None


class ProjectsSchema(BaseModel):
    """Represents a ProjectsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['ProjectSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class ProjectsQueryParamsSchema(BaseModel):
    """Represents a ProjectsQueryParamsSchema in the Iconik system."""
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


class ProjectSchema(BaseModel):
    """Represents a ProjectSchema in the Iconik system."""
    collection_id: UUID
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    name: str
    status: Optional[Literal['ACTIVE']] = None
    storage_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class ProjectMembersSchema(BaseModel):
    """Represents a ProjectMembersSchema in the Iconik system."""
    objects: Optional[List['ProjectMemberSchema']] = Field(default_factory=list)


class ProjectMembersQueryParamsSchema(BaseModel):
    """Represents a ProjectMembersQueryParamsSchema in the Iconik system."""
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


class ProjectMemberSchema(BaseModel):
    """Represents a ProjectMemberSchema in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = Field(None, description="User ID in iconik")
    project_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class ProjectMemberCreateSchema(BaseModel):
    """Represents a ProjectMemberCreateSchema in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: UUID = Field(..., description="User ID in iconik")
    project_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class ProjectMemberBaseSchema(BaseModel):
    """Represents a ProjectMemberBaseSchema in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    project_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class ProjectCreateSchema(BaseModel):
    """Represents a ProjectCreateSchema in the Iconik system."""
    collection_id: Optional[UUID] = Field(
        None,
        description="ID of a collection that will become a project collection"
    )
    collection_parent_id: Optional[UUID] = Field(
        None,
        description="ID of a collection that the project should be a child of"
    )
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    name: str
    status: Optional[Literal['ACTIVE']] = None
    storage_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class ProjectBaseSchema(BaseModel):
    """Represents a ProjectBaseSchema in the Iconik system."""
    collection_id: UUID
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    name: str
    status: Optional[Literal['ACTIVE']] = None
    storage_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class PlaylistsSchema(BaseModel):
    """Represents a PlaylistsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['Playlist']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class PlaylistsQueryParamsSchema(BaseModel):
    """Represents a PlaylistsQueryParamsSchema in the Iconik system."""
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


class PlaylistSchema(BaseModel):
    """Represents a PlaylistSchema in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    item_count: Optional[int] = None
    name: str
    playlist_items: Optional[List['PlaylistItemSchema']
                             ] = Field(default_factory=list)
    project_id: Optional[UUID] = None
    status: Optional[Literal['HIDDEN']] = None
    system_domain_id: Optional[UUID] = None


class PlaylistItemsSchema(BaseModel):
    """Represents a PlaylistItemsSchema in the Iconik system."""
    objects: Optional[List['PlaylistItemElasticSchema']
                      ] = Field(default_factory=list)


class PlaylistItemsQueryParamsSchema(BaseModel):
    """Represents a PlaylistItemsQueryParamsSchema in the Iconik system."""
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


class PlaylistItemUpdatePositionSchema(BaseModel):
    """Represents a PlaylistItemUpdatePositionSchema in the Iconik system."""
    position: Optional[int] = Field(
        None,
        ge=-2147483648,
        le=2147483647,
        description=
        "New position of the item in the playlist.If not provided, the item will be appended to the end of the playlist"
    )


class PlaylistItemSchema(BaseModel):
    """Represents a PlaylistItemSchema in the Iconik system."""
    id: Optional[UUID] = None
    object_id: UUID
    object_type: Literal['assets', 'sequences']
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    version_id: Optional[str] = None


class PlaylistItemElasticSchema(BaseModel):
    """Represents a PlaylistItemElasticSchema in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    ancestor_collections: Optional[List[str]] = Field(default_factory=list)
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    category: Optional[str] = None
    comments_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional[Any] = None
    custom_keyframe: Optional[UUID] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_imported: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_viewed: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    deleted_by_user_info: Optional['User'] = None
    duration_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    external_id: Optional[str] = None
    external_link: Optional[HttpUrl] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    favoured: Optional[bool] = None
    files: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    has_unconfirmed_persons: Optional[bool] = None
    id: Optional[UUID] = None
    in_collections: Optional[List[str]] = Field(default_factory=list)
    is_blocked: Optional[bool] = None
    is_online: Optional[bool] = None
    keyframes: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    last_archive_restore_date: Optional[datetime] = None
    media_type: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_type: Optional[str] = None
    original_asset_id: Optional[UUID] = None
    original_segment_id: Optional[UUID] = None
    original_version_id: Optional[UUID] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    position: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    proxies: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    relations: Optional[List['RelationElastic']] = Field(default_factory=list)
    site_name: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    title: str
    type: Optional[Literal['ASSET', 'SEQUENCE', 'NLE_PROJECT', 'PLACEHOLDER',
                           'CUSTOM', 'LINK', 'SUBCLIP']] = None
    updated_by_user: Optional[UUID] = None
    updated_by_user_info: Optional[Any] = None
    versions: Optional[List['AssetVersionSchema']] = Field(default_factory=list)
    versions_number: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    warning: Optional[str] = None


class PlaylistCreateSchema(BaseModel):
    """Represents a PlaylistCreateSchema in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    name: str
    playlist_items: Optional[List['PlaylistItem']] = Field(default_factory=list)
    project_id: Optional[UUID] = None
    status: Optional[Literal['HIDDEN']] = None
    system_domain_id: Optional[UUID] = None


class PlaylistItem(BaseModel):
    """Represents a PlaylistItem in the Iconik system."""
    id: Optional[UUID] = None
    object_id: UUID
    object_type: Literal['assets', 'sequences']
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    version_id: Optional[str] = None


class PlaylistBaseSchema(BaseModel):
    """Represents a PlaylistBaseSchema in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    name: str
    project_id: Optional[UUID] = None
    status: Optional[Literal['HIDDEN']] = None
    system_domain_id: Optional[UUID] = None


class Playlist(BaseModel):
    """Represents a Playlist in the Iconik system."""
    created_by_user: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    item_count: Optional[int] = None
    name: str
    project_id: Optional[UUID] = None
    status: Optional[Literal['HIDDEN']] = None
    system_domain_id: Optional[UUID] = None


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


class GetShareSchema(BaseModel):
    """Represents a GetShareSchema in the Iconik system."""
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
    date_created: Optional[datetime] = None
    expires: Optional[datetime] = None
    has_password: Optional[bool] = None
    id: Optional[str] = None
    is_approval: Optional[bool] = None
    message: Optional[str] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    owner_id: Optional[str] = None
    project_id: Optional[UUID] = Field(
        None, description="Project ID if the share is created from a project"
    )
    show_watermark: Optional[bool] = None
    system_domain_id: Optional[str] = None
    title: Optional[str] = None
    upload_storage_id: Optional[UUID] = None
    upload_storage_presign_md5_checksum: Optional[bool] = None
    url: Optional[str] = None
    users: Optional[List['ShareUser']] = Field(default_factory=list)


class ShareUser(BaseModel):
    """Represents a ShareUser in the Iconik system."""
    access_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    email: str
    first_name: Optional[str] = None
    id: Optional[str] = None
    internal_user_id: Optional[str] = None
    last_access_date: Optional[datetime] = None
    last_name: Optional[str] = None
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    password: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    share_id: Optional[str] = None


class GetAssetsLatestVersionSchema(BaseModel):
    """Represents a GetAssetsLatestVersionSchema in the Iconik system."""
    include_in_progress: Optional[bool] = None
    object_ids: List[UUID]
    object_type: Optional[Literal['assets']] = None


class FavoritesSchema(BaseModel):
    """Represents a FavoritesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[Any] = None
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class FaceBoundingBoxSchema(BaseModel):
    """Represents a FaceBoundingBoxSchema in the Iconik system."""
    bounding_box: Optional[List[float]] = Field(default_factory=list)
    face_id: UUID
    timestamp_ms: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class EditSegmentSchema(BaseModel):
    """Represents a EditSegmentSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    drawing: Optional[Any] = None
    external_id: Optional[str] = None
    face_bounding_boxes: Optional[List['FaceBoundingBox']
                                  ] = Field(default_factory=list)
    id: Optional[UUID] = None
    keyframe_id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    path: Optional[str] = None
    person_id: Optional[UUID] = None
    project_id: Optional[UUID] = Field(
        None,
        description="ID of a project if the segment is created from a project"
    )
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = None
    segment_text: Optional[str] = None
    segment_track: Optional[str] = None
    segment_type: Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                          'TRANSCRIPTION', 'SCENE', 'PERSON']
    share_id: Optional[UUID] = Field(
        None,
        description="ID of a share if the segment is created from a share"
    )
    share_user_email: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    subclip_id: Optional[UUID] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    top_level: Optional[bool] = None
    transcription: Optional['TranscriptionType'] = None
    transcription_id: Optional[UUID] = None
    user_first_name: Optional[str] = None
    user_id: Optional[UUID] = None
    user_info: Optional['User'] = None
    user_last_name: Optional[str] = None
    user_photo: Optional[str] = None
    version_id: Optional[UUID] = None


class EditSegmentForBulkSchema(BaseModel):
    """Represents a EditSegmentForBulkSchema in the Iconik system."""
    asset_id: UUID
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    drawing: Optional[Any] = None
    external_id: Optional[str] = None
    face_bounding_boxes: Optional[List['FaceBoundingBox']
                                  ] = Field(default_factory=list)
    id: UUID
    keyframe_id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    path: Optional[str] = None
    person_id: Optional[UUID] = None
    project_id: Optional[UUID] = Field(
        None,
        description="ID of a project if the segment is created from a project"
    )
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = None
    segment_text: Optional[str] = None
    segment_track: Optional[str] = None
    segment_type: Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                          'TRANSCRIPTION', 'SCENE', 'PERSON']
    share_id: Optional[UUID] = Field(
        None,
        description="ID of a share if the segment is created from a share"
    )
    share_user_email: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    subclip_id: Optional[UUID] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    top_level: Optional[bool] = None
    transcription: Optional['TranscriptionType'] = None
    transcription_id: Optional[UUID] = None
    user_first_name: Optional[str] = None
    user_id: Optional[UUID] = None
    user_info: Optional['User'] = None
    user_last_name: Optional[str] = None
    user_photo: Optional[str] = None
    version_id: Optional[UUID] = None


class EditPersonStatusSchema(BaseModel):
    """Represents a EditPersonStatusSchema in the Iconik system."""
    status: Literal['NEW', 'UNCONFIRMED', 'SYSTEM_CONFIRMED', 'USER_CONFIRMED']


class EditAssetVersionSchema(BaseModel):
    """Represents a EditAssetVersionSchema in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional['User'] = None
    date_created: Optional[datetime] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    has_unconfirmed_persons: Optional[bool] = None
    id: UUID
    is_online: Optional[bool] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    status: Optional[Literal['ACTIVE', 'IN_PROGRESS', 'FAILED', 'DELETING',
                             'DELETED']] = None
    transcribe_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                        'FAILED', 'DONE']] = None
    transcribed_languages: Optional[List[str]] = Field(default_factory=list)
    version_number: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class EditAssetSegmentSchema(BaseModel):
    """Represents a EditAssetSegmentSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    drawing: Optional[Any] = None
    external_id: Optional[str] = None
    face_bounding_boxes: Optional[List['FaceBoundingBox']
                                  ] = Field(default_factory=list)
    id: UUID
    keyframe_id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    path: Optional[str] = None
    person_id: Optional[UUID] = None
    project_id: Optional[UUID] = Field(
        None,
        description="ID of a project if the segment is created from a project"
    )
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = None
    segment_text: Optional[str] = None
    segment_track: Optional[str] = None
    segment_type: Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                          'TRANSCRIPTION', 'SCENE', 'PERSON']
    share_id: Optional[UUID] = Field(
        None,
        description="ID of a share if the segment is created from a share"
    )
    share_user_email: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    subclip_id: Optional[UUID] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    top_level: Optional[bool] = None
    transcription: Optional['TranscriptionType'] = None
    transcription_id: Optional[UUID] = None
    user_first_name: Optional[str] = None
    user_id: Optional[UUID] = None
    user_info: Optional['User'] = None
    user_last_name: Optional[str] = None
    user_photo: Optional[str] = None
    version_id: Optional[UUID] = None


class DrawingSchema(BaseModel):
    """Represents a DrawingSchema in the Iconik system."""
    primitives: Optional[List['DrawingPrimitiveSchema']
                         ] = Field(default_factory=list)


class DrawingPrimitiveSchema(BaseModel):
    """Represents a DrawingPrimitiveSchema in the Iconik system."""
    color: Optional[str] = None
    opacity: Optional[float] = None
    points: Optional[List['DrawingPointSchema']] = Field(default_factory=list)
    text: Optional[str] = None
    type: Literal['LINE', 'RECTANGLE', 'ARROW', 'ELLIPSE', 'PENCIL', 'TEXT']
    width: Optional[float] = None


class DrawingPointSchema(BaseModel):
    """Represents a DrawingPointSchema in the Iconik system."""
    x: int = Field(..., ge=-2147483648, le=2147483647)
    y: int = Field(..., ge=-2147483648, le=2147483647)


class Drawing(BaseModel):
    """Represents a Drawing in the Iconik system."""
    primitives: Optional[List['DrawingPrimitive']] = Field(default_factory=list)


class DrawingPrimitive(BaseModel):
    """Represents a DrawingPrimitive in the Iconik system."""
    color: Optional[str] = None
    opacity: Optional[float] = None
    points: Optional[List['DrawingPoint']] = Field(default_factory=list)
    text: Optional[str] = None
    type: Literal['LINE', 'RECTANGLE', 'ARROW', 'ELLIPSE', 'PENCIL', 'TEXT']
    width: Optional[float] = None


class DrawingPoint(BaseModel):
    """Represents a DrawingPoint in the Iconik system."""
    x: int = Field(..., ge=-2147483648, le=2147483647)
    y: int = Field(..., ge=-2147483648, le=2147483647)


class DeleteSegmentsSchema(BaseModel):
    """Represents a DeleteSegmentsSchema in the Iconik system."""
    segment_ids: Optional[List[UUID]] = Field(default_factory=list)
    segment_type: Optional[Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                                   'TRANSCRIPTION', 'SCENE', 'PERSON']] = None
    version_id: Optional[UUID] = None


class DeleteQueueSchema(BaseModel):
    """Represents a DeleteQueueSchema in the Iconik system."""
    ids: List[UUID]


class DeleteQueueCollectionsQueryParamsSchema(BaseModel):
    """Represents a DeleteQueueCollectionsQueryParamsSchema in the Iconik system."""
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


class DeleteQueueAssetsQueryParamsSchema(BaseModel):
    """Represents a DeleteQueueAssetsQueryParamsSchema in the Iconik system."""
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


class CustomActionsSchema(BaseModel):
    """Represents a CustomActionsSchema in the Iconik system."""
    objects: Optional[List['CustomActionSchema']] = Field(default_factory=list)


class CustomActionSchema(BaseModel):
    """Represents a CustomActionSchema in the Iconik system."""
    app_id: Optional[UUID] = None
    context: Literal['ASSET', 'ASSET_SUBCLIP', 'SHARED_ASSET', 'COLLECTION',
                     'SHARED_COLLECTION', 'BULK', 'SAVED_SEARCH', 'NONE']
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    disabled: Optional[bool] = None
    headers: Optional[Dict[str, str]] = Field(default_factory=dict)
    id: Optional[UUID] = None
    last_error: Optional[str] = None
    last_error_date: Optional[datetime] = None
    metadata_view: Optional[UUID] = None
    status: Optional[Literal['FAILING', 'HEALTHY']] = None
    system_domain_id: Optional[UUID] = None
    title: str
    type: Optional[Literal['OPEN', 'POST']] = None
    url: str


class CustomActionCallbackSchema(BaseModel):
    """Represents a CustomActionCallbackSchema in the Iconik system."""
    asset_ids: Optional[List[UUID]] = Field(default_factory=list)
    collection_ids: Optional[List[UUID]] = Field(default_factory=list)
    metadata_values: Optional[Dict[str, 'MetadataFieldValueSchema']
                              ] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    saved_search_ids: Optional[List[UUID]] = Field(default_factory=list)


class MetadataFieldValueSchema(BaseModel):
    """Represents a MetadataFieldValueSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    field_values: Optional[List[Dict[str, Any]]] = Field(default_factory=list)


class CustomActionCallbackReplySchema(BaseModel):
    """Represents a CustomActionCallbackReplySchema in the Iconik system."""
    redirect_url: Optional[str] = None


class CreateCollectionFromSavedSearchSchema(BaseModel):
    """Represents a CreateCollectionFromSavedSearchSchema in the Iconik system."""
    collection_id: UUID
    job_id: UUID
    saved_search_id: UUID


class CreateCollectionFromSavedSearchResponseSchema(BaseModel):
    """Represents a CreateCollectionFromSavedSearchResponseSchema in the Iconik system."""
    collection_title: Optional[str] = None


class CreateCollectionContentOrderingSchema(BaseModel):
    """Represents a CreateCollectionContentOrderingSchema in the Iconik system."""
    custom_order_sort: Optional[str] = Field(
        None,
        description=
        "Initial sort order for an ordered collection. Specified as a comma separated list of fieldnames with direction. For example - date_created,asc;status,desc"
    )


class CreateAssetVersionSchema(BaseModel):
    """Represents a CreateAssetVersionSchema in the Iconik system."""
    copy_metadata: Optional[bool] = None
    copy_persons: Optional[bool] = None
    copy_segments: Optional[bool] = None
    include_segment_types: Optional[List[Literal['MARKER', 'QC', 'GENERIC',
                                                 'COMMENT', 'TAG',
                                                 'TRANSCRIPTION', 'SCENE',
                                                 'PERSON']]
                                    ] = Field(default_factory=list)
    source_version_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class CreateAssetVersionFromVersionSchema(BaseModel):
    """Represents a CreateAssetVersionFromVersionSchema in the Iconik system."""
    copy_previous_version_persons: Optional[bool] = None
    copy_previous_version_segments: Optional[bool] = None
    exclude_format_ids: Optional[List[str]] = Field(default_factory=list)
    include_segment_types: Optional[List[Literal['MARKER', 'QC', 'GENERIC',
                                                 'COMMENT', 'TAG',
                                                 'TRANSCRIPTION', 'SCENE',
                                                 'PERSON']]
                                    ] = Field(default_factory=list)
    source_metadata_asset_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class CreateAssetVersionFromAssetSchema(BaseModel):
    """Represents a CreateAssetVersionFromAssetSchema in the Iconik system."""
    copy_previous_version_persons: Optional[bool] = None
    copy_previous_version_segments: Optional[bool] = None
    include_segment_types: Optional[List[Literal['MARKER', 'QC', 'GENERIC',
                                                 'COMMENT', 'TAG',
                                                 'TRANSCRIPTION', 'SCENE',
                                                 'PERSON']]
                                    ] = Field(default_factory=list)
    source_metadata_asset_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class CollectionsSchema(BaseModel):
    """Represents a CollectionsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['CollectionElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class CollectionsQueryParamsSchema(BaseModel):
    """Represents a CollectionsQueryParamsSchema in the Iconik system."""
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


class CollectionSizeSchema(BaseModel):
    """Represents a CollectionSizeSchema in the Iconik system."""
    id: Optional[UUID] = None
    size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    title: Optional[str] = None


class CollectionSchema(BaseModel):
    """Represents a CollectionSchema in the Iconik system."""
    category: Optional[str] = None
    created_by_user: Optional[UUID] = None
    custom_keyframe: Optional[UUID] = None
    custom_order_status: Optional[Literal['DISABLED', 'ENABLING',
                                          'ENABLED']] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    external_id: Optional[str] = None
    favoured: Optional[bool] = None
    id: Optional[UUID] = None
    in_collections: Optional[List[UUID]] = Field(default_factory=list)
    is_root: Optional[bool] = None
    keyframe_asset_ids: Optional[List[UUID]] = Field(default_factory=list)
    keyframes: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_type: Optional[str] = None
    parent_id: Optional[UUID] = None
    parents: Optional[List[UUID]] = Field(default_factory=list)
    permissions: Optional[List[str]] = Field(default_factory=list)
    position: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    project_id: Optional[UUID] = None
    status: Optional[Literal['ACTIVE', 'HIDDEN', 'DELETED']] = None
    storage_id: Optional[UUID] = None
    title: str


class CollectionInputSchema(BaseModel):
    """Represents a CollectionInputSchema in the Iconik system."""
    category: Optional[str] = None
    custom_keyframe: Optional[UUID] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    external_id: Optional[str] = None
    is_root: Optional[bool] = None
    keyframe_asset_ids: Optional[List[UUID]] = Field(default_factory=list)
    parent_id: Optional[UUID] = None
    status: Optional[Literal['ACTIVE', 'HIDDEN', 'DELETED']] = None
    storage_id: Optional[UUID] = None
    title: str


class CollectionElasticSchema(BaseModel):
    """Represents a CollectionElasticSchema in the Iconik system."""
    category: Optional[str] = None
    created_by_user: Optional[UUID] = None
    custom_keyframe: Optional[UUID] = None
    custom_order_status: Optional[Literal['DISABLED', 'ENABLING',
                                          'ENABLED']] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    external_id: Optional[str] = None
    favoured: Optional[bool] = None
    id: Optional[UUID] = None
    in_collections: Optional[List[UUID]] = Field(default_factory=list)
    is_root: Optional[bool] = None
    keyframe_asset_ids: Optional[List[UUID]] = Field(default_factory=list)
    keyframes: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_type: Optional[str] = None
    parent_id: Optional[UUID] = None
    parents: Optional[List[UUID]] = Field(default_factory=list)
    permissions: Optional[List[str]] = Field(default_factory=list)
    position: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    project_id: Optional[UUID] = None
    status: Optional[Literal['ACTIVE', 'HIDDEN', 'DELETED']] = None
    storage_id: Optional[UUID] = None
    title: str


class CollectionContentSchema(BaseModel):
    """Represents a CollectionContentSchema in the Iconik system."""
    collection_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    object_id: UUID
    object_type: str


class CollectionContentQueryParamsSchema(BaseModel):
    """Represents a CollectionContentQueryParamsSchema in the Iconik system."""
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


class CollectionContentOrderingSchema(BaseModel):
    """Represents a CollectionContentOrderingSchema in the Iconik system."""
    after_object_id: Optional[UUID] = None
    before_object_id: Optional[UUID] = None
    position: Optional[int] = Field(
        None,
        ge=-1,
        description=
        "Position the member will be moved to. To insert athe the end send -1"
    )


class CollectionContentInfoSchema(BaseModel):
    """Represents a CollectionContentInfoSchema in the Iconik system."""
    assets_count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    collections_count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    storage_info: Optional[List['StorageContentInfo']
                           ] = Field(default_factory=list)
    title: Optional[str] = None
    total_duration_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    total_size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class StorageContentInfo(BaseModel):
    """Represents a StorageContentInfo in the Iconik system."""
    assets_count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    file_count: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    storage_id: Optional[UUID] = None
    total_duration_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    total_size: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class CollectionBaseSchema(BaseModel):
    """Represents a CollectionBaseSchema in the Iconik system."""
    category: Optional[str] = None
    created_by_user: Optional[UUID] = None
    custom_keyframe: Optional[UUID] = None
    custom_order_status: Optional[Literal['DISABLED', 'ENABLING',
                                          'ENABLED']] = None
    custom_poster: Optional[UUID] = None
    deleted_by_user: Optional[UUID] = None
    external_id: Optional[str] = None
    favoured: Optional[bool] = None
    id: Optional[UUID] = None
    in_collections: Optional[List[UUID]] = Field(default_factory=list)
    is_root: Optional[bool] = None
    keyframe_asset_ids: Optional[List[UUID]] = Field(default_factory=list)
    keyframes: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_type: Optional[str] = None
    parent_id: Optional[UUID] = None
    parents: Optional[List[UUID]] = Field(default_factory=list)
    permissions: Optional[List[str]] = Field(default_factory=list)
    position: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    project_id: Optional[UUID] = None
    status: Optional[Literal['ACTIVE', 'HIDDEN', 'DELETED']] = None
    storage_id: Optional[UUID] = None
    title: str


class BulkShareDeleteSchema(BaseModel):
    """Represents a BulkShareDeleteSchema in the Iconik system."""
    share_ids: List[UUID]


class BulkShareCreateSchema(BaseModel):
    """Represents a BulkShareCreateSchema in the Iconik system."""
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
    emails: Optional[List[str]] = Field(default_factory=list)
    expires: Optional[datetime] = None
    id: Optional[str] = None
    is_approval: Optional[bool] = None
    message: Optional[str] = None
    metadata_views: Optional[List[str]] = Field(default_factory=list)
    object_ids: List[UUID]
    object_type: Optional[Literal['assets']] = None
    owner_id: Optional[str] = None
    password: Optional[str] = None
    share_by_url: Optional[bool] = None
    show_watermark: Optional[bool] = None
    system_domain_id: Optional[str] = None
    title: str
    upload_storage_id: Optional[UUID] = None


class BulkSetApprovalSchema(BaseModel):
    """Represents a BulkSetApprovalSchema in the Iconik system."""
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']
    status: Literal['APPROVED', 'NOT_APPROVED']


class BulkRemoveApprovalSchema(BaseModel):
    """Represents a BulkRemoveApprovalSchema in the Iconik system."""
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']


class BulkEditSegmentsSchema(BaseModel):
    """Represents a BulkEditSegmentsSchema in the Iconik system."""
    objects: List['EditSegmentForBulk']


class EditSegmentForBulk(BaseModel):
    """Represents a EditSegmentForBulk in the Iconik system."""
    asset_id: UUID
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    drawing: Optional[Any] = None
    external_id: Optional[str] = None
    face_bounding_boxes: Optional[List['FaceBoundingBox']
                                  ] = Field(default_factory=list)
    id: UUID
    keyframe_id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    path: Optional[str] = None
    person_id: Optional[UUID] = None
    project_id: Optional[UUID] = Field(
        None,
        description="ID of a project if the segment is created from a project"
    )
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = None
    segment_text: Optional[str] = None
    segment_track: Optional[str] = None
    segment_type: Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                          'TRANSCRIPTION', 'SCENE', 'PERSON']
    share_id: Optional[UUID] = Field(
        None,
        description="ID of a share if the segment is created from a share"
    )
    share_user_email: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    subclip_id: Optional[UUID] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    top_level: Optional[bool] = None
    transcription: Optional['TranscriptionType'] = None
    transcription_id: Optional[UUID] = None
    user_first_name: Optional[str] = None
    user_id: Optional[UUID] = None
    user_info: Optional['User'] = None
    user_last_name: Optional[str] = None
    user_photo: Optional[str] = None
    version_id: Optional[UUID] = None


class BulkEditAssetSegmentsSchema(BaseModel):
    """Represents a BulkEditAssetSegmentsSchema in the Iconik system."""
    objects: List['EditAssetSegment']


class EditAssetSegment(BaseModel):
    """Represents a EditAssetSegment in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    drawing: Optional[Any] = None
    external_id: Optional[str] = None
    face_bounding_boxes: Optional[List['FaceBoundingBox']
                                  ] = Field(default_factory=list)
    id: UUID
    keyframe_id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    path: Optional[str] = None
    person_id: Optional[UUID] = None
    project_id: Optional[UUID] = Field(
        None,
        description="ID of a project if the segment is created from a project"
    )
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = None
    segment_text: Optional[str] = None
    segment_track: Optional[str] = None
    segment_type: Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                          'TRANSCRIPTION', 'SCENE', 'PERSON']
    share_id: Optional[UUID] = Field(
        None,
        description="ID of a share if the segment is created from a share"
    )
    share_user_email: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    subclip_id: Optional[UUID] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    top_level: Optional[bool] = None
    transcription: Optional['TranscriptionType'] = None
    transcription_id: Optional[UUID] = None
    user_first_name: Optional[str] = None
    user_id: Optional[UUID] = None
    user_info: Optional['User'] = None
    user_last_name: Optional[str] = None
    user_photo: Optional[str] = None
    version_id: Optional[UUID] = None


class BulkDeleteSchema(BaseModel):
    """Represents a BulkDeleteSchema in the Iconik system."""
    content_only: Optional[bool] = Field(
        None,
        description=
        "If set to `False`, will also delete entities of type `object_type` specified in `object_ids`."
    )
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections', 'saved_searches']


class BulkDeleteFromFavoritesSchema(BaseModel):
    """Represents a BulkDeleteFromFavoritesSchema in the Iconik system."""
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections']


class BulkCreateSegmentsSchema(BaseModel):
    """Represents a BulkCreateSegmentsSchema in the Iconik system."""
    objects: List['Segment']


class Segment(BaseModel):
    """Represents a Segment in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    drawing: Optional[Any] = None
    external_id: Optional[str] = None
    face_bounding_boxes: Optional[List['FaceBoundingBox']
                                  ] = Field(default_factory=list)
    has_drawing: Optional[Any] = None
    id: Optional[UUID] = None
    keyframe_id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata_view_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None
    path: Optional[str] = None
    person_id: Optional[UUID] = None
    project_id: Optional[UUID] = Field(
        None,
        description="ID of a project if the segment is created from a project"
    )
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = None
    segment_text: Optional[str] = None
    segment_track: Optional[str] = None
    segment_type: Literal['MARKER', 'QC', 'GENERIC', 'COMMENT', 'TAG',
                          'TRANSCRIPTION', 'SCENE', 'PERSON']
    share_id: Optional[UUID] = Field(
        None,
        description="ID of a share if the segment is created from a share"
    )
    share_user_email: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    subclip_id: Optional[UUID] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    top_level: Optional[bool] = None
    transcription: Optional['TranscriptionType'] = None
    transcription_id: Optional[UUID] = None
    user_first_name: Optional[str] = None
    user_id: Optional[UUID] = None
    user_info: Optional['User'] = None
    user_last_name: Optional[str] = None
    user_photo: Optional[str] = None
    version_id: Optional[UUID] = None


class FaceBoundingBox(BaseModel):
    """Represents a FaceBoundingBox in the Iconik system."""
    bounding_box: Optional[List[float]] = Field(default_factory=list)
    face_id: UUID
    timestamp_ms: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class TranscriptionType(BaseModel):
    """Represents a TranscriptionType in the Iconik system."""
    speaker: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    words: List['TranscriptionElementType']


class TranscriptionElementType(BaseModel):
    """Represents a TranscriptionElementType in the Iconik system."""
    end_ms: int = Field(..., ge=-9223372036854775808, le=9223372036854775807)
    score: Optional[float] = None
    start_ms: int = Field(..., ge=-9223372036854775808, le=9223372036854775807)
    value: str


class BulkCollectionTransferSchema(BaseModel):
    """Represents a BulkCollectionTransferSchema in the Iconik system."""
    collection_ids: List[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID
    keep_collection_structure: Optional[bool] = None
    keep_parent_collection_structure: Optional[bool] = None


class BulkCollectionTranscribeSchema(BaseModel):
    """Represents a BulkCollectionTranscribeSchema in the Iconik system."""
    collection_ids: List[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID


class BulkCollectionTranscodeSchema(BaseModel):
    """Represents a BulkCollectionTranscodeSchema in the Iconik system."""
    collection_ids: List[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID


class BulkCollectionMetadataUpdateSchema(BaseModel):
    """Represents a BulkCollectionMetadataUpdateSchema in the Iconik system."""
    collection_ids: List[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID


class BulkCollectionFaceExtractionSchema(BaseModel):
    """Represents a BulkCollectionFaceExtractionSchema in the Iconik system."""
    collection_ids: List[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID


class BulkCollectionDeleteSchema(BaseModel):
    """Represents a BulkCollectionDeleteSchema in the Iconik system."""
    collection_ids: List[UUID]
    job_id: UUID
    storage_id: UUID


class BulkCollectionAnalyzeSchema(BaseModel):
    """Represents a BulkCollectionAnalyzeSchema in the Iconik system."""
    collection_ids: List[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID


class BulkCollectionActionSchema(BaseModel):
    """Represents a BulkCollectionActionSchema in the Iconik system."""
    collection_ids: List[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID


class BulkCollectionACLsUpdateSchema(BaseModel):
    """Represents a BulkCollectionACLsUpdateSchema in the Iconik system."""
    collection_ids: List[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID


class BulkAssetVersionEditSchema(BaseModel):
    """Represents a BulkAssetVersionEditSchema in the Iconik system."""
    objects: List['AssetVersionsSchema']


class BulkAssetEditSchema(BaseModel):
    """Represents a BulkAssetEditSchema in the Iconik system."""
    objects: List['AssetEditSchema']


class BulkAddToFavoritesSchema(BaseModel):
    """Represents a BulkAddToFavoritesSchema in the Iconik system."""
    object_ids: List[UUID]
    object_type: Literal['assets', 'collections']


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


class AssetsSchema(BaseModel):
    """Represents a AssetsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['AssetElasticSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class AssetsQueryParamsSchema(BaseModel):
    """Represents a AssetsQueryParamsSchema in the Iconik system."""
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


class AssetsHistoryQueryParamsSchema(BaseModel):
    """Represents a AssetsHistoryQueryParamsSchema in the Iconik system."""
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


class AssetVersionsSchema(BaseModel):
    """Represents a AssetVersionsSchema in the Iconik system."""
    asset_id: UUID
    system_domain_id: Optional[UUID] = None
    versions: Optional[List['EditAssetVersion']] = Field(default_factory=list)


class EditAssetVersion(BaseModel):
    """Represents a EditAssetVersion in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional['User'] = None
    date_created: Optional[datetime] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    has_unconfirmed_persons: Optional[bool] = None
    id: UUID
    is_online: Optional[bool] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    status: Optional[Literal['ACTIVE', 'IN_PROGRESS', 'FAILED', 'DELETING',
                             'DELETED']] = None
    transcribe_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                        'FAILED', 'DONE']] = None
    transcribed_languages: Optional[List[str]] = Field(default_factory=list)
    version_number: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class AssetVersionSchema(BaseModel):
    """Represents a AssetVersionSchema in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional['User'] = None
    date_created: Optional[datetime] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    has_unconfirmed_persons: Optional[bool] = None
    id: Optional[UUID] = None
    is_online: Optional[bool] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    status: Optional[Literal['ACTIVE', 'IN_PROGRESS', 'FAILED', 'DELETING',
                             'DELETED']] = None
    transcribe_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                        'FAILED', 'DONE']] = None
    transcribed_languages: Optional[List[str]] = Field(default_factory=list)
    version_number: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class AssetTranscriptionsPropertiesSchema(BaseModel):
    """Represents a AssetTranscriptionsPropertiesSchema in the Iconik system."""
    objects: Optional[List['AssetTranscriptionPropertiesSchema']
                      ] = Field(default_factory=list)


class AssetTranscriptionPropertiesSchema(BaseModel):
    """Represents a AssetTranscriptionPropertiesSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    id: Optional[UUID] = None
    language: Optional[str] = None
    speaker_labels: Optional[Dict[str, str]] = Field(default_factory=dict)
    system_domain_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class AssetTranscriptionFromSubtitleSchema(BaseModel):
    """Represents a AssetTranscriptionFromSubtitleSchema in the Iconik system."""
    content: Optional[str] = None
    delete_old_transcriptions: Optional[bool] = None
    format: Optional[Literal['VTT', 'WEBVTT', 'SRT']] = None
    language: Optional[str] = None
    source_subtitle_id: Optional[UUID] = Field(
        None,
        description=
        "Set to source subtitle_id or do not set and use the content fields instead"
    )


class AssetSchema(BaseModel):
    """Represents a AssetSchema in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    category: Optional[str] = None
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional[Any] = None
    custom_keyframe: Optional[UUID] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_imported: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_viewed: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    deleted_by_user_info: Optional['User'] = None
    external_id: Optional[str] = None
    external_link: Optional[HttpUrl] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    favoured: Optional[bool] = None
    has_unconfirmed_persons: Optional[bool] = None
    id: Optional[UUID] = None
    in_collections: Optional[List[str]] = Field(default_factory=list)
    is_blocked: Optional[bool] = None
    is_online: Optional[bool] = None
    last_archive_restore_date: Optional[datetime] = None
    original_asset_id: Optional[UUID] = None
    original_segment_id: Optional[UUID] = None
    original_version_id: Optional[UUID] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    site_name: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    title: str
    type: Optional[Literal['ASSET', 'SEQUENCE', 'NLE_PROJECT', 'PLACEHOLDER',
                           'CUSTOM', 'LINK', 'SUBCLIP']] = None
    updated_by_user: Optional[UUID] = None
    updated_by_user_info: Optional[Any] = None
    versions: Optional[List['AssetVersion']] = Field(default_factory=list)
    warning: Optional[str] = None


# Type alias for AssetOrCollectionSchema.
AssetOrCollectionSchema = Union['AssetElasticSchema', 'CollectionElastic']


class CollectionElastic(BaseModel):
    """Represents a CollectionElastic in the Iconik system."""
    category: Optional[str] = None
    created_by_user: Optional[UUID] = None
    custom_keyframe: Optional[UUID] = None
    custom_order_status: Optional[Literal['DISABLED', 'ENABLING',
                                          'ENABLED']] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    external_id: Optional[str] = None
    favoured: Optional[bool] = None
    id: Optional[UUID] = None
    in_collections: Optional[List[UUID]] = Field(default_factory=list)
    is_root: Optional[bool] = None
    keyframe_asset_ids: Optional[List[UUID]] = Field(default_factory=list)
    keyframes: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_type: Optional[str] = None
    parent_id: Optional[UUID] = None
    parents: Optional[List[UUID]] = Field(default_factory=list)
    permissions: Optional[List[str]] = Field(default_factory=list)
    position: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    project_id: Optional[UUID] = None
    status: Optional[Literal['ACTIVE', 'HIDDEN', 'DELETED']] = None
    storage_id: Optional[UUID] = None
    title: str


class AssetHistorySchema(BaseModel):
    """Represents a AssetHistorySchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    job_id: Optional[UUID] = None
    operation_description: Optional[str] = None
    operation_type: Literal['EXPORT', 'TRANSCODE', 'ANALYZE', 'ADD_FORMAT',
                            'DELETE_FORMAT', 'RESTORE_FORMAT', 'DELETE_FILESET',
                            'DELETE_FILE', 'RESTORE_FILESET', 'MODIFY_FILESET',
                            'APPROVE', 'REJECT', 'DOWNLOAD', 'METADATA',
                            'CUSTOM', 'TRANSCRIPTION', 'VERSION_CREATE',
                            'VERSION_DELETE', 'VERSION_UPDATE',
                            'VERSION_PROMOTE', 'RESTORE',
                            'RESTORE_FROM_GLACIER', 'ARCHIVE',
                            'RESTORE_ARCHIVE', 'DELETE', 'TRANSFER',
                            'UNLINK_SUBCLIP', 'FACE_RECOGNITION']
    share_id: Optional[UUID] = None
    share_user_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class AssetHistoryEntitiesSchema(BaseModel):
    """Represents a AssetHistoryEntitiesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['AssetHistoryElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class AssetHistoryElasticSchema(BaseModel):
    """Represents a AssetHistoryElasticSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    job_id: Optional[UUID] = None
    operation_description: Optional[str] = None
    operation_type: Literal['EXPORT', 'TRANSCODE', 'ANALYZE', 'ADD_FORMAT',
                            'DELETE_FORMAT', 'RESTORE_FORMAT', 'DELETE_FILESET',
                            'DELETE_FILE', 'RESTORE_FILESET', 'MODIFY_FILESET',
                            'APPROVE', 'REJECT', 'DOWNLOAD', 'METADATA',
                            'CUSTOM', 'TRANSCRIPTION', 'VERSION_CREATE',
                            'VERSION_DELETE', 'VERSION_UPDATE',
                            'VERSION_PROMOTE', 'RESTORE',
                            'RESTORE_FROM_GLACIER', 'ARCHIVE',
                            'RESTORE_ARCHIVE', 'DELETE', 'TRANSFER',
                            'UNLINK_SUBCLIP', 'FACE_RECOGNITION']
    share_id: Optional[UUID] = None
    share_user_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class AssetHistoryBulkSchema(BaseModel):
    """Represents a AssetHistoryBulkSchema in the Iconik system."""
    asset_ids: List[UUID]
    assets_jobs_map: Optional[Dict[str, Any]] = Field(default_factory=dict)
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    job_id: Optional[UUID] = None
    operation_description: Optional[str] = None
    operation_type: Literal['EXPORT', 'TRANSCODE', 'ANALYZE', 'ADD_FORMAT',
                            'DELETE_FORMAT', 'RESTORE_FORMAT', 'DELETE_FILESET',
                            'DELETE_FILE', 'RESTORE_FILESET', 'MODIFY_FILESET',
                            'APPROVE', 'REJECT', 'DOWNLOAD', 'METADATA',
                            'CUSTOM', 'TRANSCRIPTION', 'VERSION_CREATE',
                            'VERSION_DELETE', 'VERSION_UPDATE',
                            'VERSION_PROMOTE', 'RESTORE',
                            'RESTORE_FROM_GLACIER', 'ARCHIVE',
                            'RESTORE_ARCHIVE', 'DELETE', 'TRANSFER',
                            'UNLINK_SUBCLIP', 'FACE_RECOGNITION']
    share_id: Optional[UUID] = None
    share_user_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class AssetHistoryBaseSchema(BaseModel):
    """Represents a AssetHistoryBaseSchema in the Iconik system."""
    id: Optional[UUID] = None
    job_id: Optional[UUID] = None
    operation_description: Optional[str] = None
    operation_type: Literal['EXPORT', 'TRANSCODE', 'ANALYZE', 'ADD_FORMAT',
                            'DELETE_FORMAT', 'RESTORE_FORMAT', 'DELETE_FILESET',
                            'DELETE_FILE', 'RESTORE_FILESET', 'MODIFY_FILESET',
                            'APPROVE', 'REJECT', 'DOWNLOAD', 'METADATA',
                            'CUSTOM', 'TRANSCRIPTION', 'VERSION_CREATE',
                            'VERSION_DELETE', 'VERSION_UPDATE',
                            'VERSION_PROMOTE', 'RESTORE',
                            'RESTORE_FROM_GLACIER', 'ARCHIVE',
                            'RESTORE_ARCHIVE', 'DELETE', 'TRANSFER',
                            'UNLINK_SUBCLIP', 'FACE_RECOGNITION']
    share_id: Optional[UUID] = None
    share_user_id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    version_id: Optional[UUID] = None


class AssetElasticSchema(BaseModel):
    """Represents a AssetElasticSchema in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    ancestor_collections: Optional[List[str]] = Field(default_factory=list)
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    category: Optional[str] = None
    comments_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional[Any] = None
    custom_keyframe: Optional[UUID] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_imported: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_viewed: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    deleted_by_user_info: Optional['User'] = None
    duration_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    external_id: Optional[str] = None
    external_link: Optional[HttpUrl] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    favoured: Optional[bool] = None
    files: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    has_unconfirmed_persons: Optional[bool] = None
    id: Optional[UUID] = None
    in_collections: Optional[List[str]] = Field(default_factory=list)
    is_blocked: Optional[bool] = None
    is_online: Optional[bool] = None
    keyframes: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    last_archive_restore_date: Optional[datetime] = None
    media_type: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_type: Optional[str] = None
    original_asset_id: Optional[UUID] = None
    original_segment_id: Optional[UUID] = None
    original_version_id: Optional[UUID] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    position: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    proxies: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    relations: Optional[List['RelationElastic']] = Field(default_factory=list)
    site_name: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    title: str
    type: Optional[Literal['ASSET', 'SEQUENCE', 'NLE_PROJECT', 'PLACEHOLDER',
                           'CUSTOM', 'LINK', 'SUBCLIP']] = None
    updated_by_user: Optional[UUID] = None
    updated_by_user_info: Optional[Any] = None
    versions: Optional[List['AssetVersion']] = Field(default_factory=list)
    versions_number: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    warning: Optional[str] = None


class RelationElastic(BaseModel):
    """Represents a RelationElastic in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    related_from_asset_id: Optional[UUID] = None
    related_to_asset_id: Optional[UUID] = None
    relation_type: Optional[str] = None


class AssetVersion(BaseModel):
    """Represents a AssetVersion in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional['User'] = None
    date_created: Optional[datetime] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    has_unconfirmed_persons: Optional[bool] = None
    id: Optional[UUID] = None
    is_online: Optional[bool] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    status: Optional[Literal['ACTIVE', 'IN_PROGRESS', 'FAILED', 'DELETING',
                             'DELETED']] = None
    transcribe_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                        'FAILED', 'DONE']] = None
    transcribed_languages: Optional[List[str]] = Field(default_factory=list)
    version_number: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class AssetEditSchema(BaseModel):
    """Represents a AssetEditSchema in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    category: Optional[str] = None
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional[Any] = None
    custom_keyframe: Optional[UUID] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_imported: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_viewed: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    deleted_by_user_info: Optional['User'] = None
    external_id: Optional[str] = None
    external_link: Optional[HttpUrl] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    favoured: Optional[bool] = None
    has_unconfirmed_persons: Optional[bool] = None
    id: UUID
    is_blocked: Optional[bool] = None
    is_online: Optional[bool] = None
    last_archive_restore_date: Optional[datetime] = None
    original_asset_id: Optional[UUID] = None
    original_segment_id: Optional[UUID] = None
    original_version_id: Optional[UUID] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    site_name: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    title: Optional[str] = None
    type: Optional[Literal['ASSET', 'SEQUENCE', 'NLE_PROJECT', 'PLACEHOLDER',
                           'CUSTOM', 'LINK', 'SUBCLIP']] = None
    updated_by_user: Optional[UUID] = None
    updated_by_user_info: Optional[Any] = None
    warning: Optional[str] = None


class AssetCreateSchema(BaseModel):
    """Represents a AssetCreateSchema in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    category: Optional[str] = None
    collection_id: Optional[UUID] = None
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional[Any] = None
    custom_keyframe: Optional[UUID] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_imported: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_viewed: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    deleted_by_user_info: Optional['User'] = None
    external_id: Optional[str] = None
    external_link: Optional[HttpUrl] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    favoured: Optional[bool] = None
    has_unconfirmed_persons: Optional[bool] = None
    id: Optional[UUID] = None
    is_blocked: Optional[bool] = None
    is_online: Optional[bool] = None
    last_archive_restore_date: Optional[datetime] = None
    original_asset_id: Optional[UUID] = None
    original_segment_id: Optional[UUID] = None
    original_version_id: Optional[UUID] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    site_name: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    title: str
    type: Optional[Literal['ASSET', 'SEQUENCE', 'NLE_PROJECT', 'PLACEHOLDER',
                           'CUSTOM', 'LINK', 'SUBCLIP']] = None
    updated_by_user: Optional[UUID] = None
    updated_by_user_info: Optional[Any] = None
    warning: Optional[str] = None


class AssetBaseSchema(BaseModel):
    """Represents a AssetBaseSchema in the Iconik system."""
    analyze_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                     'FAILED', 'DONE']] = None
    archive_status: Optional[Literal['NOT_ARCHIVED', 'ARCHIVING',
                                     'FAILED_TO_ARCHIVE', 'ARCHIVED']] = None
    category: Optional[str] = None
    created_by_user: Optional[UUID] = None
    created_by_user_info: Optional[Any] = None
    custom_keyframe: Optional[UUID] = None
    custom_poster: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_imported: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_viewed: Optional[datetime] = None
    deleted_by_user: Optional[UUID] = None
    deleted_by_user_info: Optional['User'] = None
    external_id: Optional[str] = None
    external_link: Optional[HttpUrl] = None
    face_recognition_status: Optional[Literal['N/A', 'REQUESTED', 'IN_PROGRESS',
                                              'FAILED', 'DONE']] = None
    favoured: Optional[bool] = None
    has_unconfirmed_persons: Optional[bool] = None
    id: Optional[UUID] = None
    is_blocked: Optional[bool] = None
    is_online: Optional[bool] = None
    last_archive_restore_date: Optional[datetime] = None
    original_asset_id: Optional[UUID] = None
    original_segment_id: Optional[UUID] = None
    original_version_id: Optional[UUID] = None
    person_ids: Optional[List[UUID]] = Field(default_factory=list)
    site_name: Optional[str] = None
    status: Optional[Literal['ACTIVE', 'DELETED']] = None
    time_end_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    time_start_milliseconds: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    title: str
    type: Optional[Literal['ASSET', 'SEQUENCE', 'NLE_PROJECT', 'PLACEHOLDER',
                           'CUSTOM', 'LINK', 'SUBCLIP']] = None
    updated_by_user: Optional[UUID] = None
    updated_by_user_info: Optional[Any] = None
    warning: Optional[str] = None


class ApprovalsBySchema(BaseModel):
    """Represents a ApprovalsBySchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['ApprovalBySchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class ApprovalSchema(BaseModel):
    """Represents a ApprovalSchema in the Iconik system."""
    approvals_by: Optional[List['ApprovalBySchema']
                           ] = Field(default_factory=list)
    change_date: Optional[datetime] = None
    externals: Optional[List[str]] = Field(default_factory=list)
    groups: Optional[List[UUID]] = Field(default_factory=list)
    min_number: Optional[int] = Field(None, ge=1)
    object_id: Optional[UUID] = None
    object_type: Optional[str] = None
    request_date: Optional[datetime] = None
    requested_by: Optional[UUID] = None
    share_id: Optional[UUID] = None
    status: Optional[Literal['N/A', 'REQUESTED', 'APPROVED', 'NOT_APPROVED',
                             'MIXED']] = None
    user_status: Optional[Literal['N/A', 'REQUESTED', 'APPROVED',
                                  'NOT_APPROVED', 'MIXED']] = None
    users: Optional[List[UUID]] = Field(default_factory=list)
    users_info: Optional[List['User']] = Field(default_factory=list)
    version_id: Optional[UUID] = None


class User(BaseModel):
    """Represents a User in the Iconik system."""
    email: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[UUID] = None
    last_name: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None


class ApprovalJobSchema(BaseModel):
    """Represents a ApprovalJobSchema in the Iconik system."""
    job_id: Optional[UUID] = None


class ApprovalBySchema(BaseModel):
    """Represents a ApprovalBySchema in the Iconik system."""
    change_date: Optional[datetime] = None
    external: Optional[str] = None
    object_id: Optional[UUID] = None
    object_type: Optional[str] = None
    status: Optional[Literal['N/A', 'REQUESTED', 'APPROVED', 'NOT_APPROVED',
                             'MIXED']] = None
    user: Optional[UUID] = None
    version_id: Optional[UUID] = None


# Update forward references
TranscriptionTypeSchema.model_rebuild()
TranscriptionElementTypeSchema.model_rebuild()
SynchronizeCollectionKeyframesSchema.model_rebuild()
SyncSessionSchema.model_rebuild()
SyncSessionCreateSchema.model_rebuild()
StorageContentInfoSchema.model_rebuild()
SharesSchema.model_rebuild()
SharesElasticSchema.model_rebuild()
ShareUsersSchema.model_rebuild()
UserSchema.model_rebuild()
ShareUsersElasticSchema.model_rebuild()
ShareUserSchema.model_rebuild()
ShareURLSchema.model_rebuild()
ShareURLCreateSchema.model_rebuild()
ShareTokenSchema.model_rebuild()
ShareSchema.model_rebuild()
ShareRoles.model_rebuild()
ShareOptionsBaseSchema.model_rebuild()
ShareLoginSchema.model_rebuild()
ShareElasticSchema.model_rebuild()
ShareUsersElastic.model_rebuild()
ShareCreateSchema.model_rebuild()
ShareBaseSchema.model_rebuild()
SequencesSchema.model_rebuild()
SequencesQueryParamsSchema.model_rebuild()
SequenceSchema.model_rebuild()
SequenceItemsSchema.model_rebuild()
SequenceItemsQueryParamsSchema.model_rebuild()
SequenceItemUpdatePositionSchema.model_rebuild()
SequenceItemSchema.model_rebuild()
SequenceCreateSchema.model_rebuild()
SequenceBaseSchema.model_rebuild()
SegmentsSchema.model_rebuild()
SegmentSchema.model_rebuild()
SegmentQueryParamsSchema.model_rebuild()
SegmentElasticSchema.model_rebuild()
SegmentBaseSchema.model_rebuild()
SchedulePersonActionSchema.model_rebuild()
RelationsSchema.model_rebuild()
RelationsQueryParamsSchema.model_rebuild()
RelationTypesSchema.model_rebuild()
RelationTypeSchema.model_rebuild()
RelationSchema.model_rebuild()
RelationElasticSchema.model_rebuild()
ReindexShareSchema.model_rebuild()
ReindexSequenceSchema.model_rebuild()
ReindexSegmentsSchema.model_rebuild()
ReindexSegmentSchema.model_rebuild()
ReindexProjectSchema.model_rebuild()
ReindexPlaylistSchema.model_rebuild()
ReindexInheritedCollectionsACLSchema.model_rebuild()
ReindexCollectionSchema.model_rebuild()
ReindexCollectionContentSchema.model_rebuild()
ReindexBulkActionSchema.model_rebuild()
ReindexAssetSchema.model_rebuild()
ReindexAssetHistorySchema.model_rebuild()
ReindexAllSegmentsSchema.model_rebuild()
ReindexAllCollectionsSchema.model_rebuild()
ReindexAllAssetsSchema.model_rebuild()
ProjectsSchema.model_rebuild()
ProjectsQueryParamsSchema.model_rebuild()
ProjectSchema.model_rebuild()
ProjectMembersSchema.model_rebuild()
ProjectMembersQueryParamsSchema.model_rebuild()
ProjectMemberSchema.model_rebuild()
ProjectMemberCreateSchema.model_rebuild()
ProjectMemberBaseSchema.model_rebuild()
ProjectCreateSchema.model_rebuild()
ProjectBaseSchema.model_rebuild()
PlaylistsSchema.model_rebuild()
PlaylistsQueryParamsSchema.model_rebuild()
PlaylistSchema.model_rebuild()
PlaylistItemsSchema.model_rebuild()
PlaylistItemsQueryParamsSchema.model_rebuild()
PlaylistItemUpdatePositionSchema.model_rebuild()
PlaylistItemSchema.model_rebuild()
PlaylistItemElasticSchema.model_rebuild()
PlaylistCreateSchema.model_rebuild()
PlaylistItem.model_rebuild()
PlaylistBaseSchema.model_rebuild()
Playlist.model_rebuild()
ListObjectsSchema.model_rebuild()
GetShareSchema.model_rebuild()
ShareUser.model_rebuild()
GetAssetsLatestVersionSchema.model_rebuild()
FavoritesSchema.model_rebuild()
FaceBoundingBoxSchema.model_rebuild()
EditSegmentSchema.model_rebuild()
EditSegmentForBulkSchema.model_rebuild()
EditPersonStatusSchema.model_rebuild()
EditAssetVersionSchema.model_rebuild()
EditAssetSegmentSchema.model_rebuild()
DrawingSchema.model_rebuild()
DrawingPrimitiveSchema.model_rebuild()
DrawingPointSchema.model_rebuild()
Drawing.model_rebuild()
DrawingPrimitive.model_rebuild()
DrawingPoint.model_rebuild()
DeleteSegmentsSchema.model_rebuild()
DeleteQueueSchema.model_rebuild()
DeleteQueueCollectionsQueryParamsSchema.model_rebuild()
DeleteQueueAssetsQueryParamsSchema.model_rebuild()
CustomActionsSchema.model_rebuild()
CustomActionSchema.model_rebuild()
CustomActionCallbackSchema.model_rebuild()
MetadataFieldValueSchema.model_rebuild()
CustomActionCallbackReplySchema.model_rebuild()
CreateCollectionFromSavedSearchSchema.model_rebuild()
CreateCollectionFromSavedSearchResponseSchema.model_rebuild()
CreateCollectionContentOrderingSchema.model_rebuild()
CreateAssetVersionSchema.model_rebuild()
CreateAssetVersionFromVersionSchema.model_rebuild()
CreateAssetVersionFromAssetSchema.model_rebuild()
CollectionsSchema.model_rebuild()
CollectionsQueryParamsSchema.model_rebuild()
CollectionSizeSchema.model_rebuild()
CollectionSchema.model_rebuild()
CollectionInputSchema.model_rebuild()
CollectionElasticSchema.model_rebuild()
CollectionContentSchema.model_rebuild()
CollectionContentQueryParamsSchema.model_rebuild()
CollectionContentOrderingSchema.model_rebuild()
CollectionContentInfoSchema.model_rebuild()
StorageContentInfo.model_rebuild()
CollectionBaseSchema.model_rebuild()
BulkShareDeleteSchema.model_rebuild()
BulkShareCreateSchema.model_rebuild()
BulkSetApprovalSchema.model_rebuild()
BulkRemoveApprovalSchema.model_rebuild()
BulkEditSegmentsSchema.model_rebuild()
EditSegmentForBulk.model_rebuild()
BulkEditAssetSegmentsSchema.model_rebuild()
EditAssetSegment.model_rebuild()
BulkDeleteSchema.model_rebuild()
BulkDeleteFromFavoritesSchema.model_rebuild()
BulkCreateSegmentsSchema.model_rebuild()
Segment.model_rebuild()
FaceBoundingBox.model_rebuild()
TranscriptionType.model_rebuild()
TranscriptionElementType.model_rebuild()
BulkCollectionTransferSchema.model_rebuild()
BulkCollectionTranscribeSchema.model_rebuild()
BulkCollectionTranscodeSchema.model_rebuild()
BulkCollectionMetadataUpdateSchema.model_rebuild()
BulkCollectionFaceExtractionSchema.model_rebuild()
BulkCollectionDeleteSchema.model_rebuild()
BulkCollectionAnalyzeSchema.model_rebuild()
BulkCollectionActionSchema.model_rebuild()
BulkCollectionACLsUpdateSchema.model_rebuild()
BulkAssetVersionEditSchema.model_rebuild()
BulkAssetEditSchema.model_rebuild()
BulkAddToFavoritesSchema.model_rebuild()
BulkActionSchema.model_rebuild()
BaseQueryParamsSchema.model_rebuild()
AssetsSchema.model_rebuild()
AssetsQueryParamsSchema.model_rebuild()
AssetsHistoryQueryParamsSchema.model_rebuild()
AssetVersionsSchema.model_rebuild()
EditAssetVersion.model_rebuild()
AssetVersionSchema.model_rebuild()
AssetTranscriptionsPropertiesSchema.model_rebuild()
AssetTranscriptionPropertiesSchema.model_rebuild()
AssetTranscriptionFromSubtitleSchema.model_rebuild()
AssetSchema.model_rebuild()
CollectionElastic.model_rebuild()
AssetHistorySchema.model_rebuild()
AssetHistoryEntitiesSchema.model_rebuild()
AssetHistoryElasticSchema.model_rebuild()
AssetHistoryBulkSchema.model_rebuild()
AssetHistoryBaseSchema.model_rebuild()
AssetElasticSchema.model_rebuild()
RelationElastic.model_rebuild()
AssetVersion.model_rebuild()
AssetEditSchema.model_rebuild()
AssetCreateSchema.model_rebuild()
AssetBaseSchema.model_rebuild()
ApprovalsBySchema.model_rebuild()
ApprovalSchema.model_rebuild()
User.model_rebuild()
ApprovalJobSchema.model_rebuild()
ApprovalBySchema.model_rebuild()
