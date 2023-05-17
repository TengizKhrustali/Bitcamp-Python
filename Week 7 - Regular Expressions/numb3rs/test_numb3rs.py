# content of test_numb3rs.py
import numb3rs

def main():
    test_valid_ip()
    test_invalid_ip()
    test_invalid_input()
    
def test_valid_ip():
    # Test a valid IP address
    assert numb3rs.validate("10.10.10.10") is True

def test_invalid_ip():
    # Test an invalid IP address
    assert numb3rs.validate("10.10.10.300") is False

def test_invalid_input():
    # Test an invalid input type
    assert numb3rs.validate("123") is False


if __name__ == "__main__":
    main()
