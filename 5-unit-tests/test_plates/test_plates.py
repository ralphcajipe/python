"""
Tests for the is_valid function using pytest

Implement four or more functions that collectively test
the implementation of is_valid function from plates.py thoroughly.
"""

# Importing the is_valid function from the plates.py file.
from plates import is_valid


def test_empty_plate():
    """Testing if the plate number is empty. Returns False."""
    assert is_valid("") == False


def test_no_beginning_alphabetical_letters():
    """Testing if the plate number has no beginning alphabetical letters.
    Returns False.
    """
    assert is_valid("1") == False
    assert is_valid("22") == False
    assert is_valid("50CS") == False
    assert is_valid("0CS50") == False


def test_plates():
    """Testing if the plate number meets all the requirements."""
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("OUTATIME ") == False


def test_ends_with_digit():
    """Testing if the plate number ends with a digit. Returns False."""
    assert is_valid("PI3.14") == False


def test_single_character_plate():
    """Testing if the plate number is a single character. Returns False."""
    assert is_valid("H") == False


def test_no_period_allowed():
    """Testing if the plate number has a period. Returns False."""
    assert is_valid("CS50.") == False


def test_no_spaces_allowed():
    """Testing if the plate number has any spaces. Returns False."""
    assert is_valid("CS 50") == False
    assert is_valid("CS50 ") == False
    assert is_valid("CS 50") == False


def test_no_punctuation_marks_allowed():
    """Testing if the plate number has any punctuation marks. Returns False."""
    assert is_valid("CS-50") == False
    assert is_valid("CS50%") == False
    assert is_valid("CS50?") == False
    assert is_valid("CS50!") == False
