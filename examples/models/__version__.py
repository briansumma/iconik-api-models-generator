"""Version information for Iconik API models."""
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
# API specification versions
spec_versions = {
    # iconik Files
    "files": "2.0.0",
    # Iconik ACLs
    "acls": "2.0.0",
    # iconik Assets
    "assets": "2.0.0",
    # Iconik Auth
    "auth": "2.0.0",
    # Iconik Automations
    "automations": "2.0.0",
    # Iconik Jobs
    "jobs": "2.0.0",
    # Iconik Metadata
    "metadata": "2.0.0",
    # iconik Notifications
    "notifications": "2.0.0",
    # Iconik Search
    "search": "2.0.0",
    # Iconik Settings
    "settings": "2.0.0",
    # Iconik Stats
    "stats": "2.0.0",
    # Iconik Transcode
    "transcode": "2.0.0",
    # Iconik Users
    "users": "2.0.0",
    # Iconik Users Notifications
    "users_notifications": "2.0.0",
}
