"""
Iconik Users Models
This module contains Pydantic models for the Iconik Users API.
"""
from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class UsersSchema(BaseModel):
    """Represents a UsersSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['UserElasticSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class UsersQueryParamsSchema(BaseModel):
    """Represents a UsersQueryParamsSchema in the Iconik system."""
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


class UsersByEmailsSchema(BaseModel):
    """Represents a UsersByEmailsSchema in the Iconik system."""
    emails: List[str]


class UserSystemMetadataSchema(BaseModel):
    """Represents a UserSystemMetadataSchema in the Iconik system."""
    saml_created: Optional[bool] = None


class UserSystemMetadata(BaseModel):
    """Represents a UserSystemMetadata in the Iconik system."""
    saml_created: Optional[bool] = None


class UserSchema(BaseModel):
    """Represents a UserSchema in the Iconik system."""
    app_id: Optional[UUID] = None
    date_checklist_completed: Optional[datetime] = None
    date_created: Optional[datetime] = None
    date_first_uploaded: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_terms_accepted: Optional[datetime] = None
    date_welcomed: Optional[datetime] = None
    description: Optional[str] = Field(
        None, description="Available only for admin users"
    )
    disable_mixpanel: Optional[bool] = None
    email: Optional[str] = None
    email_marketing_consent: Optional[bool] = None
    first_name: str
    groups: Optional[List[UUID]] = Field(default_factory=list)
    hide_email: Optional[bool] = None
    hide_phone: Optional[bool] = None
    id: Optional[UUID] = None
    identity_provider_id: Optional[UUID] = None
    is_admin: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    last_name: Optional[str] = None
    last_successful_auth: Optional[datetime] = None
    last_unsuccessful_auth: Optional[datetime] = None
    last_web_login: Optional[datetime] = None
    metadata: Optional[Any] = None
    onboarding_goal: Optional[Literal['CENTRALIZE', 'COLLABORATE',
                                      'REVISIT']] = None
    password: Optional[str] = None
    password_changed: Optional[datetime] = None
    phone: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    photo_storage_id: Optional[UUID] = None
    primary_group: Optional[UUID] = None
    status: Optional[Literal['INACTIVE', 'ACTIVE', 'BLOCKED', 'DELETED']] = None
    system_domain_id: Optional[UUID] = None
    system_domains: Optional[List[UUID]] = Field(default_factory=list)
    system_metadata: Optional[Any] = None
    system_name: Optional[str] = None
    type: Literal['POWER', 'STANDARD', 'BROWSE_ONLY', 'BROWSE_API_ONLY']


class UserSamlUpdateSchema(BaseModel):
    """Represents a UserSamlUpdateSchema in the Iconik system."""
    email: str
    first_name: Optional[str] = None
    group_names: Optional[List[str]] = Field(default_factory=list)
    identity_provider_id: Optional[UUID] = None
    last_name: Optional[str] = None


class UserSamlIdpUpdateSchema(BaseModel):
    """Represents a UserSamlIdpUpdateSchema in the Iconik system."""
    email: str
    identity_provider_id: UUID


class UserSamlCreateSchema(BaseModel):
    """Represents a UserSamlCreateSchema in the Iconik system."""
    date_checklist_completed: Optional[datetime] = None
    date_created: Optional[datetime] = None
    date_first_uploaded: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_terms_accepted: Optional[datetime] = None
    date_welcomed: Optional[datetime] = None
    email: str
    email_marketing_consent: Optional[bool] = None
    first_name: str
    group_names: Optional[List[str]] = Field(default_factory=list)
    groups: Optional[List[UUID]] = Field(default_factory=list)
    hide_email: Optional[bool] = None
    hide_phone: Optional[bool] = None
    id: Optional[UUID] = None
    identity_provider_id: Optional[UUID] = None
    is_admin: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    last_name: Optional[str] = None
    last_successful_auth: Optional[datetime] = None
    last_unsuccessful_auth: Optional[datetime] = None
    last_web_login: Optional[datetime] = None
    metadata: Optional[Any] = None
    onboarding_goal: Optional[Literal['CENTRALIZE', 'COLLABORATE',
                                      'REVISIT']] = None
    password: Optional[str] = None
    password_changed: Optional[datetime] = None
    phone: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    primary_group: Optional[UUID] = None
    status: Optional[Literal['INACTIVE', 'ACTIVE', 'BLOCKED', 'DELETED']] = None
    system_domain_id: Optional[UUID] = None
    system_domains: Optional[List[UUID]] = Field(default_factory=list)
    system_metadata: Optional[Any] = None
    system_name: Optional[str] = None
    type: Optional[Literal['POWER', 'STANDARD', 'BROWSE_ONLY',
                           'BROWSE_API_ONLY']] = None


class UserRolesSchema(BaseModel):
    """Represents a UserRolesSchema in the Iconik system."""
    objects: Optional[List[str]] = Field(default_factory=list)


class UserOTPEditMultiPlatformSchema(BaseModel):
    """Represents a UserOTPEditMultiPlatformSchema in the Iconik system."""
    email: str
    mfa_required: Optional[bool] = None
    otp_secret: Optional[str] = None
    totp_last_counter: Optional[int] = None
    totp_verified: Optional[bool] = None


class UserLoginSchema(BaseModel):
    """Represents a UserLoginSchema in the Iconik system."""
    email: str
    password: str


class UserElasticSchema(BaseModel):
    """Represents a UserElasticSchema in the Iconik system."""
    date_checklist_completed: Optional[datetime] = None
    date_created: Optional[str] = None
    date_first_uploaded: Optional[datetime] = None
    date_modified: Optional[str] = None
    date_terms_accepted: Optional[datetime] = None
    date_welcomed: Optional[datetime] = None
    description: Optional[str] = Field(
        None, description="Available only for admin users"
    )
    email: Optional[str] = None
    email_marketing_consent: Optional[bool] = None
    first_name: str
    groups: Optional[List[UUID]] = Field(default_factory=list)
    hide_email: Optional[bool] = None
    hide_phone: Optional[bool] = None
    id: Optional[UUID] = None
    identity_provider_id: Optional[UUID] = None
    is_admin: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    last_name: Optional[str] = None
    last_successful_auth: Optional[str] = None
    last_unsuccessful_auth: Optional[str] = None
    last_web_login: Optional[str] = None
    metadata: Optional[Any] = None
    onboarding_goal: Optional[Literal['CENTRALIZE', 'COLLABORATE',
                                      'REVISIT']] = None
    password: Optional[str] = None
    password_changed: Optional[datetime] = None
    phone: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    primary_group: Optional[UUID] = None
    status: Optional[Literal['INACTIVE', 'ACTIVE', 'BLOCKED', 'DELETED']] = None
    system_domain_id: Optional[UUID] = None
    system_domains: Optional[List[UUID]] = Field(default_factory=list)
    system_metadata: Optional[Any] = None
    system_name: Optional[str] = None
    type: Literal['POWER', 'STANDARD', 'BROWSE_ONLY', 'BROWSE_API_ONLY']


class UserEditSchema(BaseModel):
    """Represents a UserEditSchema in the Iconik system."""
    current_password: Optional[str] = None
    date_checklist_completed: Optional[datetime] = None
    date_first_uploaded: Optional[datetime] = None
    date_terms_accepted: Optional[datetime] = None
    date_welcomed: Optional[datetime] = None
    description: Optional[str] = Field(
        None, description="Available only for admin users"
    )
    email: Optional[str] = None
    email_marketing_consent: Optional[bool] = None
    first_name: str
    groups: Optional[List[UUID]] = Field(default_factory=list)
    hide_email: Optional[bool] = None
    hide_phone: Optional[bool] = None
    id: Optional[UUID] = None
    identity_provider_id: Optional[UUID] = None
    is_admin: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    last_name: Optional[str] = None
    last_successful_auth: Optional[datetime] = None
    last_unsuccessful_auth: Optional[datetime] = None
    last_web_login: Optional[datetime] = None
    metadata: Optional[Any] = None
    onboarding_goal: Optional[Literal['CENTRALIZE', 'COLLABORATE',
                                      'REVISIT']] = None
    password: Optional[str] = None
    password_changed: Optional[datetime] = None
    phone: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    primary_group: Optional[UUID] = None
    status: Optional[Literal['INACTIVE', 'ACTIVE', 'BLOCKED', 'DELETED']] = None
    system_domain_id: Optional[UUID] = None
    system_domains: Optional[List[UUID]] = Field(default_factory=list)
    system_metadata: Optional[Any] = None
    system_name: Optional[str] = None
    type: Literal['POWER', 'STANDARD', 'BROWSE_ONLY', 'BROWSE_API_ONLY']


class UserEditInternalSchema(BaseModel):
    """Represents a UserEditInternalSchema in the Iconik system."""
    current_password: Optional[str] = None
    date_checklist_completed: Optional[datetime] = None
    date_first_uploaded: Optional[datetime] = None
    date_terms_accepted: Optional[datetime] = None
    date_welcomed: Optional[datetime] = None
    description: Optional[str] = Field(
        None, description="Available only for admin users"
    )
    email: Optional[str] = None
    email_marketing_consent: Optional[bool] = None
    first_name: str
    groups: Optional[List[UUID]] = Field(default_factory=list)
    hide_email: Optional[bool] = None
    hide_phone: Optional[bool] = None
    id: Optional[UUID] = None
    identity_provider_id: Optional[UUID] = None
    is_admin: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    last_name: Optional[str] = None
    last_successful_auth: Optional[datetime] = None
    last_unsuccessful_auth: Optional[datetime] = None
    last_web_login: Optional[datetime] = None
    metadata: Optional[Any] = None
    onboarding_goal: Optional[Literal['CENTRALIZE', 'COLLABORATE',
                                      'REVISIT']] = None
    password: Optional[str] = None
    password_changed: Optional[datetime] = None
    phone: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    primary_group: Optional[UUID] = None
    status: Optional[Literal['INACTIVE', 'ACTIVE', 'BLOCKED', 'DELETED']] = None
    system_domain_id: Optional[UUID] = None
    system_domains: Optional[List[UUID]] = Field(default_factory=list)
    system_metadata: Optional[Any] = None
    system_name: Optional[str] = None
    type: Literal['POWER', 'STANDARD', 'BROWSE_ONLY', 'BROWSE_API_ONLY']


class UserCreateSchema(BaseModel):
    """Represents a UserCreateSchema in the Iconik system."""
    date_checklist_completed: Optional[datetime] = None
    date_created: Optional[datetime] = None
    date_first_uploaded: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_terms_accepted: Optional[datetime] = None
    date_welcomed: Optional[datetime] = None
    description: Optional[str] = Field(
        None, description="Available only for admin users"
    )
    email: str
    email_marketing_consent: Optional[bool] = None
    first_name: str
    groups: Optional[List[UUID]] = Field(default_factory=list)
    hide_email: Optional[bool] = None
    hide_phone: Optional[bool] = None
    id: Optional[UUID] = None
    identity_provider_id: Optional[UUID] = None
    is_admin: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    last_name: Optional[str] = None
    last_successful_auth: Optional[datetime] = None
    last_unsuccessful_auth: Optional[datetime] = None
    last_web_login: Optional[datetime] = None
    metadata: Optional[Any] = None
    onboarding_goal: Optional[Literal['CENTRALIZE', 'COLLABORATE',
                                      'REVISIT']] = None
    password: Optional[str] = None
    password_changed: Optional[datetime] = None
    phone: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    primary_group: Optional[UUID] = None
    status: Optional[Literal['INACTIVE', 'ACTIVE', 'BLOCKED', 'DELETED']] = None
    system_domain_id: Optional[UUID] = None
    system_domains: Optional[List[UUID]] = Field(default_factory=list)
    system_metadata: Optional[Any] = None
    system_name: Optional[str] = None
    type: Literal['POWER', 'STANDARD', 'BROWSE_ONLY', 'BROWSE_API_ONLY']


class UserByEmailSchema(BaseModel):
    """Represents a UserByEmailSchema in the Iconik system."""
    email: str


class UserByEmailAndLoginTypeSchema(BaseModel):
    """Represents a UserByEmailAndLoginTypeSchema in the Iconik system."""
    email: str
    login_type: Optional[Literal['SSO', 'PASSWORD']] = None


class UserBaseSchema(BaseModel):
    """Represents a UserBaseSchema in the Iconik system."""
    date_checklist_completed: Optional[datetime] = None
    date_first_uploaded: Optional[datetime] = None
    date_terms_accepted: Optional[datetime] = None
    date_welcomed: Optional[datetime] = None
    email: Optional[str] = None
    email_marketing_consent: Optional[bool] = None
    first_name: str
    groups: Optional[List[UUID]] = Field(default_factory=list)
    hide_email: Optional[bool] = None
    hide_phone: Optional[bool] = None
    id: Optional[UUID] = None
    identity_provider_id: Optional[UUID] = None
    is_admin: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    last_name: Optional[str] = None
    last_successful_auth: Optional[datetime] = None
    last_unsuccessful_auth: Optional[datetime] = None
    last_web_login: Optional[datetime] = None
    metadata: Optional[Any] = None
    onboarding_goal: Optional[Literal['CENTRALIZE', 'COLLABORATE',
                                      'REVISIT']] = None
    password: Optional[str] = None
    password_changed: Optional[datetime] = None
    phone: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    primary_group: Optional[UUID] = None
    status: Optional[Literal['INACTIVE', 'ACTIVE', 'BLOCKED', 'DELETED']] = None
    system_domain_id: Optional[UUID] = None
    system_domains: Optional[List[UUID]] = Field(default_factory=list)
    system_metadata: Optional[Any] = None
    system_name: Optional[str] = None
    type: Literal['POWER', 'STANDARD', 'BROWSE_ONLY', 'BROWSE_API_ONLY']


class RoleCategoriesSchema(BaseModel):
    """Represents a RoleCategoriesSchema in the Iconik system."""
    assets_edit: Optional[bool] = None
    billing: Optional[bool] = None
    collaborate: Optional[bool] = None
    core: Optional[bool] = None
    download: Optional[bool] = None
    integrations_admin: Optional[bool] = None
    metadata_admin: Optional[bool] = None
    organize: Optional[bool] = None
    others: Optional[bool] = None
    storage_admin: Optional[bool] = None
    upload: Optional[bool] = None
    users_groups_admin: Optional[bool] = None


class RoleCategories(BaseModel):
    """Represents a RoleCategories in the Iconik system."""
    assets_edit: Optional[bool] = None
    billing: Optional[bool] = None
    collaborate: Optional[bool] = None
    core: Optional[bool] = None
    download: Optional[bool] = None
    integrations_admin: Optional[bool] = None
    metadata_admin: Optional[bool] = None
    organize: Optional[bool] = None
    others: Optional[bool] = None
    storage_admin: Optional[bool] = None
    upload: Optional[bool] = None
    users_groups_admin: Optional[bool] = None


class ReindexUserSchema(BaseModel):
    """Represents a ReindexUserSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class ReindexGroupSchema(BaseModel):
    """Represents a ReindexGroupSchema in the Iconik system."""
    sync_to_another_dc: Optional[bool] = None


class OtpSchema(BaseModel):
    """Represents a OtpSchema in the Iconik system."""
    otp: str
    otp_type: Literal['TOTP', 'MAIL_2SV']


class OtpInternalSchema(BaseModel):
    """Represents a OtpInternalSchema in the Iconik system."""
    email: str
    otp: str
    otp_type: Literal['TOTP', 'MAIL_2SV']


class OtpGenerateInternalSchema(BaseModel):
    """Represents a OtpGenerateInternalSchema in the Iconik system."""
    email: str


class OtpEditSchema(BaseModel):
    """Represents a OtpEditSchema in the Iconik system."""
    mfa_required: Optional[bool] = None
    otp: str
    otp_type: Literal['TOTP', 'MAIL_2SV']


class OtpEditInternalSchema(BaseModel):
    """Represents a OtpEditInternalSchema in the Iconik system."""
    email: str
    mfa_required: Optional[bool] = None


class MultiplatformUserSchema(BaseModel):
    """Represents a MultiplatformUserSchema in the Iconik system."""
    email: str


class MultiplatformUserPasswordEditSchema(BaseModel):
    """Represents a MultiplatformUserPasswordEditSchema in the Iconik system."""
    current_password: Optional[str] = None
    email: str
    ignore_current_password: Optional[bool] = None
    password: str


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


class GroupsSchema(BaseModel):
    """Represents a GroupsSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['GroupElasticSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class GroupsQueryParamsSchema(BaseModel):
    """Represents a GroupsQueryParamsSchema in the Iconik system."""
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


class GroupSchema(BaseModel):
    """Represents a GroupSchema in the Iconik system."""
    alias: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    default_user_type: Optional[str] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    id: Optional[UUID] = None
    is_saml_group: Optional[bool] = None
    logo: Optional[str] = None
    name: str
    role_categories: Optional[Any] = None
    roles: Optional[List[str]] = Field(default_factory=list)
    saml_primary_group_priority: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )


class GroupMappingsSchema(BaseModel):
    """Represents a GroupMappingsSchema in the Iconik system."""
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List['GroupMappingSchema']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class GroupMappingSchema(BaseModel):
    """Represents a GroupMappingSchema in the Iconik system."""
    group_id: UUID
    name: str


class GroupElasticSchema(BaseModel):
    """Represents a GroupElasticSchema in the Iconik system."""
    alias: Optional[str] = None
    date_created: Optional[str] = None
    date_modified: Optional[str] = None
    default_user_type: Optional[str] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    id: Optional[UUID] = None
    is_saml_group: Optional[bool] = None
    logo: Optional[str] = None
    name: str
    role_categories: Optional[Any] = None
    roles: Optional[List[str]] = Field(default_factory=list)
    saml_primary_group_priority: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )


class GroupCreateSchema(BaseModel):
    """Represents a GroupCreateSchema in the Iconik system."""
    alias: Optional[str] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    default_user_type: Optional[str] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    id: Optional[UUID] = None
    is_saml_group: Optional[bool] = None
    logo: Optional[str] = None
    name: str
    role_categories: Optional[Any] = None
    roles: Optional[List[str]] = Field(default_factory=list)
    saml_primary_group_priority: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    system_domain_id: UUID


class GroupBaseSchema(BaseModel):
    """Represents a GroupBaseSchema in the Iconik system."""
    alias: Optional[str] = None
    default_user_type: Optional[str] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    id: Optional[UUID] = None
    is_saml_group: Optional[bool] = None
    logo: Optional[str] = None
    name: str
    role_categories: Optional[Any] = None
    roles: Optional[List[str]] = Field(default_factory=list)
    saml_primary_group_priority: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )


class DomainUsersByEmailSchema(BaseModel):
    """Represents a DomainUsersByEmailSchema in the Iconik system."""
    facets: Optional[Dict[str, Any]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    mfa_methods: Optional[List[Literal['TOTP', 'MAIL_2SV']]
                          ] = Field(default_factory=list)
    mfa_required: Optional[bool] = None
    next_url: Optional[str] = None
    objects: Optional[List['UserElastic']] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )


class UserElastic(BaseModel):
    """Represents a UserElastic in the Iconik system."""
    date_checklist_completed: Optional[datetime] = None
    date_created: Optional[str] = None
    date_first_uploaded: Optional[datetime] = None
    date_modified: Optional[str] = None
    date_terms_accepted: Optional[datetime] = None
    date_welcomed: Optional[datetime] = None
    description: Optional[str] = Field(
        None, description="Available only for admin users"
    )
    email: Optional[str] = None
    email_marketing_consent: Optional[bool] = None
    first_name: str
    groups: Optional[List[UUID]] = Field(default_factory=list)
    hide_email: Optional[bool] = None
    hide_phone: Optional[bool] = None
    id: Optional[UUID] = None
    identity_provider_id: Optional[UUID] = None
    is_admin: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    last_name: Optional[str] = None
    last_successful_auth: Optional[str] = None
    last_unsuccessful_auth: Optional[str] = None
    last_web_login: Optional[str] = None
    metadata: Optional[Any] = None
    onboarding_goal: Optional[Literal['CENTRALIZE', 'COLLABORATE',
                                      'REVISIT']] = None
    password: Optional[str] = None
    password_changed: Optional[datetime] = None
    phone: Optional[str] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_small: Optional[str] = None
    primary_group: Optional[UUID] = None
    status: Optional[Literal['INACTIVE', 'ACTIVE', 'BLOCKED', 'DELETED']] = None
    system_domain_id: Optional[UUID] = None
    system_domains: Optional[List[UUID]] = Field(default_factory=list)
    system_metadata: Optional[Any] = None
    system_name: Optional[str] = None
    type: Literal['POWER', 'STANDARD', 'BROWSE_ONLY', 'BROWSE_API_ONLY']


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


# Update forward references
UsersSchema.model_rebuild()
UsersQueryParamsSchema.model_rebuild()
UsersByEmailsSchema.model_rebuild()
UserSystemMetadataSchema.model_rebuild()
UserSystemMetadata.model_rebuild()
UserSchema.model_rebuild()
UserSamlUpdateSchema.model_rebuild()
UserSamlIdpUpdateSchema.model_rebuild()
UserSamlCreateSchema.model_rebuild()
UserRolesSchema.model_rebuild()
UserOTPEditMultiPlatformSchema.model_rebuild()
UserLoginSchema.model_rebuild()
UserElasticSchema.model_rebuild()
UserEditSchema.model_rebuild()
UserEditInternalSchema.model_rebuild()
UserCreateSchema.model_rebuild()
UserByEmailSchema.model_rebuild()
UserByEmailAndLoginTypeSchema.model_rebuild()
UserBaseSchema.model_rebuild()
RoleCategoriesSchema.model_rebuild()
RoleCategories.model_rebuild()
ReindexUserSchema.model_rebuild()
ReindexGroupSchema.model_rebuild()
OtpSchema.model_rebuild()
OtpInternalSchema.model_rebuild()
OtpGenerateInternalSchema.model_rebuild()
OtpEditSchema.model_rebuild()
OtpEditInternalSchema.model_rebuild()
MultiplatformUserSchema.model_rebuild()
MultiplatformUserPasswordEditSchema.model_rebuild()
ListObjectsSchema.model_rebuild()
GroupsSchema.model_rebuild()
GroupsQueryParamsSchema.model_rebuild()
GroupSchema.model_rebuild()
GroupMappingsSchema.model_rebuild()
GroupMappingSchema.model_rebuild()
GroupElasticSchema.model_rebuild()
GroupCreateSchema.model_rebuild()
GroupBaseSchema.model_rebuild()
DomainUsersByEmailSchema.model_rebuild()
UserElastic.model_rebuild()
BaseQueryParamsSchema.model_rebuild()
