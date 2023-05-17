import pytest
from um import count


def test_count_normal():
    # Test the count function with a normal input
    text = "Um, hello? Um, are you there?"
    expected = 2
    actual = count(text)
    assert actual == expected

def test_count_empty():
    # Test the count function with an empty input
    text = ""
    expected = 0
    actual = count(text)
    assert actual == expected


def test_count_no_um():
    # Test the count function with an input that has no "um"
    text = "Hello, world!"
    expected = 0
    actual = count(text)
    assert actual == expected


def test_count_substring():
    # Test the count function with an input that has "um" as a substring of some other word
    text = "Yummy food!"
    expected = 0
    actual = count(text)
    assert actual == expected


def test_count_case_insensitive():
    # Test the count function with an input that has different cases of "um"
    text = "Um, UM, um, uM"
    expected = 4
    actual = count(text)
    assert actual == expected
