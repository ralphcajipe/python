"""
Unit Tests for the validate function using pytest

Implement two or more functions that collectively test the implementation of validate function
from numb3rs.py thoroughly.

Test Summary
====================
✅ All tests passed
    11 tests passed
"""

from numb3rs import validate
import pytest


def test_validate_1():
    assert validate("127.0.0.1") is True


def test_validate_2():
    assert validate("255.255.255.255") is True


def test_validate_3():
    assert validate("512.512.512.512") is False


def test_validate_4():
    assert validate("1.2.3.1000") is False


def test_validate_5():
    assert validate("cat") is False


def test_validate_6():
    assert validate(" .  .  .  ") is False


def test_validate_7():
    assert validate("1.2.3.4") is True


def test_validate_8():
    assert validate("127.0.0.1") is True


def test_validate_9():
    assert validate("255.255.255.0") is True


def test_validate_10():
    assert validate("275.3.6.28") is False


# test_numb3rs.py catches numb3rs.py only checking first octet of the IPv4 address.
def test_validate_11():
    assert validate("1.256.256.256") is False
