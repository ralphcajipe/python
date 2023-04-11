"""
Tests for the shorten function using pytest

Implementation of one or more functions that collectively tests
the implementation of shorten function from twttr.py thoroughly.
"""

# Importing the shorten function from the twttr.py file.
from twttr import shorten


def test_shorten_with_lowercase():
    """
    Test the shorten function with lowercase words.
    """
    assert shorten("hello world") == "hll wrld"


def test_shorten_with_uppercase():
    """
    Test the shorten function with uppercase words.
    """
    assert shorten("HELLO WORLD") == "HLL WRLD"


def test_shorten_with_numbers():
    """
    Test the shorten function with a word containing numbers.
    """
    assert shorten("hello123") == "hll123"
    assert shorten("HELLO123") == "HLL123"
    assert shorten("HELLO123 WORLD") == "HLL123 WRLD"


def test_shorten_with_punctuations():
    """
    Test the shorten function with a word containing punctuations.
    """
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("HELLO, WORLD!") == "HLL, WRLD!"
    assert shorten("HELLO, WORLD! 123") == "HLL, WRLD! 123"
