"""
Tests for the count function using pytest

Implement three or more functions that collectively test the implementation
of count function from um.py thoroughly, each of whose names should begin
with test_ so that you can execute your tests with:

pytest test_working.py
"""

from um import count


def test_count_empty_string():
    assert count("") == 0


def test_count_word_with_no_um():
    assert count("Hello world") == 0


def test_count_word_with_um():
    assert count("Hello world, I am um") == 1
    assert count("Hello world, I am um, I'm um") == 2
    assert count("Hello wors, I am UM") == 1
    assert count("Um, thanks, um...") == 2


def test_count_word_with_um_in_middle():
    """
    It returns 0 if the word contains "um" in the middle
    """
    assert count("yummy") == 0
    assert count("dummy") == 0
