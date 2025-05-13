#!/usr/bin/env python3
"""
Script to download Iconik API specifications and generate Pydantic v2 models.

This script creates a Python package named `models` containing Pydantic models
for each Iconik API specification based on the OpenAPI v3 specification
`component.schemas` objects.
"""
import argparse
import glob
import json
import logging
import os
import platform
import shutil
import subprocess
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple

import requests
from jinja2 import Environment, FileSystemLoader

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# API specifications to download
SPEC_NAMES = [
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
    "users-notifications",
]

# Base URL for Iconik API specifications
BASE_URL = "https://app.iconik.io/docs/{}/spec/"

# Output directory for the models package
OUTPUT_DIR = "models"

# Template for Pydantic model generation
MODEL_TEMPLATE = '''
{% for model in models %}
{% if model.get('is_type_alias', False) %}
# {{ model.description }}
{{ model.name }} = {{ model.type_hint }}
{% else %}
class {{ model.name }}({{ model.base_class }}):
    """{{ model.description }}"""
    {% for field_name, field_info in model.fields.items() %}
    {{ field_name }}: {{ field_info.type_hint }}{% if field_info.default is not none %} = {{ field_info.default }}{% endif %}
    {% endfor %}
    {% if model.config %}
    
    class Config:
        {% for key, value in model.config.items() %}
        {{ key }} = {{ value }}
        {% endfor %}
    {% endif %}
{% endif %}
{% endfor %}
'''


def download_specs(output_dir: str) -> Dict[str, Dict[str, Any]]:
    """
    Download the OpenAPI specifications for Iconik API.
    
    Args:
        output_dir: Directory to save the downloaded specifications
        
    Returns:
        Dict mapping specification names to their parsed JSON content
    """
    specs = {}

    for spec_name in SPEC_NAMES:
        url = BASE_URL.format(spec_name)
        logger.info("Downloading specification: %s", url)

        try:
            response = requests.get(url, timeout=60)
            response.raise_for_status()

            # Parse the JSON content
            spec_json = response.json()
            specs[spec_name] = spec_json

            # Save the specification to a file
            spec_path = os.path.join(output_dir, f"{spec_name}.json")
            with open(spec_path, "w", encoding="utf-8") as fp:
                json.dump(spec_json, fp, indent=2)

            logger.info("Saved specification to: %s", spec_path)

        except requests.RequestException as e:
            logger.error(
                "Failed to download specification %s: %s", spec_name, e
            )

    return specs


def extract_schemas(
    specs: Dict[str, Dict[str, Any]]
) -> Dict[str, Dict[str, Any]]:
    """
    Extract component schemas from the API specifications.
    
    Args:
        specs: Dictionary mapping specification names to their parsed JSON
            content
        
    Returns:
        Dictionary mapping specification names to their component schemas
    """
    schemas = {}

    for spec_name, spec in specs.items():
        if "components" in spec and "schemas" in spec["components"]:
            schemas[spec_name] = spec["components"]["schemas"]
        else:
            logger.warning(
                "No component schemas found in specification: %s", spec_name
            )
            schemas[spec_name] = {}

    return schemas


def extract_all_schemas(
    specs: Dict[str, Dict[str, Any]]
) -> Dict[str, Dict[str, Any]]:
    """
    Extract all component schemas from the API specifications.
    
    Args:
        specs: Dictionary mapping specification names to their parsed JSON
            content
        
    Returns:
        Dictionary mapping schema names to schema definitions
    """
    all_schemas = {}

    for _, spec in specs.items():
        if "components" in spec and "schemas" in spec["components"]:
            for schema_name, schema in spec["components"]["schemas"].items():
                all_schemas[schema_name] = schema

    return all_schemas


def resolve_schema_references(
    schema: Dict[str, Any], all_schemas: Dict[str, Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Resolve $ref references in the schema.
    
    Args:
        schema: The schema to resolve references in
        all_schemas: Dictionary of all schemas, keyed by name
        
    Returns:
        Schema with references resolved
    """
    if not isinstance(schema, dict):
        return schema

    # Create a new schema to avoid modifying the input
    resolved = {}

    for key, value in schema.items():
        if key == "$ref" and isinstance(value, str):
            # Extract reference path components
            ref_parts = value.split("/")
            if (
                ref_parts[0] == "#" and ref_parts[1] == "components"
                and ref_parts[2] == "schemas"
            ):
                ref_name = ref_parts[3]
                if ref_name in all_schemas:
                    # Merge the referenced schema
                    referenced_schema = all_schemas[ref_name]
                    resolved.update(
                        resolve_schema_references(
                            referenced_schema, all_schemas
                        )
                    )
                else:
                    logger.warning("Referenced schema not found: %s", ref_name)
                    resolved[key] = value
            else:
                resolved[key] = value
        elif isinstance(value, dict):
            resolved[key] = resolve_schema_references(value, all_schemas)
        elif isinstance(value, list):
            resolved[key] = [
                resolve_schema_references(item, all_schemas)
                if isinstance(item, dict) else item for item in value
            ]
        else:
            resolved[key] = value

    return resolved


def openapi_type_to_python(
    openapi_type: str,
    openapi_format: Optional[str] = None,
    is_array: bool = False,
    ref: Optional[str] = None,
    enum: Optional[List[Any]] = None,
) -> str:
    """
    Convert OpenAPI type to Python type hint.
    
    Args:
        openapi_type: The OpenAPI type
        openapi_format: The OpenAPI format
        is_array: Whether the type is an array
        ref: Reference to another schema
        enum: Enumeration values
        
    Returns:
        Python type hint as a string
    """
    if ref:
        # Extract the model name from the reference
        model_name = ref.split("/")[-1]
        type_hint = model_name
    elif enum:
        # For enum types, use Literal
        enum_values = ", ".join([repr(v) for v in enum])
        type_hint = f"Literal[{enum_values}]"
    elif openapi_type == "string":
        if openapi_format == "date-time":
            type_hint = "datetime"
        elif openapi_format == "date":
            type_hint = "date"
        elif openapi_format == "uuid":
            type_hint = "UUID"
        elif openapi_format in ("uri", "url"):
            type_hint = "HttpUrl"
        else:
            type_hint = "str"
    elif openapi_type == "integer":
        if openapi_format == "int64":
            type_hint = "int"  # Using int for both int32 and int64
        else:
            type_hint = "int"
    elif openapi_type == "number":
        if openapi_format == "float":
            type_hint = "float"
        else:
            type_hint = "float"
    elif openapi_type == "boolean":
        type_hint = "bool"
    elif openapi_type == "object":
        type_hint = "Dict[str, Any]"
    elif openapi_type == "array":
        # Arrays are handled separately
        type_hint = "Any"
    else:
        type_hint = "Any"

    if is_array:
        type_hint = f"List[{type_hint}]"

    return type_hint


# pylint: disable=unused-argument
def handle_oneof_anyof(
    schema: Dict[str, Any],
    all_schemas: Dict[str, Dict[str, Any]],
    model_names: Set[str] = None
) -> str:
    """
    Handle oneOf and anyOf in OpenAPI schemas.

    Args:
        schema: The schema containing oneOf or anyOf
        all_schemas: Dictionary of all schemas
        model_names: Set of model names to check for forward references

    Returns:
        Python type hint as a string
    """
    if model_names is None:
        model_names = set()

    if "oneOf" in schema:
        types = []
        for sub_schema in schema["oneOf"]:
            if "$ref" in sub_schema:
                ref = sub_schema["$ref"]
                model_name = ref.split("/")[-1]
                # Use string literal for forward references
                if model_name in model_names:
                    types.append(f"'{model_name}'")
                else:
                    types.append(model_name)
            else:
                type_hint = openapi_type_to_python(
                    sub_schema.get("type", "any"),
                    sub_schema.get("format"),
                    is_array=False,
                    enum=sub_schema.get("enum")
                )
                types.append(type_hint)

        return f"Union[{', '.join(types)}]"

    if "anyOf" in schema:
        types = []
        for sub_schema in schema["anyOf"]:
            if "$ref" in sub_schema:
                ref = sub_schema["$ref"]
                model_name = ref.split("/")[-1]
                # Use string literal for forward references
                if model_name in model_names:
                    types.append(f"'{model_name}'")
                else:
                    types.append(model_name)
            else:
                type_hint = openapi_type_to_python(
                    sub_schema.get("type", "any"),
                    sub_schema.get("format"),
                    is_array=False,
                    enum=sub_schema.get("enum")
                )
                types.append(type_hint)

        return f"Union[{', '.join(types)}]"

    return "Any"


def generate_models(
    schemas: Dict[str, Dict[str, Any]], all_schemas: Dict[str, Dict[str, Any]]
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Generate Pydantic models from OpenAPI schemas.

    Args:
        schemas: Dictionary mapping specification names to their component
            schemas
        all_schemas: Dictionary of all schemas

    Returns:
        Dictionary mapping specification names to lists of model definitions
    """
    models_by_spec = {}

    for spec_name, spec_schemas in schemas.items():
        models = []

        # First, collect all model names that will be defined
        model_names = set(spec_schemas.keys())

        for model_name, schema in spec_schemas.items():
            # Handle oneOf/anyOf at the top level
            if "oneOf" in schema or "anyOf" in schema:
                # Pass model_names to handle_oneof_anyof to identify forward
                # references
                type_hint = handle_oneof_anyof(schema, all_schemas, model_names)

                model = {
                    "name": model_name,
                    "is_type_alias": True,
                    "type_hint": type_hint,
                    "description": schema.get(
                        "description", f"Type alias for {model_name}."
                    )
                }

                models.append(model)
                continue

            # Skip non-object schemas
            if schema.get("type") != "object" and "properties" not in schema:
                logger.warning("Skipping non-object schema: %s", model_name)
                continue

            # Get required fields
            required = schema.get("required", [])

            # Process properties
            properties = schema.get("properties", {})
            fields = {}

            for field_name, field_schema in properties.items():
                field_name, field_info = generate_model_field(
                    field_name, field_schema, required, model_names
                )
                fields[field_name] = field_info

            # Add model configuration
            config = {}

            # Handle extra fields
            if "additionalProperties" in schema:
                config["extra"] = "allow"

            # Create model definition
            model = {
                "name": model_name,
                "base_class": "BaseModel",
                "description": schema.get(
                    "description",
                    f"Represents a {model_name} in the Iconik system."
                ),
                "fields": fields,
                "config": config
            }

            models.append(model)

        # Sort models by dependency
        sorted_models = sort_models_by_dependency(models)

        models_by_spec[spec_name] = sorted_models

    return models_by_spec


def generate_model_field(
    field_name: str,
    schema: Dict[str, Any],
    required: List[str],
    model_names: Set[str] = None
) -> Tuple[str, Dict[str, Any]]:
    """
    Generate a Pydantic field definition from an OpenAPI schema property.

    Args:
        field_name: Name of the field
        schema: OpenAPI schema for the field
        required: List of required field names
        model_names: Set of model names to check for forward references

    Returns:
        Tuple of (field_name, field_info) where field_info contains type_hint
            and default
    """
    if model_names is None:
        model_names = set()

    # Store the original field name for potential use as an alias
    original_field_name = field_name

    # Check if field name contains dashes or other invalid characters
    has_invalid_chars = "-" in field_name or field_name.startswith("x-")

    # Convert dashed names to underscore
    if has_invalid_chars:
        # For fields starting with x-, keep the x_ prefix
        if field_name.startswith("x-"):
            field_name = "x_" + field_name[2:].replace("-", "_")
        else:
            field_name = field_name.replace("-", "_")

    # Convert Python keywords
    if field_name in [
        "class", "from", "import", "return", "pass", "if", "else", "for",
        "while", "as", "def", "try", "except", "finally", "raise", "with",
        "yield", "async", "await", "lambda", "None", "True", "False", "and",
        "or", "not", "in", "is", "global", "nonlocal", "assert", "del", "elif",
        "continue", "break"
    ]:
        field_name = f"{field_name}_"

    # Handle references
    if "$ref" in schema:
        ref = schema["$ref"]
        ref_name = ref.split("/")[-1]

        # Use string literals for forward references
        if ref_name in model_names:
            type_hint = f"'{ref_name}'"
        else:
            type_hint = ref_name

        is_required = original_field_name in required

        field_info = {
            "type_hint": f"Optional[{type_hint}]"
            if not is_required else type_hint,
            "default": "None" if not is_required else None
        }

        # Add alias if the field name has been changed
        if has_invalid_chars:
            if field_info["default"] is None:
                field_info["default"
                           ] = f'Field(..., alias="{original_field_name}")'
            else:
                field_info["default"
                           ] = f'Field(None, alias="{original_field_name}")'

        return field_name, field_info

    # Handle oneOf/anyOf
    if "oneOf" in schema or "anyOf" in schema:
        # Pass model_names to handle_oneof_anyof
        type_hint = handle_oneof_anyof(schema, {}, model_names)
        is_required = original_field_name in required

        field_info = {
            "type_hint": f"Optional[{type_hint}]"
            if not is_required else type_hint,
            "default": "None" if not is_required else None
        }

        # Add alias if the field name has been changed
        if has_invalid_chars:
            if field_info["default"] is None:
                field_info["default"
                           ] = f'Field(..., alias="{original_field_name}")'
            else:
                field_info["default"
                           ] = f'Field(None, alias="{original_field_name}")'

        return field_name, field_info

    # Handle arrays
    if schema.get("type") == "array":
        items = schema.get("items", {})
        if "$ref" in items:
            ref = items["$ref"]
            ref_name = ref.split("/")[-1]

            # Use string literals for forward references
            if ref_name in model_names:
                item_type = f"'{ref_name}'"
            else:
                item_type = ref_name
        else:
            item_type = openapi_type_to_python(
                items.get("type", "any"),
                items.get("format"),
                enum=items.get("enum")
            )

        type_hint = f"List[{item_type}]"
        is_required = original_field_name in required

        default = "Field(default_factory=list)"
        if has_invalid_chars:
            default = f'Field(default_factory=list, alias="{original_field_name}")'  # pylint: disable=line-too-long

        if is_required:
            if has_invalid_chars:
                default = f'Field(..., alias="{original_field_name}")'
            else:
                default = None

        return field_name, {
            "type_hint": f"Optional[{type_hint}]"
            if not is_required else type_hint,
            "default": default
        }

    # Handle objects
    if schema.get("type") == "object":
        if "additionalProperties" in schema:
            if "$ref" in schema["additionalProperties"]:
                ref = schema["additionalProperties"]["$ref"]
                ref_name = ref.split("/")[-1]

                # Use string literals for forward references
                if ref_name in model_names:
                    value_type = f"'{ref_name}'"
                else:
                    value_type = ref_name
            else:
                value_type = openapi_type_to_python(
                    schema["additionalProperties"].get("type", "any"),
                    schema["additionalProperties"].get("format")
                )

            type_hint = f"Dict[str, {value_type}]"
        else:
            type_hint = "Dict[str, Any]"

        is_required = original_field_name in required

        default = "Field(default_factory=dict)"
        if has_invalid_chars:
            default = f'Field(default_factory=dict, alias="{original_field_name}")'  # pylint: disable=line-too-long

        if is_required:
            if has_invalid_chars:
                default = f'Field(..., alias="{original_field_name}")'
            else:
                default = None

        return field_name, {
            "type_hint": f"Optional[{type_hint}]"
            if not is_required else type_hint,
            "default": default
        }

    # Handle other types
    type_hint = openapi_type_to_python(
        schema.get("type", "any"),
        schema.get("format"),
        enum=schema.get("enum")
    )

    is_required = original_field_name in required

    # Start building constraints list, beginning with an alias if needed
    constraints = []
    if has_invalid_chars:
        constraints.append(f'alias="{original_field_name}"')

    # Handle patterns and constraints
    if schema.get("pattern"):
        pattern = schema["pattern"]
        constraints.append(f'pattern="{pattern}"')

    # Handle min/max
    if schema.get("minimum") is not None:
        constraints.append(f"ge={schema['minimum']}")
    if schema.get("maximum") is not None:
        constraints.append(f"le={schema['maximum']}")

    # Handle min/max length
    if schema.get("minLength") is not None:
        constraints.append(f"min_length={schema['minLength']}")
    if schema.get("maxLength") is not None:
        constraints.append(f"max_length={schema['maxLength']}")

    # Handle min/max items
    if schema.get("minItems") is not None:
        constraints.append(f"min_items={schema['minItems']}")
    if schema.get("maxItems") is not None:
        constraints.append(f"max_items={schema['maxItems']}")

    # Add description if available
    if schema.get("description"):
        description = schema["description"].replace('"', '\\"')
        constraints.append(f'description="{description}"')

    if constraints:
        constraints_str = ", ".join(constraints)

        if is_required:
            default = f"Field(..., {constraints_str})"
        else:
            default = f"Field(None, {constraints_str})"
    else:
        default = "None" if not is_required else None

    return field_name, {
        "type_hint": f"Optional[{type_hint}]" if not is_required else type_hint,
        "default": default
    }


def collect_model_dependencies(
    models: List[Dict[str, Any]]
) -> Dict[str, Set[str]]:
    """
    Collect dependencies between models.
    
    Args:
        models: List of model definitions
        
    Returns:
        Dictionary mapping model names to sets of dependent model names
    """
    dependencies = {}

    for model in models:
        model_name = model["name"]
        dependencies[model_name] = set()

        if model.get("is_type_alias", False):
            type_hint = model["type_hint"]

            # Extract model names from type hint
            for other_model in models:
                other_name = other_model["name"]
                if other_name != model_name and other_name in type_hint:
                    dependencies[model_name].add(other_name)

            continue

        for field_info in model["fields"].values():
            type_hint = field_info["type_hint"]

            # Extract model names from type hints
            for other_model in models:
                other_name = other_model["name"]
                if other_name != model_name and other_name in type_hint:
                    dependencies[model_name].add(other_name)

    return dependencies


def sort_models_by_dependency(
    models: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Sort models by dependency order to ensure dependent models come first.
    
    Args:
        models: List of model definitions
        
    Returns:
        Sorted list of model definitions
    """
    # Collect model names
    model_names = [model["name"] for model in models]

    # Collect dependencies
    dependencies = collect_model_dependencies(models)

    # Helper function to get dependencies for a model
    def get_deps(name):
        return dependencies.get(name, set())

    # Create a mapping of models by name
    models_by_name = {model["name"]: model for model in models}

    # Perform topological sort
    sorted_names = []
    visited = set()
    temp_marks = set()

    def visit(name):
        if name in temp_marks:
            # Circular dependency detected, just continue
            return
        if name not in visited:
            temp_marks.add(name)
            for dep in get_deps(name):
                if dep in model_names:
                    visit(dep)
            temp_marks.remove(name)
            visited.add(name)
            sorted_names.append(name)

    # Visit all nodes
    for name in model_names:
        if name not in visited:
            visit(name)

    # Reverse the order so that dependencies come first
    sorted_names.reverse()

    # Create sorted list of models
    sorted_models = []
    for name in sorted_names:
        if name in models_by_name:
            sorted_models.append(models_by_name[name])

    return sorted_models


def generate_model_code(models: List[Dict[str, Any]]) -> str:
    """
    Generate Python code for Pydantic models.
    
    Args:
        models: List of model definitions
        
    Returns:
        Python code as a string
    """
    env = Environment(loader=FileSystemLoader("."))
    template = env.from_string(MODEL_TEMPLATE)

    return template.render(models=models)


def create_module_file(
    spec_name: str, models: List[Dict[str, Any]], output_dir: str
) -> None:
    """
    Create a Python module file for a specification's models.

    Args:
        spec_name: Name of the specification
        models: List of model definitions
        output_dir: Directory to save the module file
    """
    # Convert spec name to Python module name
    module_name = spec_name.replace("-", "_")

    # Create module file path
    module_path = os.path.join(output_dir, f"{module_name}.py")

    # Essential imports to avoid circular dependencies
    imports = {
        "from __future__ import annotations",
        "from typing import Any, Dict, List, Optional, Union, TYPE_CHECKING"
    }
    imports.add("from pydantic import BaseModel, Field")

    # Check for specific types
    has_datetime = False
    has_date = False
    has_uuid = False
    has_url = False
    has_literal = False

    for model in models:
        if model.get("is_type_alias", False):
            type_hint = model["type_hint"]

            if "datetime" in type_hint:
                has_datetime = True
            if "date" in type_hint and "datetime" not in type_hint:
                has_date = True
            if "UUID" in type_hint:
                has_uuid = True
            if "HttpUrl" in type_hint:
                has_url = True
            if "Literal" in type_hint:
                has_literal = True

            continue

        for field_info in model["fields"].values():
            type_hint = field_info["type_hint"]

            if "datetime" in type_hint:
                has_datetime = True
            if "date" in type_hint and "datetime" not in type_hint:
                has_date = True
            if "UUID" in type_hint:
                has_uuid = True
            if "HttpUrl" in type_hint:
                has_url = True
            if "Literal" in type_hint:
                has_literal = True

    if has_datetime or has_date:
        if has_datetime and has_date:
            imports.add("from datetime import date, datetime")
        elif has_datetime:
            imports.add("from datetime import datetime")
        else:
            imports.add("from datetime import date")

    if has_uuid:
        imports.add("from uuid import UUID")

    if has_url:
        imports.add("from pydantic import HttpUrl")

    if has_literal:
        imports.add("from typing import Literal")

    # Generate module docstring
    docstring = (
        f'"""\nIconik {spec_name.capitalize()} Models\n\n'
        f'This module contains Pydantic models for the Iconik '
        f'{spec_name.capitalize()} API.\n"""'
    )

    # Generate model code with string literals for cross-references
    model_code = generate_model_code(models)

    # Write the module file
    with open(module_path, "w", encoding="utf-8") as fp:
        fp.write(docstring + "\n\n")
        fp.write("\n".join(sorted(imports)) + "\n\n\n")
        fp.write(model_code)

        # Add model_rebuild calls to resolve forward references
        fp.write("\n\n# Update forward references\n")
        for model in models:
            if not model.get("is_type_alias", False):
                fp.write(f"{model['name']}.model_rebuild()\n")

    logger.info("Created module file: %s", module_path)


def get_calendar_version(patch=None, modifier=None, modifier_num=None):
    """
    Generate a calendar-based version string in the format
    YYYY.M[.P][-modifier.N]

    Args:
        patch: Optional patch number
        modifier: Optional pre-release identifier (alpha/beta/rc)
        modifier_num: Optional pre-release sequence number

    Returns:
        str: Calendar-based version string
    """
    now = datetime.now()
    year = now.year
    month = now.month

    # Start with YYYY.M
    version = f"{year}.{month}"

    # Add patch if provided
    if patch is not None:
        version += f".{patch}"

    # Add modifier and number if provided
    if modifier is not None and modifier_num is not None:
        version += f"-{modifier}.{modifier_num}"

    return version


def create_package_files(
    output_dir: str, spec_names: List[str], specs: Dict[str, Dict[str, Any]]
) -> None:
    """
    Create package files (__init__.py, __version__.py) for the models package.

    Args:
        output_dir: Directory for the models package
        spec_names: List of specification names
        specs: Dictionary containing the full specifications with version info
    """
    # Create __version__.py with versions from all specs
    version_path = os.path.join(output_dir, "__version__.py")
    with open(version_path, "w", encoding="utf-8") as fp:
        fp.write('"""Version information for Iconik API models."""\n\n')

        # Package version using calendar versioning
        version = get_calendar_version()
        fp.write('# Package version (YYYY.M format)\n')
        fp.write(f'__version__ = "{version}"\n\n')

        # Document versioning scheme
        fp.write('"""\n')
        fp.write('This project uses calendar-based versioning in the format\n')
        fp.write('`YYYY.M[.P][-modifier.N]` where:\n')
        fp.write('\n')
        fp.write('- `YYYY` - Four-digit year\n')
        fp.write('- `M` - Month number (1-12)\n')
        fp.write('- `P` - (Optional) Sequential patch number\n')
        fp.write(
            '- `modifier` - (Optional) Pre-release identifier (alpha/beta/rc)\n'
        )
        fp.write('- `N` - (Optional) Pre-release sequence number\n')
        fp.write('\n')
        fp.write('Examples:\n')
        fp.write('\n')
        fp.write('2025.5          -> May 2025 release\n')
        fp.write('2025.5.1        -> May 2025 patch 1\n')
        fp.write('2025.5-alpha.1  -> First alpha release for May 2025\n')
        fp.write('2025.5-beta.1   -> First beta release for May 2025\n')
        fp.write('2025.5-rc.1     -> First release candidate for May 2025\n')
        fp.write('"""\n\n')

        # Add individual spec versions
        fp.write('# API specification versions\n')
        fp.write('spec_versions = {\n')

        for spec_name in spec_names:
            module_name = spec_name.replace("-", "_")

            # Extract version from spec info
            version = "unknown"
            if spec_name in specs and "info" in specs[spec_name]:
                spec_info = specs[spec_name]["info"]
                if "version" in spec_info:
                    version = spec_info["version"]

                # Include title information as a comment
                title = spec_info.get(
                    "title", f"Iconik {spec_name.capitalize()}"
                )
                fp.write(f'    # {title}\n')

            fp.write(f'    "{module_name}": "{version}",\n')

        fp.write('}\n')

    logger.info("Created version file: %s", version_path)

    # Create __init__.py with imports
    init_path = os.path.join(output_dir, "__init__.py")
    with open(init_path, "w", encoding="utf-8") as fp:
        fp.write('"""Iconik API models package."""\n\n')
        fp.write("from . import __version__\n\n")

        # Import all modules
        for spec_name in spec_names:
            module_name = spec_name.replace("-", "_")
            fp.write(f"from . import {module_name}\n")

        fp.write("\n__all__ = [\n")
        fp.write("    \"__version__\",\n")

        for spec_name in spec_names:
            module_name = spec_name.replace("-", "_")
            fp.write(f"    \"{module_name}\",\n")

        fp.write("]\n")

    logger.info("Created init file: %s", init_path)


def format_generated_code(output_dir: str, format_code: bool = False) -> None:
    """
    Format the generated Python code using common linting tools.

    Args:
        output_dir: Directory containing the generated code
        format_code: Whether to format the code
    """
    if not format_code:
        logger.info("Skipping code formatting. Use --format-code to enable.")
        return

    formatters = [{
        "name": "pycln",
        "cmd": ["pycln", "--all", output_dir],
        "check": lambda: shutil.which("pycln") is not None
    }, {
        "name": "isort",
        "cmd": [
            "isort", "--balanced", "--ensure-newline-before-comments",
            "--force-grid-wrap=0", "--trailing-comma", "--line-length=80",
            "--lines-after-imports=2", "--multi-line=3", "--profile=pycharm",
            "--skip-glob=**/venv/**", "--extend-skip-glob=**/.venv/**",
            "--extend-skip-glob=**/env/**", "--extend-skip-glob=**/.env/**",
            "--use-parentheses", output_dir
        ],
        "check": lambda: shutil.which("isort") is not None
    }, {
        "name": "remove_empty_lines",
        "cmd": get_empty_line_removal_command(output_dir),
        "check": lambda: shutil.which("sed") is not None
    }, {
        "name": "yapf",
        "cmd": [
            "yapf", "--in-place", "--recursive", "--print-modified", output_dir
        ],
        "check": lambda: shutil.which("yapf") is not None
    }]

    for formatter in formatters:
        if formatter["check"]():
            # Skip if command is None (which can happen for the sed command on
            # Windows)
            if formatter["cmd"] is None:
                logger.warning(
                    "Skipping %s as it's not properly supported on this OS",
                    formatter["name"]
                )
                continue

            logger.info("Running %s...", formatter["name"])
            try:
                result = subprocess.run(
                    formatter["cmd"],
                    check=True,
                    capture_output=True,
                    text=True
                )
                logger.info("%s completed successfully", formatter["name"])
                if result.stdout:
                    logger.debug(
                        "%s output: %s", formatter["name"], result.stdout
                    )
            except subprocess.CalledProcessError as e:
                logger.error(
                    "%s failed with code %d: %s", formatter["name"],
                    e.returncode, e.stderr
                )
        else:
            logger.warning("%s not found. Skipping.", formatter["name"])


def get_empty_line_removal_command(output_dir: str) -> Optional[List[str]]:
    """
    Generate the appropriate command to remove empty lines based on OS.

    Args:
        output_dir: Directory containing Python files to process

    Returns:
        A command list for subprocess or None if not supported
    """
    system = platform.system()

    if system == "Windows":
        # sed on Windows works differently and is often not reliable
        # Alternative could be to use Python to process files directly
        return None

    python_files = glob.glob(
        os.path.join(output_dir, "**/*.py"), recursive=True
    )
    cmds = ["sed", "-i", "", "-e", "s/[[:space:]]*$//", "-e", "/^$/d"
            ] if system == "Darwin" else [
                "sed", "-i", "-e", "s/[[:space:]]*$//", "-e", "/^$/d"
            ]
    return cmds + python_files


# Update main function to include the formatting option
def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Generate Pydantic models from Iconik API specifications"
    )
    parser.add_argument(
        "--output-dir",
        default=OUTPUT_DIR,
        help=f"Output directory for the models package (default: {OUTPUT_DIR})"
    )
    parser.add_argument(
        "--format-code",
        action="store_true",
        help="Format generated code using pycln, isort, and yapf"
    )
    args = parser.parse_args()

    output_dir = args.output_dir
    spec_dir = os.path.join(output_dir, "_specs")

    # Create output directories
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(spec_dir, exist_ok=True)

    # Download specifications
    specs = download_specs(spec_dir)

    if not specs:
        logger.error("No specifications downloaded. Exiting.")
        return 1

    # Extract all schemas for reference resolution
    all_schemas = extract_all_schemas(specs)

    # Extract schemas for each spec
    schemas = extract_schemas(specs)

    # Generate models
    models_by_spec = generate_models(schemas, all_schemas)

    # Create module files
    for spec_name, models in models_by_spec.items():
        if models:
            create_module_file(spec_name, models, output_dir)

    # Create package files
    create_package_files(
        output_dir, [name for name in SPEC_NAMES if models_by_spec.get(name)],
        specs
    )

    # Format the generated code
    format_generated_code(output_dir, args.format_code)

    logger.info("Model generation complete. Package created at: %s", output_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
