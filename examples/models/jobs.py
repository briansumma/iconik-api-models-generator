# pylint: disable=line-too-long
"""
Iconik Jobs Models
This module contains Pydantic models for the Iconik Jobs API.
"""
from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class RelatedObjectSchema(BaseModel):
    """Represents a RelatedObjectSchema in the Iconik system."""
    object_id: UUID
    object_type: str


class ReindexJobSchema(BaseModel):
    """Represents a ReindexJobSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


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


class JobsStateSchema(BaseModel):
    """Represents a JobsStateSchema in the Iconik system."""
    action: Literal['PAUSE', 'RESUME', 'ABORT', 'RESTART']
    job_ids: List[UUID]


class JobsSchema(BaseModel):
    """Represents a JobsSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['JobElasticSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class JobsQueryParamsSchema(BaseModel):
    """Represents a JobsQueryParamsSchema in the Iconik system."""
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


class JobsPrioritySchema(BaseModel):
    """Represents a JobsPrioritySchema in the Iconik system."""
    job_ids: List[UUID]
    priority: int = Field(..., ge=1, le=10)


class JobsBulkDeleteSchema(BaseModel):
    """Represents a JobsBulkDeleteSchema in the Iconik system."""
    job_ids: List[UUID]


class JobsBulkActionSchema(BaseModel):
    """Represents a JobsBulkActionSchema in the Iconik system."""
    job_ids: List[UUID]


class JobStepsUpdateSchema(BaseModel):
    """Represents a JobStepsUpdateSchema in the Iconik system."""
    steps: List['JobStepUpdateBulkSchema']


class JobStepsSchema(BaseModel):
    """Represents a JobStepsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['JobStepSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class JobStepUpdateSchema(BaseModel):
    """Represents a JobStepUpdateSchema in the Iconik system."""
    date_updated: Optional[datetime] = None
    error_message: Optional[str] = None
    id: Optional[UUID] = None
    label: str
    message: Optional[str] = None
    status: Literal['IN_PROGRESS', 'WAITING', 'FAILED', 'DONE', 'SKIPPED']


class JobStepUpdateBulkSchema(BaseModel):
    """Represents a JobStepUpdateBulkSchema in the Iconik system."""
    date_updated: Optional[datetime] = None
    error_message: Optional[str] = None
    id: UUID
    label: str
    message: Optional[str] = None
    status: Literal['IN_PROGRESS', 'WAITING', 'FAILED', 'DONE', 'SKIPPED']


class JobStepSchema(BaseModel):
    """Represents a JobStepSchema in the Iconik system."""
    date_updated: Optional[datetime] = None
    error_message: Optional[str] = None
    id: Optional[UUID] = None
    label: str
    message: Optional[str] = None
    status: Literal['IN_PROGRESS', 'WAITING', 'FAILED', 'DONE', 'SKIPPED']


class JobStepElasticSchema(BaseModel):
    """Represents a JobStepElasticSchema in the Iconik system."""
    date_updated: Optional[str] = None
    error_message: Optional[str] = None
    id: Optional[UUID] = None
    label: str
    message: Optional[str] = None
    status: Optional[str] = None


class JobSchema(BaseModel):
    """Represents a JobSchema in the Iconik system."""
    action_context: Optional['ActionContextSchema'] = None
    children_progress: Optional[Dict[str, 'JobChildProgressSchema']
                                ] = Field(default_factory=dict)
    completed_at: Optional[datetime] = None
    created_by: Optional[UUID] = None
    custom_type: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    error_message: Optional[str] = None
    has_children: Optional[bool] = None
    id: Optional[UUID] = None
    job_context: Optional[Dict[str, Any]] = Field(default_factory=dict)
    message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_id: Optional[UUID] = None
    object_type: Optional[str] = None
    parent_id: Optional[UUID] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    progress: Optional[int] = None
    progress_processed: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    progress_total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    related_objects: Optional[List['RelatedObject']
                              ] = Field(default_factory=list)
    started_at: Optional[datetime] = None
    status: Literal['READY', 'STARTED', 'FINISHED', 'FINISHED_WITH_WARNING',
                    'FAILED', 'WAITING', 'ABORT_PENDING', 'ABORTED', 'SKIPPED',
                    'PAUSED']
    steps: Optional[List['JobStep']] = Field(default_factory=list)
    title: str
    type: Literal['MEDIAINFO', 'TRANSCODE', 'KEYFRAMES', 'EXPORT', 'DELETE',
                  'REINDEX', 'MOVE', 'TRANSFER', 'ANALYZE', 'METADATA',
                  'CUSTOM', 'SCAN', 'ARCHIVE', 'RESTORE',
                  'RESTORE_FROM_GLACIER', 'ACL', 'COPY', 'TRANSCRIPTION',
                  'REQUEST_COLLECTION_MAP', 'COLLECTION_CUSTOM_ORDER',
                  'STORAGE_GATEWAY_FILE_INGEST', 'MARK_MISSING',
                  'FACE_RECOGNITION', 'SET_APPROVAL', 'REQUEST_APPROVAL',
                  'CHANGE_PERSON', 'CONFIRM_PERSON', 'DELETE_PERSON',
                  'AUTOMATION', 'REVIEW_REQUEST',
                  'CONVERT_SAVED_SEARCH_TO_COLLECTION']


class JobElasticSchema(BaseModel):
    """Represents a JobElasticSchema in the Iconik system."""
    action_context: Optional['ActionContextSchema'] = None
    children_progress: Optional[Dict[str, 'JobChildProgressSchema']
                                ] = Field(default_factory=dict)
    completed_at: Optional[datetime] = None
    created_by: Optional[UUID] = None
    custom_type: Optional[str] = None
    date_created: Optional[str] = None
    date_modified: Optional[str] = None
    error_message: Optional[str] = None
    has_children: Optional[bool] = None
    id: Optional[UUID] = None
    job_context: Optional[Dict[str, Any]] = Field(default_factory=dict)
    message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_id: Optional[UUID] = None
    object_type: Optional[str] = None
    parent_id: Optional[UUID] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    progress: Optional[int] = None
    progress_processed: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    progress_total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    related_objects: Optional[List['RelatedObject']
                              ] = Field(default_factory=list)
    started_at: Optional[datetime] = None
    status: Literal['READY', 'STARTED', 'FINISHED', 'FINISHED_WITH_WARNING',
                    'FAILED', 'WAITING', 'ABORT_PENDING', 'ABORTED', 'SKIPPED',
                    'PAUSED']
    steps: Optional[List['JobStepElastic']] = Field(default_factory=list)
    storage_id: Optional[UUID] = None
    title: str
    type: Literal['MEDIAINFO', 'TRANSCODE', 'KEYFRAMES', 'EXPORT', 'DELETE',
                  'REINDEX', 'MOVE', 'TRANSFER', 'ANALYZE', 'METADATA',
                  'CUSTOM', 'SCAN', 'ARCHIVE', 'RESTORE',
                  'RESTORE_FROM_GLACIER', 'ACL', 'COPY', 'TRANSCRIPTION',
                  'REQUEST_COLLECTION_MAP', 'COLLECTION_CUSTOM_ORDER',
                  'STORAGE_GATEWAY_FILE_INGEST', 'MARK_MISSING',
                  'FACE_RECOGNITION', 'SET_APPROVAL', 'REQUEST_APPROVAL',
                  'CHANGE_PERSON', 'CONFIRM_PERSON', 'DELETE_PERSON',
                  'AUTOMATION', 'REVIEW_REQUEST',
                  'CONVERT_SAVED_SEARCH_TO_COLLECTION']


class JobStepElastic(BaseModel):
    """Represents a JobStepElastic in the Iconik system."""
    date_updated: Optional[str] = None
    error_message: Optional[str] = None
    id: Optional[UUID] = None
    label: str
    message: Optional[str] = None
    status: Optional[str] = None


class JobCreateSchema(BaseModel):
    """Represents a JobCreateSchema in the Iconik system."""
    action_context: Optional['ActionContextSchema'] = None
    children_progress: Optional[Dict[str, 'JobChildProgressSchema']
                                ] = Field(default_factory=dict)
    completed_at: Optional[datetime] = None
    created_by: Optional[UUID] = None
    custom_type: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    error_message: Optional[str] = None
    has_children: Optional[bool] = None
    id: Optional[UUID] = None
    job_context: Optional[Dict[str, Any]] = Field(default_factory=dict)
    message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_id: Optional[UUID] = None
    object_type: Optional[str] = None
    parent_id: Optional[UUID] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    progress: Optional[int] = None
    progress_processed: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    progress_total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    related_objects: Optional[List['RelatedObject']
                              ] = Field(default_factory=list)
    started_at: Optional[datetime] = None
    status: Literal['READY', 'STARTED', 'FINISHED', 'FINISHED_WITH_WARNING',
                    'FAILED', 'WAITING', 'ABORT_PENDING', 'ABORTED', 'SKIPPED',
                    'PAUSED']
    steps: Optional[List['JobStep']] = Field(default_factory=list)
    title: str
    type: Literal['MEDIAINFO', 'TRANSCODE', 'KEYFRAMES', 'EXPORT', 'DELETE',
                  'REINDEX', 'MOVE', 'TRANSFER', 'ANALYZE', 'METADATA',
                  'CUSTOM', 'SCAN', 'ARCHIVE', 'RESTORE',
                  'RESTORE_FROM_GLACIER', 'ACL', 'COPY', 'TRANSCRIPTION',
                  'REQUEST_COLLECTION_MAP', 'COLLECTION_CUSTOM_ORDER',
                  'STORAGE_GATEWAY_FILE_INGEST', 'MARK_MISSING',
                  'FACE_RECOGNITION', 'SET_APPROVAL', 'REQUEST_APPROVAL',
                  'CHANGE_PERSON', 'CONFIRM_PERSON', 'DELETE_PERSON',
                  'AUTOMATION', 'REVIEW_REQUEST',
                  'CONVERT_SAVED_SEARCH_TO_COLLECTION']


class JobStep(BaseModel):
    """Represents a JobStep in the Iconik system."""
    date_updated: Optional[datetime] = None
    error_message: Optional[str] = None
    id: Optional[UUID] = None
    label: str
    message: Optional[str] = None
    status: Literal['IN_PROGRESS', 'WAITING', 'FAILED', 'DONE', 'SKIPPED']


class JobBaseSchema(BaseModel):
    """Represents a JobBaseSchema in the Iconik system."""
    action_context: Optional['ActionContextSchema'] = None
    children_progress: Optional[Dict[str, 'JobChildProgressSchema']
                                ] = Field(default_factory=dict)
    completed_at: Optional[datetime] = None
    custom_type: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    error_message: Optional[str] = None
    has_children: Optional[bool] = None
    id: Optional[UUID] = None
    job_context: Optional[Dict[str, Any]] = Field(default_factory=dict)
    message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_id: Optional[UUID] = None
    object_type: Optional[str] = None
    parent_id: Optional[UUID] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    progress: Optional[int] = None
    progress_processed: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    progress_total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    related_objects: Optional[List['RelatedObject']
                              ] = Field(default_factory=list)
    started_at: Optional[datetime] = None
    status: Literal['READY', 'STARTED', 'FINISHED', 'FINISHED_WITH_WARNING',
                    'FAILED', 'WAITING', 'ABORT_PENDING', 'ABORTED', 'SKIPPED',
                    'PAUSED']
    title: str
    type: Literal['MEDIAINFO', 'TRANSCODE', 'KEYFRAMES', 'EXPORT', 'DELETE',
                  'REINDEX', 'MOVE', 'TRANSFER', 'ANALYZE', 'METADATA',
                  'CUSTOM', 'SCAN', 'ARCHIVE', 'RESTORE',
                  'RESTORE_FROM_GLACIER', 'ACL', 'COPY', 'TRANSCRIPTION',
                  'REQUEST_COLLECTION_MAP', 'COLLECTION_CUSTOM_ORDER',
                  'STORAGE_GATEWAY_FILE_INGEST', 'MARK_MISSING',
                  'FACE_RECOGNITION', 'SET_APPROVAL', 'REQUEST_APPROVAL',
                  'CHANGE_PERSON', 'CONFIRM_PERSON', 'DELETE_PERSON',
                  'AUTOMATION', 'REVIEW_REQUEST',
                  'CONVERT_SAVED_SEARCH_TO_COLLECTION']


class RelatedObject(BaseModel):
    """Represents a RelatedObject in the Iconik system."""
    object_id: UUID
    object_type: str


class JobChildProgressSchema(BaseModel):
    """Represents a JobChildProgressSchema in the Iconik system."""
    progress_processed: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    progress_total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    status: Optional[Literal['READY', 'STARTED', 'FINISHED',
                             'FINISHED_WITH_WARNING', 'FAILED', 'WAITING',
                             'ABORT_PENDING', 'ABORTED', 'SKIPPED',
                             'PAUSED']] = None


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


class ActionContextValueSchema(BaseModel):
    """Represents a ActionContextValueSchema in the Iconik system."""
    bulk: Optional[bool] = None
    url: Optional[str] = None


class ActionContextSchema(BaseModel):
    """Represents a ActionContextSchema in the Iconik system."""
    ABORT: Optional['ActionContextValue'] = None
    CHANGE_PRIORITY: Optional['ActionContextValue'] = None
    PAUSE: Optional['ActionContextValue'] = None
    RESTART: Optional['ActionContextValue'] = None
    RESUME: Optional['ActionContextValue'] = None


class ActionContextValue(BaseModel):
    """Represents a ActionContextValue in the Iconik system."""
    bulk: Optional[bool] = None
    url: Optional[str] = None


# Update forward references
RelatedObjectSchema.model_rebuild()
ReindexJobSchema.model_rebuild()
ListObjectsSchema.model_rebuild()
JobsStateSchema.model_rebuild()
JobsSchema.model_rebuild()
JobsQueryParamsSchema.model_rebuild()
JobsPrioritySchema.model_rebuild()
JobsBulkDeleteSchema.model_rebuild()
JobsBulkActionSchema.model_rebuild()
JobStepsUpdateSchema.model_rebuild()
JobStepsSchema.model_rebuild()
JobStepUpdateSchema.model_rebuild()
JobStepUpdateBulkSchema.model_rebuild()
JobStepSchema.model_rebuild()
JobStepElasticSchema.model_rebuild()
JobSchema.model_rebuild()
JobElasticSchema.model_rebuild()
JobStepElastic.model_rebuild()
JobCreateSchema.model_rebuild()
JobStep.model_rebuild()
JobBaseSchema.model_rebuild()
RelatedObject.model_rebuild()
JobChildProgressSchema.model_rebuild()
BaseQueryParamsSchema.model_rebuild()
ActionContextValueSchema.model_rebuild()
ActionContextSchema.model_rebuild()
ActionContextValue.model_rebuild()
