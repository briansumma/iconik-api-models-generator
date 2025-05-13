"""
Iconik Metadata Models
This module contains Pydantic models for the Iconik Metadata API.
"""
from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field, HttpUrl


class SegmentsCopyMappingSchema(BaseModel):
    """Represents a SegmentsCopyMappingSchema in the Iconik system."""
    destination_object_id: UUID
    destination_version_id: UUID
    source_object_id: UUID
    source_version_id: UUID


class MetadataViewsSchema(BaseModel):
    """Represents a MetadataViewsSchema in the Iconik system."""
    objects: Optional[List['MetadataViewForListSchema']
                      ] = Field(default_factory=list)


class MetadataViewSchema(BaseModel):
    """Represents a MetadataViewSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    name: str
    view_fields: List['MetadataFieldSchema']


class MetadataViewInputSchema(BaseModel):
    """Represents a MetadataViewInputSchema in the Iconik system."""
    description: Optional[str] = None
    id: Optional[UUID] = None
    name: str
    view_fields: List['MetadataViewFieldSchema']


class MetadataViewForListSchema(BaseModel):
    """Represents a MetadataViewForListSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    name: str
    view_fields: List['MetadataViewFieldSchema']


class MetadataViewFieldSchema(BaseModel):
    """Represents a MetadataViewFieldSchema in the Iconik system."""
    auto_set: Optional[bool] = None
    hide_if_not_set: Optional[bool] = None
    label: Optional[str] = None
    mapped_field_name: Optional[str] = None
    name: str
    options: Optional[List['FieldOptionsSchema']] = Field(default_factory=list)
    read_only: Optional[bool] = None
    required: Optional[bool] = None
    source_url: Optional[HttpUrl] = Field(
        None,
        description=
        "Will be used to upload MetadataField's `options`. Cannot be set or used as long as `options` are set.  **Example**: The value is `https://external-url.com/foo/`. In that case `GET` request will be sent to `https://external-url.com/foo/?user_id=uuid1&view_id=uuid1&field_name=bar&view_name=user_view&system_domain_id=uuid1`. Please note that some query parameters were added by *iconik* to get values that were predefined in your system for each user [user_id] and view [view_id]. Metadata field name [field_name], view's name [view_name] and system domain identifier [system_domain_id] will be also passed in each request. *iconik* will successfully parse the response from that URL if it will be sent in JSON formatted string: `{\"bar\": [{\"value\": \"1\", \"label\": \"1st\"}, {\"value\": \"2\", \"label\": \"2nd\"}]}`"
    )


class MetadataValuesSchema(BaseModel):
    """Represents a MetadataValuesSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    job_id: Optional[UUID] = None
    metadata_values: Dict[str, 'MetadataFieldValueSchema']
    object_id: Optional[UUID] = None
    object_type: Optional[str] = None
    version_id: Optional[UUID] = None


class MetadataValuesObjectIdSchema(BaseModel):
    """Represents a MetadataValuesObjectIdSchema in the Iconik system."""
    id: UUID
    metadata_values: Dict[str, 'MetadataFieldValueSchema']


class MetadataValuesBatchSchema(BaseModel):
    """Represents a MetadataValuesBatchSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    metadata_values: Dict[str, 'MetadataFieldValueSchema']
    object_ids: List[UUID]
    object_type: Optional[str] = None


class MetadataFieldsSchema(BaseModel):
    """Represents a MetadataFieldsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['MetadataFieldSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class MetadataFieldSchema(BaseModel):
    """Represents a MetadataFieldSchema in the Iconik system."""
    auto_set: Optional[bool] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    field_type: str
    hide_if_not_set: Optional[bool] = None
    is_block_field: Optional[bool] = None
    is_warning_field: Optional[bool] = None
    label: str
    mapped_field_name: Optional[str] = None
    max_value: Optional[float] = None
    min_value: Optional[float] = None
    multi: Optional[bool] = None
    name: str
    options: Optional[List['FieldOptionsSchema']] = Field(default_factory=list)
    read_only: Optional[bool] = None
    representative: Optional[bool] = None
    required: Optional[bool] = None
    sortable: Optional[bool] = None
    source_url: Optional[HttpUrl] = Field(
        None,
        description=
        "Will be used to upload MetadataField's `options`. Cannot be set or used as long as `options` are set.  **Example**: The value is `https://external-url.com/foo/`. In that case `GET` request will be sent to `https://external-url.com/foo/?user_id=uuid1&view_id=uuid1&field_name=bar&view_name=user_view&system_domain_id=uuid1`. Please note that some query parameters were added by *iconik* to get values that were predefined in your system for each user [user_id] and view [view_id]. Metadata field name [field_name], view's name [view_name] and system domain identifier [system_domain_id] will be also passed in each request. *iconik* will successfully parse the response from that URL if it will be sent in JSON formatted string: `{\"bar\": [{\"value\": \"1\", \"label\": \"1st\"}, {\"value\": \"2\", \"label\": \"2nd\"}]}`"
    )
    use_as_facet: Optional[bool] = None


class MetadataFieldMappingsSchema(BaseModel):
    """Represents a MetadataFieldMappingsSchema in the Iconik system."""
    objects: Optional[List['MetadataFieldMappingSchema']
                      ] = Field(default_factory=list)


class MetadataFieldMappingUpdateSchema(BaseModel):
    """Represents a MetadataFieldMappingUpdateSchema in the Iconik system."""
    field_type: Optional[str] = None
    mapped_field_name: str = Field(..., min_length=1)
    name: Optional[str] = None


class MetadataFieldMappingSchema(BaseModel):
    """Represents a MetadataFieldMappingSchema in the Iconik system."""
    field_type: Optional[str] = None
    mapped_field_name: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)


class MetadataFieldMappingOptionsSchema(BaseModel):
    """Represents a MetadataFieldMappingOptionsSchema in the Iconik system."""
    objects: List['MetadataFieldMappingOptionSchema']


class MetadataFieldMappingOptionSchema(BaseModel):
    """Represents a MetadataFieldMappingOptionSchema in the Iconik system."""
    name: str = Field(..., min_length=1)


class MetadataFieldCreateSchema(BaseModel):
    """Represents a MetadataFieldCreateSchema in the Iconik system."""
    auto_set: Optional[bool] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    field_type: str
    hide_if_not_set: Optional[bool] = None
    is_block_field: Optional[bool] = None
    is_warning_field: Optional[bool] = None
    label: str
    mapped_field_name: Optional[str] = None
    max_value: Optional[float] = None
    min_value: Optional[float] = None
    multi: Optional[bool] = None
    name: str
    options: Optional[List['FieldOptionsSchema']] = Field(default_factory=list)
    read_only: Optional[bool] = None
    representative: Optional[bool] = None
    required: Optional[bool] = None
    sortable: Optional[bool] = None
    source_url: Optional[HttpUrl] = Field(
        None,
        description=
        "Will be used to upload MetadataField's `options`. Cannot be set or used as long as `options` are set.  **Example**: The value is `https://external-url.com/foo/`. In that case `GET` request will be sent to `https://external-url.com/foo/?user_id=uuid1&view_id=uuid1&field_name=bar&view_name=user_view&system_domain_id=uuid1`. Please note that some query parameters were added by *iconik* to get values that were predefined in your system for each user [user_id] and view [view_id]. Metadata field name [field_name], view's name [view_name] and system domain identifier [system_domain_id] will be also passed in each request. *iconik* will successfully parse the response from that URL if it will be sent in JSON formatted string: `{\"bar\": [{\"value\": \"1\", \"label\": \"1st\"}, {\"value\": \"2\", \"label\": \"2nd\"}]}`"
    )
    use_as_facet: Optional[bool] = None


class MetadataFieldBaseSchema(BaseModel):
    """Represents a MetadataFieldBaseSchema in the Iconik system."""
    auto_set: Optional[bool] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    field_type: str
    hide_if_not_set: Optional[bool] = None
    is_block_field: Optional[bool] = None
    is_warning_field: Optional[bool] = None
    mapped_field_name: Optional[str] = None
    max_value: Optional[float] = None
    min_value: Optional[float] = None
    multi: Optional[bool] = None
    options: Optional[List['FieldOptionsSchema']] = Field(default_factory=list)
    read_only: Optional[bool] = None
    representative: Optional[bool] = None
    required: Optional[bool] = None
    sortable: Optional[bool] = None
    source_url: Optional[HttpUrl] = Field(
        None,
        description=
        "Will be used to upload MetadataField's `options`. Cannot be set or used as long as `options` are set.  **Example**: The value is `https://external-url.com/foo/`. In that case `GET` request will be sent to `https://external-url.com/foo/?user_id=uuid1&view_id=uuid1&field_name=bar&view_name=user_view&system_domain_id=uuid1`. Please note that some query parameters were added by *iconik* to get values that were predefined in your system for each user [user_id] and view [view_id]. Metadata field name [field_name], view's name [view_name] and system domain identifier [system_domain_id] will be also passed in each request. *iconik* will successfully parse the response from that URL if it will be sent in JSON formatted string: `{\"bar\": [{\"value\": \"1\", \"label\": \"1st\"}, {\"value\": \"2\", \"label\": \"2nd\"}]}`"
    )
    use_as_facet: Optional[bool] = None


class MetadataCategorySchema(BaseModel):
    """Represents a MetadataCategorySchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    label: str
    name: str
    object_type: Optional[str] = None
    view_ids: Optional[List[str]] = Field(default_factory=list)
    views: Optional[List['MetadataView']] = Field(default_factory=list)


class MetadataCategoriesSchema(BaseModel):
    """Represents a MetadataCategoriesSchema in the Iconik system."""
    objects: Optional[List['MetadataCategory']] = Field(default_factory=list)


class MetadataCategory(BaseModel):
    """Represents a MetadataCategory in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    label: str
    name: str
    object_type: Optional[str] = None
    view_ids: Optional[List[str]] = Field(default_factory=list)
    views: Optional[List['MetadataView']] = Field(default_factory=list)


class MetadataView(BaseModel):
    """Represents a MetadataView in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    name: str
    view_fields: List['MetadataField']


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


class FacetFieldNamesSchema(BaseModel):
    """Represents a FacetFieldNamesSchema in the Iconik system."""
    objects: Optional[List[str]] = Field(default_factory=list)


class ExternalSourceFieldOptionsSchema(BaseModel):
    """Represents a ExternalSourceFieldOptionsSchema in the Iconik system."""
    label: Optional[str] = None
    value: Optional[str] = None


class CreateMetadataValuesBatchSchema(BaseModel):
    """Represents a CreateMetadataValuesBatchSchema in the Iconik system."""
    asset_id: Optional[UUID] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    metadata_values_object_id_mapping: List['MetadataValuesObjectId']
    object_ids: List[UUID]
    object_type: Optional[str] = None


class MetadataValuesObjectId(BaseModel):
    """Represents a MetadataValuesObjectId in the Iconik system."""
    id: UUID
    metadata_values: Dict[str, 'MetadataFieldValueSchema']


class CopySourceQueryParamsSchema(BaseModel):
    """Represents a CopySourceQueryParamsSchema in the Iconik system."""
    source_object_id: Optional[UUID] = None
    source_object_type: Optional[str] = None
    source_version_id: Optional[UUID] = None


class CollectionMetadataValuesBatchSchema(BaseModel):
    """Represents a CollectionMetadataValuesBatchSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    include_assets: bool
    include_collections: bool
    metadata_values: Dict[str, 'MetadataFieldValueSchema']
    object_ids: List[UUID]
    object_type: Optional[str] = None


class MetadataField(BaseModel):
    """Represents a MetadataField in the Iconik system."""
    auto_set: Optional[bool] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    field_type: str
    hide_if_not_set: Optional[bool] = None
    is_block_field: Optional[bool] = None
    is_warning_field: Optional[bool] = None
    label: str
    mapped_field_name: Optional[str] = None
    max_value: Optional[float] = None
    min_value: Optional[float] = None
    multi: Optional[bool] = None
    name: str
    options: Optional[List['FieldOptionsSchema']] = Field(default_factory=list)
    read_only: Optional[bool] = None
    representative: Optional[bool] = None
    required: Optional[bool] = None
    sortable: Optional[bool] = None
    source_url: Optional[HttpUrl] = Field(
        None,
        description=
        "Will be used to upload MetadataField's `options`. Cannot be set or used as long as `options` are set.  **Example**: The value is `https://external-url.com/foo/`. In that case `GET` request will be sent to `https://external-url.com/foo/?user_id=uuid1&view_id=uuid1&field_name=bar&view_name=user_view&system_domain_id=uuid1`. Please note that some query parameters were added by *iconik* to get values that were predefined in your system for each user [user_id] and view [view_id]. Metadata field name [field_name], view's name [view_name] and system domain identifier [system_domain_id] will be also passed in each request. *iconik* will successfully parse the response from that URL if it will be sent in JSON formatted string: `{\"bar\": [{\"value\": \"1\", \"label\": \"1st\"}, {\"value\": \"2\", \"label\": \"2nd\"}]}`"
    )
    use_as_facet: Optional[bool] = None


class FieldOptionsSchema(BaseModel):
    """Represents a FieldOptionsSchema in the Iconik system."""
    label: Optional[str] = None
    value: Optional[str] = None


class MetadataFieldValueSchema(BaseModel):
    """Represents a MetadataFieldValueSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    field_values: Optional[List[Dict[str, Any]]] = Field(default_factory=list)
    mode: Optional[Literal['append', 'delete', 'overwrite']] = None


class BulkMetadataDeleteSchema(BaseModel):
    """Represents a BulkMetadataDeleteSchema in the Iconik system."""
    object_ids: List[UUID]


class BulkMetadataCopySchema(BaseModel):
    """Represents a BulkMetadataCopySchema in the Iconik system."""
    object_ids_mapping: List['SegmentsCopyMapping']


class SegmentsCopyMapping(BaseModel):
    """Represents a SegmentsCopyMapping in the Iconik system."""
    destination_object_id: UUID
    destination_version_id: UUID
    source_object_id: UUID
    source_version_id: UUID


# Update forward references
SegmentsCopyMappingSchema.model_rebuild()
MetadataViewsSchema.model_rebuild()
MetadataViewSchema.model_rebuild()
MetadataViewInputSchema.model_rebuild()
MetadataViewForListSchema.model_rebuild()
MetadataViewFieldSchema.model_rebuild()
MetadataValuesSchema.model_rebuild()
MetadataValuesObjectIdSchema.model_rebuild()
MetadataValuesBatchSchema.model_rebuild()
MetadataFieldsSchema.model_rebuild()
MetadataFieldSchema.model_rebuild()
MetadataFieldMappingsSchema.model_rebuild()
MetadataFieldMappingUpdateSchema.model_rebuild()
MetadataFieldMappingSchema.model_rebuild()
MetadataFieldMappingOptionsSchema.model_rebuild()
MetadataFieldMappingOptionSchema.model_rebuild()
MetadataFieldCreateSchema.model_rebuild()
MetadataFieldBaseSchema.model_rebuild()
MetadataCategorySchema.model_rebuild()
MetadataCategoriesSchema.model_rebuild()
MetadataCategory.model_rebuild()
MetadataView.model_rebuild()
ListObjectsSchema.model_rebuild()
FacetFieldNamesSchema.model_rebuild()
ExternalSourceFieldOptionsSchema.model_rebuild()
CreateMetadataValuesBatchSchema.model_rebuild()
MetadataValuesObjectId.model_rebuild()
CopySourceQueryParamsSchema.model_rebuild()
CollectionMetadataValuesBatchSchema.model_rebuild()
MetadataField.model_rebuild()
FieldOptionsSchema.model_rebuild()
MetadataFieldValueSchema.model_rebuild()
BulkMetadataDeleteSchema.model_rebuild()
BulkMetadataCopySchema.model_rebuild()
SegmentsCopyMapping.model_rebuild()
