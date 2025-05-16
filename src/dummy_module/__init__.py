"""
Pylintrc dummy package for pipeline testing.

This package exists to provide a testable module structure
for linting pipelines using pylint, ruff, and yapf.
"""

from .__main__ import (
    DEFAULT_OPERATIONS,
    MAX_HISTORY_SIZE,
    CalculationError,
    Calculator,
)


__version__ = "0.1.0"
__all__ = [
    "Calculator",
    "CalculationError",
    "DEFAULT_OPERATIONS",
    "MAX_HISTORY_SIZE",
]
