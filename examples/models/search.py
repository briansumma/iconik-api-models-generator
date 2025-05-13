"""
Iconik Search Models
This module contains Pydantic models for the Iconik Search API.
"""
from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class SearchSuggestsResponseSchema(BaseModel):
    """Represents a SearchSuggestsResponseSchema in the Iconik system."""
    objects: Optional[List['SearchSuggestResponseSchema']
                      ] = Field(default_factory=list)


class SearchSuggestSchema(BaseModel):
    """Represents a SearchSuggestSchema in the Iconik system."""
    doc_types: Optional[List[Literal['assets', 'collections', 'segments',
                                     'saved_searches', 'saved_search_groups']]
                        ] = Field(default_factory=list)
    field_name: str
    metadata_view_id: Optional[UUID] = None
    query: str


class SearchSuggestResponseSchema(BaseModel):
    """Represents a SearchSuggestResponseSchema in the Iconik system."""
    value: Optional[str] = None


class SearchQueryParamsSchema(BaseModel):
    """Represents a SearchQueryParamsSchema in the Iconik system."""
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


class SearchHistorySchema(BaseModel):
    """Represents a SearchHistorySchema in the Iconik system."""
    criteria: Dict[str, Any]
    date_created: Optional[datetime] = None
    id: UUID


class SearchHistoryListSchema(BaseModel):
    """Represents a SearchHistoryListSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['SearchHistory']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class SearchHistory(BaseModel):
    """Represents a SearchHistory in the Iconik system."""
    criteria: Dict[str, Any]
    date_created: Optional[datetime] = None
    id: UUID


class SearchDocumentsSchema(BaseModel):
    """Represents a SearchDocumentsSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['SearchDocumentSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class SearchDocumentSchema(BaseModel):
    """Represents a SearchDocumentSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_type: str
    title: str


class SearchDocumentInputSchema(BaseModel):
    """Represents a SearchDocumentInputSchema in the Iconik system."""
    fields: List[Dict[str, Any]]


class SearchCriteriaSchema(BaseModel):
    """Represents a SearchCriteriaSchema in the Iconik system."""
    doc_types: Optional[List[Literal['assets', 'collections', 'segments',
                                     'saved_searches', 'saved_search_groups']]
                        ] = Field(default_factory=list)
    exclude_fields: Optional[List[str]] = Field(default_factory=list)
    facets: Optional[List[str]] = Field(default_factory=list)
    facets_filters: Optional[List['FacetFilterSchema']
                             ] = Field(default_factory=list)
    filter: Optional['CriteriaFilterSchema'] = None
    include_fields: Optional[List[str]] = Field(default_factory=list)
    metadata_view_id: Optional[UUID] = None
    query: Optional[str] = None
    search_after: Optional[List[Any]] = Field(default_factory=list)
    search_fields: Optional[List[str]] = Field(default_factory=list)
    sort: Optional[List['CriteriaSortSchema']] = Field(default_factory=list)


class SavedSearchesSchema(BaseModel):
    """Represents a SavedSearchesSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['SavedSearchElasticSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class SavedSearchSchema(BaseModel):
    """Represents a SavedSearchSchema in the Iconik system."""
    criteria: 'SearchCriteria'
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    group_id: Optional[UUID] = None
    id: Optional[UUID] = None
    name: str
    permissions: Optional[List[str]] = Field(default_factory=list)


class SavedSearchResultsSchema(BaseModel):
    """Represents a SavedSearchResultsSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    id: Optional[UUID] = None
    last_url: Optional[str] = None
    name: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['SearchDocument']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    search_criteria_document: Optional['SavedSearch'] = None
    total: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class SearchDocument(BaseModel):
    """Represents a SearchDocument in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_type: str
    title: str


class SavedSearchQueryParamsSchema(BaseModel):
    """Represents a SavedSearchQueryParamsSchema in the Iconik system."""
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


class SavedSearchGroupsSchema(BaseModel):
    """Represents a SavedSearchGroupsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['SavedSearchGroupSchema']
                      ] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class SavedSearchGroupSchema(BaseModel):
    """Represents a SavedSearchGroupSchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    name: str
    system_domain_id: Optional[UUID] = None
    user_id: Optional[UUID] = None


class SavedSearchGroupQueryParamsSchema(BaseModel):
    """Represents a SavedSearchGroupQueryParamsSchema in the Iconik system."""
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


class SavedSearchElasticSchema(BaseModel):
    """Represents a SavedSearchElasticSchema in the Iconik system."""
    criteria: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    group_id: Optional[UUID] = None
    id: Optional[UUID] = None
    name: str
    permissions: Optional[List[str]] = Field(default_factory=list)


class SavedSearchCopyFromTemplateSchema(BaseModel):
    """Represents a SavedSearchCopyFromTemplateSchema in the Iconik system."""
    from_domain: UUID
    metadata_view_map: Dict[str, UUID]
    to_domain: UUID


class SavedSearchConvertCollectionSchema(BaseModel):
    """Represents a SavedSearchConvertCollectionSchema in the Iconik system."""
    collection_id: UUID


class SavedSearch(BaseModel):
    """Represents a SavedSearch in the Iconik system."""
    criteria: 'SearchCriteria'
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    group_id: Optional[UUID] = None
    id: Optional[UUID] = None
    name: str
    permissions: Optional[List[str]] = Field(default_factory=list)


class SearchCriteria(BaseModel):
    """Represents a SearchCriteria in the Iconik system."""
    doc_types: Optional[List[Literal['assets', 'collections', 'segments',
                                     'saved_searches', 'saved_search_groups']]
                        ] = Field(default_factory=list)
    exclude_fields: Optional[List[str]] = Field(default_factory=list)
    facets: Optional[List[str]] = Field(default_factory=list)
    facets_filters: Optional[List['FacetFilterSchema']
                             ] = Field(default_factory=list)
    filter: Optional['CriteriaFilterSchema'] = None
    include_fields: Optional[List[str]] = Field(default_factory=list)
    metadata_view_id: Optional[UUID] = None
    query: Optional[str] = None
    search_after: Optional[List[Any]] = Field(default_factory=list)
    search_fields: Optional[List[str]] = Field(default_factory=list)
    sort: Optional[List['CriteriaSortSchema']] = Field(default_factory=list)


class ReindexSavedSearchSchema(BaseModel):
    """Represents a ReindexSavedSearchSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexSavedSearchGroupSchema(BaseModel):
    """Represents a ReindexSavedSearchGroupSchema in the Iconik system."""
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
    total: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class FacetFilterSchema(BaseModel):
    """Represents a FacetFilterSchema in the Iconik system."""
    name: str
    value_in: Optional[List[str]] = Field(default_factory=list)


class DiscoveryViewSettingsSchema(BaseModel):
    """Represents a DiscoveryViewSettingsSchema in the Iconik system."""
    entity_ids: List[UUID]
    id: Optional[UUID] = None
    system_domain_id: Optional[UUID] = None


class DiscoveryEntitySchema(BaseModel):
    """Represents a DiscoveryEntitySchema in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_id: UUID
    object_type: Literal['COLLECTION', 'SAVED_SEARCH']
    title: str
    user_id: str


class DiscoveryEntitiesSchema(BaseModel):
    """Represents a DiscoveryEntitiesSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['DiscoveryEntity']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    scroll_id: Optional[str] = None
    total: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class DiscoveryEntity(BaseModel):
    """Represents a DiscoveryEntity in the Iconik system."""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[UUID] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    object_id: UUID
    object_type: Literal['COLLECTION', 'SAVED_SEARCH']
    title: str
    user_id: str


class CriteriaTermSchema(BaseModel):
    """Represents a CriteriaTermSchema in the Iconik system."""
    exists: Optional[bool] = None
    missing: Optional[bool] = None
    name: str
    range: Optional['CriteriaRangeFilterSchema'] = None
    value: Optional[str] = None
    value_in: Optional[List[str]] = Field(default_factory=list)


class CriteriaSortSchema(BaseModel):
    """Represents a CriteriaSortSchema in the Iconik system."""
    name: str
    order: Optional[str] = None


class CriteriaRangeFilterSchema(BaseModel):
    """Represents a CriteriaRangeFilterSchema in the Iconik system."""
    max: Optional[str] = None
    min: Optional[str] = None
    timezone: Optional[str] = Field(
        None, description="Format: +02:00. Results returned in UTC by default"
    )


class CriteriaFilterSchema(BaseModel):
    """Represents a CriteriaFilterSchema in the Iconik system."""
    filters: Optional[List['CriteriaFilterSchema']
                      ] = Field(default_factory=list)
    operator: str
    terms: Optional[List['CriteriaTerm']] = Field(default_factory=list)


class BulkSavedSearchReindexSchema(BaseModel):
    """Represents a BulkSavedSearchReindexSchema in the Iconik system."""
    include_assets: Optional[bool] = None
    include_collections: Optional[bool] = None
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchObjectsTransferSchema(BaseModel):
    """Represents a BulkSavedSearchObjectsTransferSchema in the Iconik system."""
    include_assets: bool
    include_collections: bool
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchObjectsTranscribeSchema(BaseModel):
    """Represents a BulkSavedSearchObjectsTranscribeSchema in the Iconik system."""
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchObjectsTranscodeSchema(BaseModel):
    """Represents a BulkSavedSearchObjectsTranscodeSchema in the Iconik system."""
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchObjectsSetApprovalSchema(BaseModel):
    """Represents a BulkSavedSearchObjectsSetApprovalSchema in the Iconik system."""
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchObjectsDeleteSchema(BaseModel):
    """Represents a BulkSavedSearchObjectsDeleteSchema in the Iconik system."""
    content_only: Optional[bool] = None
    include_assets: bool
    include_collections: bool
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchObjectsAnalyzeSchema(BaseModel):
    """Represents a BulkSavedSearchObjectsAnalyzeSchema in the Iconik system."""
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchObjectsACLUpdateSchema(BaseModel):
    """Represents a BulkSavedSearchObjectsACLUpdateSchema in the Iconik system."""
    include_assets: bool
    include_collections: bool
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchMetadataUpdateSchema(BaseModel):
    """Represents a BulkSavedSearchMetadataUpdateSchema in the Iconik system."""
    include_assets: bool
    include_collections: bool
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchFilesDeleteSchema(BaseModel):
    """Represents a BulkSavedSearchFilesDeleteSchema in the Iconik system."""
    job_id: UUID
    search_ids: List[UUID]
    storage_id: UUID


class BulkSavedSearchFaceExtractionSchema(BaseModel):
    """Represents a BulkSavedSearchFaceExtractionSchema in the Iconik system."""
    include_assets: bool
    include_collections: bool
    job_id: UUID
    search_ids: List[UUID]


class BulkSavedSearchActionSchema(BaseModel):
    """Represents a BulkSavedSearchActionSchema in the Iconik system."""
    job_id: UUID
    search_ids: List[UUID]


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


class AutomationSearchCriteriaSchema(BaseModel):
    """Represents a AutomationSearchCriteriaSchema in the Iconik system."""
    automation_ids: List[UUID]
    doc_types: Optional[List[Literal['assets', 'collections', 'segments',
                                     'saved_searches', 'saved_search_groups']]
                        ] = Field(default_factory=list)
    execution_time: Optional[datetime] = None
    filter: Optional['CriteriaFilter'] = None


class CriteriaFilter(BaseModel):
    """Represents a CriteriaFilter in the Iconik system."""
    filters: Optional[List['CriteriaFilter']] = Field(default_factory=list)
    operator: str
    terms: Optional[List['CriteriaTerm']] = Field(default_factory=list)


class CriteriaTerm(BaseModel):
    """Represents a CriteriaTerm in the Iconik system."""
    exists: Optional[bool] = None
    missing: Optional[bool] = None
    name: str
    range: Optional['CriteriaRangeFilter'] = None
    value: Optional[str] = None
    value_in: Optional[List[str]] = Field(default_factory=list)


class CriteriaRangeFilter(BaseModel):
    """Represents a CriteriaRangeFilter in the Iconik system."""
    max: Optional[str] = None
    min: Optional[str] = None
    timezone: Optional[str] = Field(
        None, description="Format: +02:00. Results returned in UTC by default"
    )


# Update forward references
SearchSuggestsResponseSchema.model_rebuild()
SearchSuggestSchema.model_rebuild()
SearchSuggestResponseSchema.model_rebuild()
SearchQueryParamsSchema.model_rebuild()
SearchHistorySchema.model_rebuild()
SearchHistoryListSchema.model_rebuild()
SearchHistory.model_rebuild()
SearchDocumentsSchema.model_rebuild()
SearchDocumentSchema.model_rebuild()
SearchDocumentInputSchema.model_rebuild()
SearchCriteriaSchema.model_rebuild()
SavedSearchesSchema.model_rebuild()
SavedSearchSchema.model_rebuild()
SavedSearchResultsSchema.model_rebuild()
SearchDocument.model_rebuild()
SavedSearchQueryParamsSchema.model_rebuild()
SavedSearchGroupsSchema.model_rebuild()
SavedSearchGroupSchema.model_rebuild()
SavedSearchGroupQueryParamsSchema.model_rebuild()
SavedSearchElasticSchema.model_rebuild()
SavedSearchCopyFromTemplateSchema.model_rebuild()
SavedSearchConvertCollectionSchema.model_rebuild()
SavedSearch.model_rebuild()
SearchCriteria.model_rebuild()
ReindexSavedSearchSchema.model_rebuild()
ReindexSavedSearchGroupSchema.model_rebuild()
ListObjectsSchema.model_rebuild()
FacetFilterSchema.model_rebuild()
DiscoveryViewSettingsSchema.model_rebuild()
DiscoveryEntitySchema.model_rebuild()
DiscoveryEntitiesSchema.model_rebuild()
DiscoveryEntity.model_rebuild()
CriteriaTermSchema.model_rebuild()
CriteriaSortSchema.model_rebuild()
CriteriaRangeFilterSchema.model_rebuild()
CriteriaFilterSchema.model_rebuild()
BulkSavedSearchReindexSchema.model_rebuild()
BulkSavedSearchObjectsTransferSchema.model_rebuild()
BulkSavedSearchObjectsTranscribeSchema.model_rebuild()
BulkSavedSearchObjectsTranscodeSchema.model_rebuild()
BulkSavedSearchObjectsSetApprovalSchema.model_rebuild()
BulkSavedSearchObjectsDeleteSchema.model_rebuild()
BulkSavedSearchObjectsAnalyzeSchema.model_rebuild()
BulkSavedSearchObjectsACLUpdateSchema.model_rebuild()
BulkSavedSearchMetadataUpdateSchema.model_rebuild()
BulkSavedSearchFilesDeleteSchema.model_rebuild()
BulkSavedSearchFaceExtractionSchema.model_rebuild()
BulkSavedSearchActionSchema.model_rebuild()
BaseQueryParamsSchema.model_rebuild()
AutomationSearchCriteriaSchema.model_rebuild()
CriteriaFilter.model_rebuild()
CriteriaTerm.model_rebuild()
CriteriaRangeFilter.model_rebuild()
