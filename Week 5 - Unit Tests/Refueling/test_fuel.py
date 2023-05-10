import pytest

from fuel import convert, gauge # import the convert and gauge functions from the code file

def main():
    test_convert()
    test_gauge()
    test_zero_error()
    test_value_error()
# define a test function for the convert function
def test_convert():
    # use assert statements to check if the convert function returns the expected values
    assert convert("1/2") == 50 # check if 1/2 is converted to 50% and flag is True
    assert convert("3/4") == 75 # check if 3/4 is converted to 75% and flag is True

# define a test function for the gauge function
def test_gauge():
    # use assert statements to check if the gauge function returns the expected values
    assert gauge(50) == "50%" # check if 50% is returned as "50%"
    assert gauge(1) == "E" # check if 1% is returned as "E"
    assert gauge(99) == "F" # check if 99% is returned as "F"
    assert gauge(100) == "F" # check if 100% is returned as "F"
def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_value_error():   
    with pytest.raises(ValueError):
        convert("sd")
        convert("s/d")
        convert("s/50")
    with pytest.raises(ValueError):
        convert("-5/10")
        convert("5/-3")
    with pytest.raises(ValueError):
        convert("1.5/3")
        convert("5/3")



if __name__ == "__main__":
    main()
