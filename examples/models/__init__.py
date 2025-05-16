"""Iconik API models package."""
from . import (
    acls,
    assets,
    auth,
    automations,
    files,
    jobs,
    metadata,
    notifications,
    search,
    settings,
    stats,
    transcode,
    users,
    users_notifications,
)
# Package version (YYYY.M format)
__version__ = "2025.5"
"""
This project uses calendar-based versioning in the format
`YYYY.M[.P][-modifier.N]` where:
- `YYYY` - Four-digit year
- `M` - Month number (1-12)
- `P` - (Optional) Sequential patch number
- `modifier` - (Optional) Pre-release identifier (alpha/beta/rc)
- `N` - (Optional) Pre-release sequence number
Examples:
2025.5          -> May 2025 release
2025.5.1        -> May 2025 patch 1
2025.5-alpha.1  -> First alpha release for May 2025
2025.5-beta.1   -> First beta release for May 2025
2025.5-rc.1     -> First release candidate for May 2025
"""
# API specification information
__info__ = {
    "files": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "iconik Files"
    },
    "acls": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik ACLs"
    },
    "assets": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "iconik Assets"
    },
    "auth": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Auth"
    },
    "automations": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Automations"
    },
    "jobs": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Jobs"
    },
    "metadata": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Metadata"
    },
    "notifications": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "iconik Notifications"
    },
    "search": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Search"
    },
    "settings": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Settings"
    },
    "stats": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Stats"
    },
    "transcode": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Transcode"
    },
    "users": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Users"
    },
    "users_notifications": {
        "version": "2.0.0",
        "openapi": "3.0.3",
        "title": "Iconik Users Notifications"
    },
}
__all__ = [
    "__version__",
    "__info__",
    "files",
    "acls",
    "assets",
    "auth",
    "automations",
    "jobs",
    "metadata",
    "notifications",
    "search",
    "settings",
    "stats",
    "transcode",
    "users",
    "users_notifications",
]
