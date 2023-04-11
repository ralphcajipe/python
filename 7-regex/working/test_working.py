"""
Tests for the `convert` function using pytest

Implement three or more functions that collectively test the
implementation of `convert` function from `working.py` thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py
"""

import pytest
from working import convert


def test_convert_with_12_hour_time():
    """
    If the 12 hour time is valid, output the 24 hour time.
    """
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_convert_with_missing_to():
    """
    If the 12 hour time is missing the "to", raise an error.
    """
    with pytest.raises(ValueError):
        convert("9:00 AM to")
    with pytest.raises(ValueError):
        convert("9 AM to")
    with pytest.raises(ValueError):
        convert("10 PM")
    with pytest.raises(ValueError):
        convert("10:30 PM")


def test_convert_with_missing_AM_PM():
    """
    If the 12 hour time is missing the "AM" or "PM", raise an error.
    """
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("10 to 8")
    with pytest.raises(ValueError):
        convert("10:30 to 8:50")


def test_convert_with_out_of_range_time():
    """
    If the 12 hour time is out of range, raise an error.
    """
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
