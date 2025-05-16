#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the dummy_module to ensure the code passes linting.

This module contains pytest-compatible tests for the Calculator class.
"""
import pytest

from src.dummy_module import MAX_HISTORY_SIZE, CalculationError, Calculator


@pytest.fixture
def calculator():
    """Return a Calculator instance for testing."""
    return Calculator()


def test_add(calculator):
    """Test the add operation."""
    # Test with integers
    assert calculator.add(2, 3) == 5.0

    # Test with floats
    assert calculator.add(2.5, 3.5) == 6.0

    # Test with negative numbers
    assert calculator.add(-2, -3) == -5.0


def test_subtract(calculator):
    """Test the subtract operation."""
    # Test with integers
    assert calculator.subtract(5, 3) == 2.0

    # Test with floats
    assert calculator.subtract(5.5, 3.5) == 2.0

    # Test with negative result
    assert calculator.subtract(3, 5) == -2.0


def test_multiply(calculator):
    """Test the multiply operation."""
    # Test with integers
    assert calculator.multiply(2, 3) == 6.0

    # Test with floats
    assert calculator.multiply(2.5, 4) == 10.0

    # Test with zero
    assert calculator.multiply(5, 0) == 0.0


def test_divide(calculator):
    """Test the divide operation."""
    # Test with integers
    assert calculator.divide(6, 3) == 2.0

    # Test with floats
    assert calculator.divide(5, 2) == 2.5

    # Test division by negative number
    assert calculator.divide(10, -2) == -5.0


def test_divide_by_zero(calculator):
    """Test that division by zero raises an error."""
    with pytest.raises(CalculationError):
        calculator.divide(10, 0)


def test_calculate(calculator):
    """Test the calculate method with different operations."""
    assert calculator.calculate("add", 2, 3) == 5.0
    assert calculator.calculate("subtract", 5, 3) == 2.0
    assert calculator.calculate("multiply", 2, 3) == 6.0
    assert calculator.calculate("divide", 6, 3) == 2.0


def test_invalid_operation(calculator):
    """Test that an invalid operation raises an error."""
    with pytest.raises(CalculationError):
        calculator.calculate("power", 2, 3)


def test_history(calculator):
    """Test that operations are recorded in history."""
    # Perform some operations
    calculator.add(2, 3)
    calculator.subtract(5, 3)
    calculator.multiply(2, 3)

    # Check history
    history = calculator.get_history()
    assert len(history) == 3

    # Check specific history entry
    assert history[0]["operation"] == "add"
    assert history[0]["a"] == 2
    assert history[0]["b"] == 3
    assert history[0]["result"] == 5.0


def test_clear_history(calculator):
    """Test that history can be cleared."""
    # Perform some operations
    calculator.add(2, 3)
    calculator.subtract(5, 3)

    # Clear history
    calculator.clear_history()

    # Check history is empty
    assert len(calculator.get_history()) == 0


def test_custom_operations():
    """Test calculator with custom operations."""
    custom_calc = Calculator(operations=["add", "multiply"])

    # Valid operations should work
    assert custom_calc.calculate("add", 2, 3) == 5.0
    assert custom_calc.calculate("multiply", 2, 3) == 6.0

    # Invalid operation should raise error
    with pytest.raises(CalculationError):
        custom_calc.calculate("subtract", 5, 3)


def test_history_limit():
    """Test that history size is limited."""
    # Create a calculator and perform more operations than the history limit
    calc = Calculator()
    for i in range(MAX_HISTORY_SIZE + 10):
        calc.add(i, 1)

    # Check that history size equals the maximum
    assert len(calc.get_history()) == MAX_HISTORY_SIZE

    # Check that the oldest entries were removed (FIFO)
    history = calc.get_history()
    assert history[0]["a"] == 10  # First entry should be i=10, not i=0
