import pytest
from datetime import date
from seasons import minutes_lived

def test_minutes_lived_valid():
    # Test that the function returns the correct number of minutes for a valid date
    assert minutes_lived(2000, 1, 1) == "Twelve million, two hundred ninety-nine thousand forty minutes"

def test_minutes_lived_invalid():
    # Test that the function returns "invalid Date" for an invalid date
    assert minutes_lived(23, 2, 30) == "invalid Date"
