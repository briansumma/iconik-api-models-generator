"""
Iconik Notifications Models
This module contains Pydantic models for the Iconik Notifications API.
"""
from __future__ import annotations
from datetime import datetime
from typing import Dict, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class WebhooksSchema(BaseModel):
    """Represents a WebhooksSchema in the Iconik system."""
    objects: Optional[List['WebhookSchema']] = Field(default_factory=list)


class WebhookSchema(BaseModel):
    """Represents a WebhookSchema in the Iconik system."""
    name: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    last_error: Optional[str] = None
    first_failed_at: Optional[datetime] = None
    status: Literal['ENABLED', 'DISABLED', 'FAILING', 'DELETED']
    url: str = Field(
        ...,
        description="URL you want to be called when notification is appeared"
    )
    object_id: Optional[UUID] = Field(
        None, description="ID of a particular object you want to subscribe on"
    )
    id: UUID
    query: Optional[str] = Field(
        None,
        description=
        "Adding a query allows filtering out messages so webhooks will be called only if for messages that match this query."
    )
    realm: Optional[str] = Field(
        None,
        description="Realm of event. Example entity, contents, acls, metadata"
    )
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    headers: Optional[Dict[str, str]] = Field(default_factory=dict)
    operation: Optional[str] = Field(
        None, description="Operation of event. Example create, update, delete"
    )
    event_type: str = Field(
        ..., description="Type of events. Example assets, collections"
    )
    last_payload: Optional[str] = None


class WebhookInternalSchema(BaseModel):
    """Represents a WebhookInternalSchema in the Iconik system."""
    name: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    last_error: Optional[str] = None
    first_failed_at: Optional[datetime] = None
    status: Literal['ENABLED', 'DISABLED', 'FAILING', 'DELETED']
    url: str = Field(
        ...,
        description="URL you want to be called when notification is appeared"
    )
    object_id: Optional[UUID] = Field(
        None, description="ID of a particular object you want to subscribe on"
    )
    id: UUID
    query: Optional[str] = Field(
        None,
        description=
        "Adding a query allows filtering out messages so webhooks will be called only if for messages that match this query."
    )
    realm: Optional[str] = Field(
        None,
        description="Realm of event. Example entity, contents, acls, metadata"
    )
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    headers: Optional[str] = None
    operation: Optional[str] = Field(
        None, description="Operation of event. Example create, update, delete"
    )
    event_type: str = Field(
        ..., description="Type of events. Example assets, collections"
    )
    last_payload: Optional[str] = None


class WebhookCreateSchema(BaseModel):
    """Represents a WebhookCreateSchema in the Iconik system."""
    name: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    last_error: Optional[str] = None
    first_failed_at: Optional[datetime] = None
    status: Literal['ENABLED', 'DISABLED', 'FAILING', 'DELETED']
    url: str = Field(
        ...,
        description="URL you want to be called when notification is appeared"
    )
    object_id: Optional[UUID] = Field(
        None, description="ID of a particular object you want to subscribe on"
    )
    id: Optional[UUID] = None
    query: Optional[str] = Field(
        None,
        description=
        "Adding a query allows filtering out messages so webhooks will be called only if for messages that match this query."
    )
    realm: Optional[str] = Field(
        None,
        description="Realm of event. Example entity, contents, acls, metadata"
    )
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    headers: Optional[Dict[str, str]] = Field(default_factory=dict)
    operation: Optional[str] = Field(
        None, description="Operation of event. Example create, update, delete"
    )
    event_type: str = Field(
        ..., description="Type of events. Example assets, collections"
    )
    last_payload: Optional[str] = None


class WebhookBaseSchema(BaseModel):
    """Represents a WebhookBaseSchema in the Iconik system."""
    name: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    last_error: Optional[str] = None
    first_failed_at: Optional[datetime] = None
    status: Literal['ENABLED', 'DISABLED', 'FAILING', 'DELETED']
    url: str = Field(
        ...,
        description="URL you want to be called when notification is appeared"
    )
    object_id: Optional[UUID] = Field(
        None, description="ID of a particular object you want to subscribe on"
    )
    id: UUID
    query: Optional[str] = Field(
        None,
        description=
        "Adding a query allows filtering out messages so webhooks will be called only if for messages that match this query."
    )
    realm: Optional[str] = Field(
        None,
        description="Realm of event. Example entity, contents, acls, metadata"
    )
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    headers: Optional[Dict[str, str]] = Field(default_factory=dict)
    operation: Optional[str] = Field(
        None, description="Operation of event. Example create, update, delete"
    )
    event_type: str = Field(
        ..., description="Type of events. Example assets, collections"
    )
    last_payload: Optional[str] = None


# Update forward references
WebhooksSchema.model_rebuild()
WebhookSchema.model_rebuild()
WebhookInternalSchema.model_rebuild()
WebhookCreateSchema.model_rebuild()
WebhookBaseSchema.model_rebuild()
