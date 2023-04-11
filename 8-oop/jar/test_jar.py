"""
Unit tests for the methods from Jar class using pytest

Implement four or more functions that collectively test the implementation
of Jar class from jar.py thoroughly, each of whose names should begin
with test_ so that you can execute your tests with:

pytest test_jar.py
"""

import pytest
from jar import Jar


def test_init():
    """
    It creates a new Jar object with a capacity of 12 and a size of 0
    which is optional.

    This asserts that the capacity is 12 and the size is 0.
    """
    jar = Jar(capacity=12)
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    """
    It tests that the string representation of a jar is a string of emoji cookies.
    """
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    """It tests that the deposit method works as expected."""
    jar = Jar(capacity=12)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    """It tests that the withdraw method works as expected."""
    jar = Jar(capacity=12)
    jar.deposit(1)
    jar.deposit(11)
    assert jar.size == 12
    jar.withdraw(1)
    assert jar.size == 11
    with pytest.raises(ValueError):
        jar.withdraw(13)
