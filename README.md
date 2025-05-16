# Iconik API Models Generator

This tool downloads the OpenAPI v3 specifications for the Iconik API and
generates Pydantic v2 models based on the component schemas.

## Core Functionality

- Downloads all Iconik API specifications
- Generates Pydantic v2 models for each specification
- Resolves schema references
- Handles complex types (oneOf, anyOf)
- Sorts models by dependency
- Creates a well-structured Python package
- Automatically formats generated code (optional)

## System Requirements

- Python 3.9 or later
- Required packages:
    - `requests`: API specification acquisition
    - `jinja2`: Template processing
    - `pydantic` (v2): Model generation
- Optional formatting packages:
    - `pycln`: Import optimization
    - `isort`: Import organization
    - `yapf`: Code style normalization

## Installation Procedure

### Basic Setup

```bash
# Repository acquisition
git clone https://github.com/briansumma/iconik-api-models-generator.git
cd iconik-api-models-generator

# Core dependency installation
pip install -e .
```

### Development Environment Configuration

```bash
# Complete development environment
pip install -e ".[dev]"

# Formatting tools only
pip install -e ".[formatters]"
```

## Operation Procedures

### Basic Execution

```bash
generate-iconik-models
```

### Configuration Options

The tool accepts the following command-line parameters:

| Option             | Syntax                                   | Purpose                                                            |
| ------------------ | ---------------------------------------- | ------------------------------------------------------------------ |
| Help               | `-h, --help`                             | Displays usage information and available options                   |
| Version            | `--version`                              | Shows program's version number and exits                           |
| Output Directory   | `-o OUTPUT_DIR, --output-dir OUTPUT_DIR` | Specifies target location for generated models (default: `models`) |
| Code Formatting    | `-F, --format-code`                      | Applies automated formatting using `pycln`, `isort`, and `yapf`    |
| Preserve Downloads | `--keep-downloads`                       | Retains downloaded specification files after processing            |
| Debug Mode         | `--debug`                                | Enables verbose diagnostic logging for troubleshooting             |

### Processing Workflow

1. **API Specification Acquisition**

    - Downloads latest OpenAPI v3 specifications from Iconik API
      endpoints
    - Validates specification format compatibility

2. **Schema Extraction**

    - Parses component schemas from specification documents
    - Resolves reference dependencies between schemas

3. **Model Generation**

    - Converts OpenAPI schemas to Pydantic v2 model classes
    - Applies Python typing system for property validation

4. **Package Structure Creation**

    - Organizes models into logical API-aligned modules
    - Generates appropriate import statements and package hierarchy

5. **Code Optimization** (when using `--format-code`)
    - Removes unused imports with `pycln`
    - Sorts import statements with `isort`
    - Eliminates trailing whitespace with `sed`
    - Normalizes code formatting with `yapf`

## Generated Package Structure

The output directory structure varies depending on command-line
parameters:

### Standard Output (Default)

```
models/
├── __init__.py
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

### With Preserved Specifications (`--keep-downloads`)

```
models/
├── __init__.py
├── _specs/
│   ├── acls.json
│   ├── assets.json
│   ├── auth.json
│   ├── automations.json
│   ├── files.json
│   ├── jobs.json
│   ├── metadata.json
│   ├── notifications.json
│   ├── search.json
│   ├── settings.json
│   ├── stats.json
│   ├── transcode.json
│   ├── users-notifications.json
│   └── users.json
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

Each Python module contains Pydantic models corresponding to the
associated Iconik API specification. When the `--keep-downloads` flag is
specified, the original JSON specification files are preserved in the
`_specs/` directory for reference. This is useful if you're using an IDE
that can render OpenAPI definitions in JSON files, providing convenient
visualization and exploration of the API schema during development.

## Implementation Examples

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

## Code Formatting Procedures

### Automated Formatting

The `--format-code` option applies a comprehensive formatting workflow:

1. Import optimization with `pycln`
2. Import organization with `isort`
3. Whitespace normalization with `sed`
4. Code structure standardization with `yapf`

### Manual Formatting Options

#### Quality Verification

```bash
# Verify code quality with pylint
pylint --errors-only --rcfile pyproject.toml --recursive yes models/

# Full quality assessment
pylint --rcfile pyproject.toml --recursive yes models/
```

#### Formatter Selection

Different code formatters offer varying formatting approaches:

| Tool     | Installation           | Usage                                                               | Characteristics                  |
| -------- | ---------------------- | ------------------------------------------------------------------- | -------------------------------- |
| Black    | `pip install black`    | `black models/`                                                     | Strict, deterministic formatting |
| autopep8 | `pip install autopep8` | `autopep8 --in-place --recursive --aggressive --aggressive models/` | Incremental PEP 8 compliance     |
| Ruff     | `pip install ruff`     | `ruff format models/`                                               | High-performance formatter       |

#### Linting Tools

| Tool   | Installation         | Usage                      | Purpose                   |
| ------ | -------------------- | -------------------------- | ------------------------- |
| Flake8 | `pip install flake8` | `flake8 models/`           | Style guide enforcement   |
| Ruff   | `pip install ruff`   | `ruff check --fix models/` | Fast linting with autofix |

### Using `sed` for Trailing Whitespace Removal

The `sed` (stream editor) implementation varies between POSIX variants,
requiring different syntax for in-place editing operations:

#### Command Syntax by Operating System

| System Type | Command Pattern                    | Example                                        |
| ----------- | ---------------------------------- | ---------------------------------------------- |
| BSD/macOS   | `sed -i '<suffix>' -e '<pattern>'` | `sed -i '' -e 's/[[:space:]]*$//' models/*.py` |
| GNU/Linux   | `sed -i[<suffix>] -e '<pattern>'`  | `sed -i -e 's/[[:space:]]*$//' models/*.py`    |

#### Implementation Notes:

- The `-i` flag enables in-place editing of files
- BSD implementations require an argument (use empty string `''` for no
  backup)
- GNU implementations accept an optional suffix parameter
- The pattern `'s/[[:space:]]*$//'` removes trailing whitespace from
  each line

### Recommended Formatting Workflow

For optimal code quality, apply formatters in this sequence:

```bash
# 1. Remove unused imports
pycln --all models/

# 2. Sort imports
isort models/

# 3. Format code style (choose one)
black -l 88 models/    # Option 1: Black formatter
# or
yapf -i models/*.py    # Option 2: YAPF formatter

# 4. Lint and fix remaining issues
ruff check --fix models/

# 5. Final verification
pylint --rcfile pyproject.toml models/
```

This multi-stage process ensures both proper import organization and
consistent code style.

## Troubleshooting Procedures

If you encounter implementation issues:

1. **Environment Verification**

    - Ensure Python 3.9+ is correctly installed and active
    - Verify all dependencies are properly installed
    - Confirm network connectivity for API specification download

2. **Formatting Issues**

    - Install formatting tools: `pip install -e ".[formatters]"`
    - Try manual formatting procedures (see section above)
    - Verify tool compatibility with your Python version

3. **Generation Failures**
    - Check for API specification changes
    - Examine error messages for specific schema incompatibilities
    - Ensure sufficient disk space for generated files

## License

MIT
