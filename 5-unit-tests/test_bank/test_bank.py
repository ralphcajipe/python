"""
Tests for the value fucntion using pytest

Implement three or more functions that collectively test
the implementation of value function from bank.py thoroughly.

Test Summary
====================
✅ All tests passed
    4 tests passed
"""

# Importing the value function from the bank.py file.
from bank import value


def test_value_with_hello_Hello():
    """
    If the greeting starts with "hello", output $0.
    """
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello, Ralph") == 0


def test_value_with_h_H():
    """
    If the greeting starts with an "h" (but not "hello"), output $20.
    """
    assert value("how you doing?") == 20
    assert value("How you doing?") == 20


def test_value_with_other_characters():
    """
    If the greeting does not start with "hello" or "h", output $100.
    """
    assert value("What's happening?") == 100


def test_value_with_empty_string():
    """
    If the greeting is an empty string, output $100.
    """
    assert value("") == 100
