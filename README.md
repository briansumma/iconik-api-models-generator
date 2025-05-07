# Iconik API Models Generator

This script downloads the OpenAPI v3 specifications for the Iconik API
and generates Pydantic v2 models based on the component schemas.

## Features

- Downloads all Iconik API specifications
- Generates Pydantic v2 models for each specification
- Resolves schema references
- Handles complex types (oneOf, anyOf)
- Sorts models by dependency
- Creates a well-structured Python package
- Automatically formats generated code (optional)

## Requirements

- Python 3.9 or later
- Required packages:
    - requests
    - jinja2
    - pydantic (v2)
- Optional formatting packages:
    - pycln
    - isort
    - yapf

## Installation

```bash
# Clone the repository
git clone https://github.com/briansumma/iconik-api-models-generator.git
cd iconik-api-models-generator

# Install dependencies
pip install -e .

# For development with formatting tools
pip install -e ".[dev]"
# Or just the formatting tools
pip install -e ".[formatters]"
```

## Usage

```bash
# Basic usage
generate-iconik-models

# With custom output directory
generate-iconik-models --output-dir my_models

# With code formatting
generate-iconik-models --format-code
```

This will:

1. Download the latest OpenAPI specifications for Iconik API
2. Extract component schemas from the specifications
3. Generate Pydantic v2 models based on the schemas
4. Create a models package with modules for each specification
5. Optionally format the generated code with pycln, isort, and yapf
   (when using `--format-code`)

The models package will be created in the `models` directory by default.

## Generated Package Structure

```
models/
├── __init__.py
├── __version__.py
├── acls.py
├── assets.py
├── auth.py
├── automations.py
├── files.py
├── jobs.py
├── metadata.py
├── notifications.py
├── search.py
├── settings.py
├── stats.py
├── transcode.py
├── users_notifications.py
└── users.py
```

Each module contains Pydantic models for the corresponding Iconik API
specification.

## Example Usage

Once you've generated the models, you can use them in your code:

```python
from models import assets, files

# Create an asset
asset = assets.AssetCreateSchema(
    title="My Asset",
    external_id="ext-123",
    type="ASSET"
)

# Create a file
file = files.FileCreateSchema(
    directory_path="/path/to/dir",
    original_name="my_file.mp4",
    type="FILE"
)
```

## Manually Formatting Generated Code

The generated code may have whitespace issues or other formatting
inconsistencies. You can verify this by running:

```bash
# Check for errors using pylint
pylint --errors-only --rcfile pyproject.toml --recursive yes models/
# Or the default categories
pylint --rcfile pyproject.toml --recursive yes models/
```

While the `--format-code` option will use pycln, isort, and yapf, you
can manually format the generated code using various tools:

### Using Black

```bash
# Install black
pip install black

# Format the code
black models/
```

### Using autopep8

```bash
# Install autopep8
pip install autopep8

# Format the code
autopep8 --in-place --recursive --aggressive --aggressive models/
```

### Using Flake8 (for linting)

```bash
# Install flake8
pip install flake8

# Lint the code
flake8 models/
```

### Using Ruff (fast linter/formatter)

```bash
# Install ruff
pip install ruff

# Format the code
ruff format models/

# Lint and fix automatically
ruff check --fix models/
```

### Combination Approach (recommended)

For the best results, use a combination of tools in this order:

```bash
# 1. Remove unused imports
pycln --all models/

# 2. Sort imports
isort models/

# 3. Format code style
black -l 88 models/  # or yapf/autopep8

# 4. Lint and fix remaining issues
ruff check --fix models/

# 5. Final verification
pylint --rcfile pyproject.toml models/
```

This multi-step approach ensures both proper import organization and
consistent code style.

## Troubleshooting

If you encounter any issues:

1. Ensure you have the correct Python version (3.9+)
2. Verify that all dependencies are installed
3. Check that you have internet access to download the specifications
4. If code formatting fails, ensure you have the formatting tools
   installed (`pip install -e ".[formatters]"`)
5. For persistent formatting issues, try the manual formatting steps
   above

## License

MIT
