"""
Tests for the convert and gauge function function using pytest

Implement two or more functions that collectively test
the implementation of convert and gauge function from fuel.py thoroughly.

Test Summary
====================
✅ All tests passed
    6 tests passed
"""

# Importing the functions convert and gauge from the fuel.py file.
from fuel import convert, gauge
import pytest


def test_conversion():
    """
    It converts a fraction to a correct int percentage
    """
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("1/4") == 25


def test_convert_raise_value_error():
    """
    Tests the convert function for ValueError
    """
    with pytest.raises(ValueError):
        convert("0/")
    with pytest.raises(ValueError):
        convert("mario/luigi")


def test_convert_zero_division_error():
    """
    Tests the convert function for ZeroDivisionError
    """
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge_not_labeling_1_percent():
    """
    Tests the gauge function for not labeling 1%
    """
    assert gauge(1) == "E"


def test_gauge_not_printing_percent():
    """
    Tests the gauge function for not printing the percentage
    """
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


def test_gauge_not_labeling_99_percent_as_f():
    """
    Tests the gauge function for not labeling 99% as F
    """
    assert gauge(99) == "F"
