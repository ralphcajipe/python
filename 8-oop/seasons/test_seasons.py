"""
Tests for the sing function using pytest

Implement one or more functions that collectively test the implementation
of sing function from seasons.py thoroughly, each of whose names should begin
with test_ so that you can execute your tests with:

pytest test_seasons.py

Assume that the dates here were recorded on August 2, 2022, the date I
programmed this to test.
"""

import pytest
from seasons import sing


def test_prompts_for_birthdate():
    """
    It raises a SystemExit exception if the user doesn't enter a birthdate
    """
    with pytest.raises(SystemExit):
        sing("")


def test_invalid_date():
    """
    It tests that the `sing` function raises a `SystemExit` exception when
    given an invalid date, an example is a string.
    """
    with pytest.raises(SystemExit):
        sing("January 1, 1999")


def test_sing_one_year_ago():
    """
    Input of '2021-08-02' should return 'Five hundred, twenty-one thousand,
    two hundred minutes' when today is '2022-08-02'.
    """
    assert sing("2021-08-02") == "Five hundred twenty-five thousand, six hundred minutes"


def test_sing_two_years_ago():
    """
    Input of '2020-08-02' should return 'Five hundred, twenty-one thousand,
    two hundred minutes' when today is '2022-08-02'.
    """
    assert sing("2020-08-02") == "One million, fifty-one thousand, two hundred minutes"
