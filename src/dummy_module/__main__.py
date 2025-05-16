#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dummy module to ensure linting pipelines pass successfully.

This module provides a basic calculator implementation with proper type
hints, docstrings, and error handling to pass linting checks.
"""
import logging
from typing import Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Constants
DEFAULT_OPERATIONS = ["add", "subtract", "multiply", "divide"]
MAX_HISTORY_SIZE = 100


class CalculationError(Exception):
    """Exception raised for errors in the calculation."""


class Calculator:
    """
    A simple calculator implementation.

    This class provides basic arithmetic operations and maintains a
    history of calculations.

    Attributes:
        history (List[Dict]): List of previous calculations
        operations (List[str]): Available operations
    """

    def __init__(self, operations: Optional[List[str]] = None) -> None:
        """
        Initialize the Calculator.

        Args:
            operations: List of available operations. If None, uses
                default operations.
        """
        self.history: List[Dict[str, Union[str, float, int]]] = []
        self.operations = operations if operations else DEFAULT_OPERATIONS
        logger.info(
            "Calculator initialized with %s operations",
            ", ".join(self.operations),
        )

    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        result = float(a) + float(b)
        self._add_to_history("add", a, b, result)
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            The difference of a and b
        """
        result = float(a) - float(b)
        self._add_to_history("subtract", a, b, result)
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
        result = float(a) * float(b)
        self._add_to_history("multiply", a, b, result)
        return result

    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide a by b.

        Args:
            a: First number
            b: Second number

        Returns:
            The quotient of a and b

        Raises:
            CalculationError: If division by zero is attempted
        """
        try:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = float(a) / float(b)
            self._add_to_history("divide", a, b, result)
            return result
        except ZeroDivisionError as e:
            logger.error("Division by zero attempted: %s / %s", a, b)
            raise CalculationError(f"Division error: {str(e)}") from e

    def calculate(
        self, operation: str, a: Union[int, float], b: Union[int, float]
    ) -> float:
        """
        Perform a calculation using the specified operation.

        Args:
            operation: The name of the operation to perform
            a: First number
            b: Second number

        Returns:
            The result of the operation

        Raises:
            CalculationError: If the operation is not supported
        """
        if operation not in self.operations:
            available_ops = ", ".join(self.operations)
            logger.error("Unsupported operation '%s' requested", operation)
            raise CalculationError(
                f"Unsupported operation: {operation}. Available: {available_ops}"
            )

        operation_methods = {
            "add": self.add,
            "subtract": self.subtract,
            "multiply": self.multiply,
            "divide": self.divide,
        }

        op_func = operation_methods.get(operation)
        if op_func:
            return op_func(a, b)

        # This should not be reached if operations are configured correctly
        raise CalculationError(f"Operation implementation missing: {operation}")

    def _add_to_history(
        self,
        operation: str,
        a: Union[int, float],
        b: Union[int, float],
        result: float,
    ) -> None:
        """
        Add an operation to the calculation history.

        Args:
            operation: Name of the operation performed
            a: First number
            b: Second number
            result: The calculation result
        """
        entry = {"operation": operation, "a": a, "b": b, "result": result}
        self.history.append(entry)

        # Keep history size under the limit
        if len(self.history) > MAX_HISTORY_SIZE:
            self.history.pop(0)

        logger.debug("Added to history: %s %s %s = %s", a, operation, b, result)

    def get_history(self) -> List[Dict[str, Union[str, float, int]]]:
        """
        Get the calculation history.

        Returns:
            A list of calculation records
        """
        return self.history

    def clear_history(self) -> None:
        """Clear the calculation history."""
        history_size = len(self.history)
        self.history = []
        logger.info("Cleared %s items from calculator history", history_size)


def main() -> None:
    """Example usage of the Calculator class."""
    calculator = Calculator()

    try:
        result1 = calculator.add(5, 3)
        logger.info("5 + 3 = %s", result1)

        result2 = calculator.subtract(10, 4)
        logger.info("10 - 4 = %s", result2)

        result3 = calculator.multiply(2.5, 4)
        logger.info("2.5 * 4 = %s", result3)

        result4 = calculator.divide(20, 5)
        logger.info("20 / 5 = %s", result4)

        # This will raise an exception
        # calculator.divide(10, 0)

    except CalculationError as e:
        logger.error("Calculation failed: %s", str(e))


if __name__ == "__main__":
    main()
