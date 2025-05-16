# pylint: disable=line-too-long
"""
Iconik Settings Models
This module contains Pydantic models for the Iconik Settings API.
"""
from __future__ import annotations
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class WatermarkOptionsTypeSchema(BaseModel):
    """Represents a WatermarkOptionsTypeSchema in the Iconik system."""
    custom_text: Optional[str] = None
    include_custom_text: Optional[bool] = None
    include_date_time: Optional[bool] = None
    include_email: Optional[bool] = None
    include_ip_address: Optional[bool] = None
    shadow_opacity: Optional[float] = Field(None, ge=0, le=1)
    show_watermark: Optional[bool] = None
    text_appearance: Optional[Literal['top', 'center', 'bottom']] = None
    text_opacity: Optional[float] = Field(None, ge=0, le=1)


class WatermarkOptionsType(BaseModel):
    """Represents a WatermarkOptionsType in the Iconik system."""
    custom_text: Optional[str] = None
    include_custom_text: Optional[bool] = None
    include_date_time: Optional[bool] = None
    include_email: Optional[bool] = None
    include_ip_address: Optional[bool] = None
    shadow_opacity: Optional[float] = Field(None, ge=0, le=1)
    show_watermark: Optional[bool] = None
    text_appearance: Optional[Literal['top', 'center', 'bottom']] = None
    text_opacity: Optional[float] = Field(None, ge=0, le=1)


class UserSettingSchema(BaseModel):
    """Represents a UserSettingSchema in the Iconik system."""
    acl_template_id: Optional[UUID] = None
    allowed_ips: Optional[List['AllowedIPSchema']] = Field(default_factory=list)
    append_asset_uuid_to_downloads: Optional[bool] = None
    asset_default_sections: Optional[List[str]] = Field(default_factory=list)
    client_ip: Optional[str] = None
    collections_get_parent_acls: Optional[bool] = None
    date_format: Optional[str] = None
    datetime_format: Optional[str] = None
    default_upload_storage_id: Optional[UUID] = None
    delete_grace_period: Optional[int] = Field(
        None,
        ge=0,
        le=87600,
        description=
        "Grace period that indicate how long objects will live in recycle bin. Unit: hours"
    )
    facet_fields: Optional[List['FacetFieldSchema']
                           ] = Field(default_factory=list)
    filters_default_metadata_view_id: Optional[UUID] = None
    genesis: Optional[str] = None
    hide_favourites: Optional[bool] = None
    home_page: Optional[str] = None
    jobs_dashboard: Optional[Any] = None
    search_auto_resize_title_column: Optional[bool] = None
    search_default_sections: Optional[List[str]] = Field(default_factory=list)
    search_display_fields: Optional[List['SearchDisplayFieldSchema']
                                    ] = Field(default_factory=list)
    search_in_transcriptions: Optional[bool] = None
    search_results_asset_metadata_view_id: Optional[UUID] = None
    search_results_collection_metadata_view_id: Optional[UUID] = None
    share_expiration_time: Optional[int] = Field(
        None,
        ge=0,
        le=3650,
        description=
        "Default share expiration time that indicate how long share will be valid. Unit: days"
    )
    show_persons_confirmation_modal: Optional[bool] = None
    use_asset_name_on_download: Optional[bool] = None


class UserSettingRemoveAttributesSchema(BaseModel):
    """Represents a UserSettingRemoveAttributesSchema in the Iconik system."""
    allowed_ips: Optional[List['AllowedIPSchema']] = Field(default_factory=list)
    asset_default_sections: Optional[List[str]] = Field(default_factory=list)
    facet_fields: Optional[List['FacetFieldSchema']
                           ] = Field(default_factory=list)
    jobs_dashboard: Optional[Any] = None
    search_default_sections: Optional[List[str]] = Field(default_factory=list)
    search_display_fields: Optional[List['SearchDisplayFieldSchema']
                                    ] = Field(default_factory=list)
    user_ids: List[UUID]


class SystemSettingSchema(BaseModel):
    """Represents a SystemSettingSchema in the Iconik system."""
    acl_template_id: Optional[UUID] = None
    allow_play_original_during_transcoding: Optional[bool] = Field(
        None,
        description=
        "Allow playing the original file while transcoding is in progress."
    )
    allowed_ips: Optional[List['AllowedIPSchema']] = Field(default_factory=list)
    append_asset_uuid_to_downloads: Optional[bool] = None
    asset_default_sections: Optional[List[str]] = Field(default_factory=list)
    client_ip: Optional[str] = None
    collections_get_parent_acls: Optional[bool] = None
    cors_hosts: Optional[List[str]] = Field(default_factory=list)
    date_format: Optional[str] = None
    datetime_format: Optional[str] = None
    default_share_options: Optional[Any] = None
    default_upload_storage_id: Optional[UUID] = None
    delete_grace_period: Optional[int] = Field(
        None,
        ge=0,
        le=87600,
        description=
        "Grace period that indicate how long objects will live in recycle bin. Unit: hours"
    )
    enable_shield: Optional[bool] = None
    external_share: Optional[bool] = None
    facet_fields: Optional[List['FacetFieldSchema']
                           ] = Field(default_factory=list)
    filters_default_metadata_view_id: Optional[UUID] = None
    hide_favourites: Optional[bool] = None
    home_page: Optional[str] = None
    image_properties_metadata_field: Optional[str] = None
    jobs_dashboard: Optional[Any] = None
    locations_metadata_field: Optional[str] = None
    lock_mapped_collections: Optional[bool] = Field(
        None,
        description="Forbid regular users to edit or delete mapped collections."
    )
    logo_storage_id: Optional[UUID] = None
    logo_url: Optional[str] = None
    logos_metadata_field: Optional[str] = None
    max_browse_users: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    max_power_users: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    max_standard_users: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    max_storage_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    max_traffic_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    mfa_methods: Optional[List[Literal['TOTP', 'MAIL_2SV']]
                          ] = Field(default_factory=list)
    mfa_required: Optional[bool] = None
    password_checks: Optional[Any] = None
    required_metadata_views: Optional[List[str]] = Field(default_factory=list)
    safe_searches_metadata_field: Optional[str] = None
    saml_require_groups: Optional[bool] = None
    search_auto_resize_title_column: Optional[bool] = None
    search_default_sections: Optional[List[str]] = Field(default_factory=list)
    search_display_fields: Optional[List['SearchDisplayFieldSchema']
                                    ] = Field(default_factory=list)
    search_in_transcriptions: Optional[bool] = None
    search_results_asset_metadata_view_id: Optional[UUID] = None
    search_results_collection_metadata_view_id: Optional[UUID] = None
    search_users_from_share: Optional[bool] = None
    share_expiration_time: Optional[int] = Field(
        None,
        ge=0,
        le=3650,
        description=
        "Default share expiration time that indicate how long share will be valid. Unit: days"
    )
    support_access: Optional[bool] = None
    system_domain_id: Optional[UUID] = None
    system_domain_name: Optional[str] = None
    tags_metadata_field: Optional[str] = None
    texts_metadata_field: Optional[str] = None
    update_saml_primary_group_on_login: Optional[bool] = None
    use_asset_name_on_download: Optional[bool] = None
    watermark_options: Optional[Any] = None


class SystemSettingPublicSchema(BaseModel):
    """Represents a SystemSettingPublicSchema in the Iconik system."""
    acl_template_id: Optional[UUID] = None
    allow_play_original_during_transcoding: Optional[bool] = Field(
        None,
        description=
        "Allow playing the original file while transcoding is in progress."
    )
    allowed_ips: Optional[List['AllowedIPSchema']] = Field(default_factory=list)
    append_asset_uuid_to_downloads: Optional[bool] = None
    asset_default_sections: Optional[List[str]] = Field(default_factory=list)
    client_ip: Optional[str] = None
    collections_get_parent_acls: Optional[bool] = None
    cors_hosts: Optional[List[str]] = Field(default_factory=list)
    custom_terms: Optional[bool] = None
    date_format: Optional[str] = None
    datetime_format: Optional[str] = None
    default_share_options: Optional[Any] = None
    default_upload_storage_id: Optional[UUID] = None
    delete_grace_period: Optional[int] = Field(
        None,
        ge=0,
        le=87600,
        description=
        "Grace period that indicate how long objects will live in recycle bin. Unit: hours"
    )
    disable_billing_page: Optional[bool] = None
    domain_has_preloaded_assets: Optional[bool] = None
    enable_shield: Optional[bool] = None
    external_share: Optional[bool] = None
    facet_fields: Optional[List['FacetFieldSchema']
                           ] = Field(default_factory=list)
    features: Optional[List[str]] = Field(default_factory=list)
    filters_default_metadata_view_id: Optional[UUID] = None
    hide_favourites: Optional[bool] = None
    home_page: Optional[str] = None
    image_properties_metadata_field: Optional[str] = None
    is_plg_domain: Optional[bool] = None
    jobs_dashboard: Optional[Any] = None
    locations_metadata_field: Optional[str] = None
    lock_mapped_collections: Optional[bool] = Field(
        None,
        description="Forbid regular users to edit or delete mapped collections."
    )
    logo_storage_id: Optional[UUID] = None
    logo_url: Optional[str] = None
    logos_metadata_field: Optional[str] = None
    max_browse_users: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    max_power_users: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    max_standard_users: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    max_storage_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    max_traffic_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    mfa_methods: Optional[List[Literal['TOTP', 'MAIL_2SV']]
                          ] = Field(default_factory=list)
    mfa_required: Optional[bool] = None
    password_checks: Optional[Any] = None
    required_metadata_views: Optional[List[str]] = Field(default_factory=list)
    safe_searches_metadata_field: Optional[str] = None
    saml_require_groups: Optional[bool] = None
    search_auto_resize_title_column: Optional[bool] = None
    search_default_sections: Optional[List[str]] = Field(default_factory=list)
    search_display_fields: Optional[List['SearchDisplayFieldSchema']
                                    ] = Field(default_factory=list)
    search_in_transcriptions: Optional[bool] = None
    search_results_asset_metadata_view_id: Optional[UUID] = None
    search_results_collection_metadata_view_id: Optional[UUID] = None
    search_users_from_share: Optional[bool] = None
    share_expiration_time: Optional[int] = Field(
        None,
        ge=0,
        le=3650,
        description=
        "Default share expiration time that indicate how long share will be valid. Unit: days"
    )
    support_access: Optional[bool] = None
    system_domain_id: Optional[UUID] = None
    system_domain_name: Optional[str] = None
    tags_metadata_field: Optional[str] = None
    texts_metadata_field: Optional[str] = None
    update_saml_primary_group_on_login: Optional[bool] = None
    use_asset_name_on_download: Optional[bool] = None
    watermark_options: Optional[Any] = None


class SortSchema(BaseModel):
    """Represents a SortSchema in the Iconik system."""
    name: str
    order: Optional[Literal['asc', 'desc']] = None


class SearchDisplayFieldSchema(BaseModel):
    """Represents a SearchDisplayFieldSchema in the Iconik system."""
    name: str


class PasswordChecksTypeSchema(BaseModel):
    """Represents a PasswordChecksTypeSchema in the Iconik system."""
    digits: Optional[int] = Field(None, ge=0)
    lowercase: Optional[int] = Field(None, ge=0)
    max_length: Optional[int] = Field(None, ge=8, le=64)
    min_length: Optional[int] = Field(None, ge=8, le=56)
    special_symbols: Optional[int] = Field(None, ge=0)
    uppercase: Optional[int] = Field(None, ge=0)


class PasswordChecksType(BaseModel):
    """Represents a PasswordChecksType in the Iconik system."""
    digits: Optional[int] = Field(None, ge=0)
    lowercase: Optional[int] = Field(None, ge=0)
    max_length: Optional[int] = Field(None, ge=8, le=64)
    min_length: Optional[int] = Field(None, ge=8, le=56)
    special_symbols: Optional[int] = Field(None, ge=0)
    uppercase: Optional[int] = Field(None, ge=0)


class MergedSettingsSchema(BaseModel):
    """Represents a MergedSettingsSchema in the Iconik system."""
    acl_template_id: Optional[UUID] = None
    allow_play_original_during_transcoding: Optional[bool] = Field(
        None,
        description=
        "Allow playing the original file while transcoding is in progress."
    )
    allowed_ips: Optional[List['AllowedIPSchema']] = Field(default_factory=list)
    append_asset_uuid_to_downloads: Optional[bool] = None
    asset_default_sections: Optional[List[str]] = Field(default_factory=list)
    client_ip: Optional[str] = None
    collections_get_parent_acls: Optional[bool] = None
    cors_hosts: Optional[List[str]] = Field(default_factory=list)
    custom_terms: Optional[bool] = None
    date_format: Optional[str] = None
    datetime_format: Optional[str] = None
    default_share_options: Optional[Any] = None
    default_upload_storage_id: Optional[UUID] = None
    delete_grace_period: Optional[int] = Field(
        None,
        ge=0,
        le=87600,
        description=
        "Grace period that indicate how long objects will live in recycle bin. Unit: hours"
    )
    disable_billing_page: Optional[bool] = None
    domain_has_preloaded_assets: Optional[bool] = None
    enable_shield: Optional[bool] = None
    external_share: Optional[bool] = None
    facet_fields: Optional[List['FacetFieldSchema']
                           ] = Field(default_factory=list)
    features: Optional[List[str]] = Field(default_factory=list)
    filters_default_metadata_view_id: Optional[UUID] = None
    genesis: Optional[str] = None
    group_id: Optional[UUID] = None
    hide_favourites: Optional[bool] = None
    home_page: Optional[str] = None
    image_properties_metadata_field: Optional[str] = None
    is_plg_domain: Optional[bool] = None
    jobs_dashboard: Optional[Any] = None
    locations_metadata_field: Optional[str] = None
    lock_mapped_collections: Optional[bool] = Field(
        None,
        description="Forbid regular users to edit or delete mapped collections."
    )
    logo_storage_id: Optional[UUID] = None
    logo_url: Optional[str] = None
    logos_metadata_field: Optional[str] = None
    max_browse_users: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    max_power_users: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    max_standard_users: Optional[int] = Field(
        None, ge=-2147483648, le=2147483647
    )
    max_storage_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    max_traffic_bytes: Optional[int] = Field(
        None, ge=-9223372036854775808, le=9223372036854775807
    )
    mfa_methods: Optional[List[Literal['TOTP', 'MAIL_2SV']]
                          ] = Field(default_factory=list)
    mfa_required: Optional[bool] = None
    password_checks: Optional[Any] = None
    required_metadata_views: Optional[List[str]] = Field(default_factory=list)
    safe_searches_metadata_field: Optional[str] = None
    saml_require_groups: Optional[bool] = None
    search_auto_resize_title_column: Optional[bool] = None
    search_default_sections: Optional[List[str]] = Field(default_factory=list)
    search_display_fields: Optional[List['SearchDisplayField']
                                    ] = Field(default_factory=list)
    search_in_transcriptions: Optional[bool] = None
    search_results_asset_metadata_view_id: Optional[UUID] = None
    search_results_collection_metadata_view_id: Optional[UUID] = None
    search_users_from_share: Optional[bool] = None
    share_expiration_time: Optional[int] = Field(
        None,
        ge=0,
        le=3650,
        description=
        "Default share expiration time that indicate how long share will be valid. Unit: days"
    )
    show_persons_confirmation_modal: Optional[bool] = None
    support_access: Optional[bool] = None
    system_domain_id: Optional[UUID] = None
    system_domain_name: Optional[str] = None
    tags_metadata_field: Optional[str] = None
    texts_metadata_field: Optional[str] = None
    update_saml_primary_group_on_login: Optional[bool] = None
    use_asset_name_on_download: Optional[bool] = None
    watermark_options: Optional[Any] = None


class KubernetesSettingSchema(BaseModel):
    """Represents a KubernetesSettingSchema in the Iconik system."""
    settings: Optional[Dict[str, Any]] = Field(default_factory=dict)


class JobsWidgetOptionSchema(BaseModel):
    """Represents a JobsWidgetOptionSchema in the Iconik system."""
    columns: Optional[List[str]] = Field(default_factory=list)
    filters: Optional[Dict[str, Any]] = Field(default_factory=dict)
    limit: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    sort: Optional[List['Sort']] = Field(default_factory=list)


class JobsWidgetOptionFilterSchema(BaseModel):
    """Represents a JobsWidgetOptionFilterSchema in the Iconik system."""
    name: Optional[str] = None
    value: Optional[List[str]] = Field(default_factory=list)


class JobsDashboardWidgetSchema(BaseModel):
    """Represents a JobsDashboardWidgetSchema in the Iconik system."""
    id: Optional[str] = None
    options: Optional['JobsWidgetOption'] = None
    title: Optional[str] = None
    type: Optional[Literal['JOBS_LIST', 'JOBS_STATS_LIST']] = None


class JobsDashboardSchema(BaseModel):
    """Represents a JobsDashboardSchema in the Iconik system."""
    widgets: Optional[List['JobsDashboardWidget']] = Field(default_factory=list)


class JobsDashboard(BaseModel):
    """Represents a JobsDashboard in the Iconik system."""
    widgets: Optional[List['JobsDashboardWidget']] = Field(default_factory=list)


class JobsDashboardWidget(BaseModel):
    """Represents a JobsDashboardWidget in the Iconik system."""
    id: Optional[str] = None
    options: Optional['JobsWidgetOption'] = None
    title: Optional[str] = None
    type: Optional[Literal['JOBS_LIST', 'JOBS_STATS_LIST']] = None


class JobsWidgetOption(BaseModel):
    """Represents a JobsWidgetOption in the Iconik system."""
    columns: Optional[List[str]] = Field(default_factory=list)
    filters: Optional[Dict[str, Any]] = Field(default_factory=dict)
    limit: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    sort: Optional[List['Sort']] = Field(default_factory=list)


class Sort(BaseModel):
    """Represents a Sort in the Iconik system."""
    name: str
    order: Optional[Literal['asc', 'desc']] = None


class GroupSettingSchema(BaseModel):
    """Represents a GroupSettingSchema in the Iconik system."""
    group_id: Optional[UUID] = None
    logo_storage_id: Optional[UUID] = None
    logo_url: Optional[str] = None
    system_domain_id: Optional[UUID] = None


class GroupSettingPublicSchema(BaseModel):
    """Represents a GroupSettingPublicSchema in the Iconik system."""
    acl_template_id: Optional[UUID] = None
    allowed_ips: Optional[List['AllowedIPSchema']] = Field(default_factory=list)
    append_asset_uuid_to_downloads: Optional[bool] = None
    asset_default_sections: Optional[List[str]] = Field(default_factory=list)
    client_ip: Optional[str] = None
    collections_get_parent_acls: Optional[bool] = None
    date_format: Optional[str] = None
    datetime_format: Optional[str] = None
    default_upload_storage_id: Optional[UUID] = None
    delete_grace_period: Optional[int] = Field(
        None,
        ge=0,
        le=87600,
        description=
        "Grace period that indicate how long objects will live in recycle bin. Unit: hours"
    )
    facet_fields: Optional[List['FacetFieldSchema']
                           ] = Field(default_factory=list)
    filters_default_metadata_view_id: Optional[UUID] = None
    group_id: Optional[UUID] = None
    hide_favourites: Optional[bool] = None
    home_page: Optional[str] = None
    jobs_dashboard: Optional[Any] = None
    logo_storage_id: Optional[UUID] = None
    logo_url: Optional[str] = None
    required_metadata_views: Optional[List[str]] = Field(default_factory=list)
    search_auto_resize_title_column: Optional[bool] = None
    search_default_sections: Optional[List[str]] = Field(default_factory=list)
    search_display_fields: Optional[List['SearchDisplayField']
                                    ] = Field(default_factory=list)
    search_in_transcriptions: Optional[bool] = None
    search_results_asset_metadata_view_id: Optional[UUID] = None
    search_results_collection_metadata_view_id: Optional[UUID] = None
    share_expiration_time: Optional[int] = Field(
        None,
        ge=0,
        le=3650,
        description=
        "Default share expiration time that indicate how long share will be valid. Unit: days"
    )
    system_domain_id: Optional[UUID] = None
    use_asset_name_on_download: Optional[bool] = None


class SearchDisplayField(BaseModel):
    """Represents a SearchDisplayField in the Iconik system."""
    name: str


class GlobalSettingsSchema(BaseModel):
    """Represents a GlobalSettingsSchema in the Iconik system."""
    debug: Optional[bool] = None
    log_level: Optional[Literal['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR',
                                'CRITICAL']] = None


class FacetFieldSchema(BaseModel):
    """Represents a FacetFieldSchema in the Iconik system."""
    name: str


class DefaultShareOptionsTypeSchema(BaseModel):
    """Represents a DefaultShareOptionsTypeSchema in the Iconik system."""
    allow_approving_comments: Optional[bool] = None
    allow_comments: Optional[bool] = None
    allow_custom_actions: Optional[bool] = None
    allow_download: Optional[bool] = None
    allow_download_proxy: Optional[bool] = None
    allow_setting_approve_status: Optional[bool] = None
    allow_upload: Optional[bool] = None
    allow_view_transcriptions: Optional[bool] = None
    allow_view_versions: Optional[bool] = None
    can_change_allow_approving_comments: Optional[bool] = None
    can_change_allow_comments: Optional[bool] = None
    can_change_allow_custom_actions: Optional[bool] = None
    can_change_allow_download: Optional[bool] = None
    can_change_allow_download_proxy: Optional[bool] = None
    can_change_allow_setting_approve_status: Optional[bool] = None
    can_change_allow_upload: Optional[bool] = None
    can_change_allow_view_transcriptions: Optional[bool] = None
    can_change_allow_view_versions: Optional[bool] = None
    can_change_search_users_from_share: Optional[bool] = None
    can_change_share_expiration_time: Optional[bool] = None
    can_change_show_watermark: Optional[bool] = None
    require_password: Optional[bool] = None
    show_watermark: Optional[bool] = None


class CORSHostsSchema(BaseModel):
    """Represents a CORSHostsSchema in the Iconik system."""
    objects: Optional[List['CORSHostSchema']] = Field(default_factory=list)


class CORSHostSchema(BaseModel):
    """Represents a CORSHostSchema in the Iconik system."""
    host: str
    id: Optional[UUID] = None


class AllowedIPSchema(BaseModel):
    """Represents a AllowedIPSchema in the Iconik system."""
    app_id: Optional[UUID] = None
    ip: Optional[str] = None


# Update forward references
WatermarkOptionsTypeSchema.model_rebuild()
WatermarkOptionsType.model_rebuild()
UserSettingSchema.model_rebuild()
UserSettingRemoveAttributesSchema.model_rebuild()
SystemSettingSchema.model_rebuild()
SystemSettingPublicSchema.model_rebuild()
SortSchema.model_rebuild()
SearchDisplayFieldSchema.model_rebuild()
PasswordChecksTypeSchema.model_rebuild()
PasswordChecksType.model_rebuild()
MergedSettingsSchema.model_rebuild()
KubernetesSettingSchema.model_rebuild()
JobsWidgetOptionSchema.model_rebuild()
JobsWidgetOptionFilterSchema.model_rebuild()
JobsDashboardWidgetSchema.model_rebuild()
JobsDashboardSchema.model_rebuild()
JobsDashboard.model_rebuild()
JobsDashboardWidget.model_rebuild()
JobsWidgetOption.model_rebuild()
Sort.model_rebuild()
GroupSettingSchema.model_rebuild()
GroupSettingPublicSchema.model_rebuild()
SearchDisplayField.model_rebuild()
GlobalSettingsSchema.model_rebuild()
FacetFieldSchema.model_rebuild()
DefaultShareOptionsTypeSchema.model_rebuild()
CORSHostsSchema.model_rebuild()
CORSHostSchema.model_rebuild()
AllowedIPSchema.model_rebuild()
