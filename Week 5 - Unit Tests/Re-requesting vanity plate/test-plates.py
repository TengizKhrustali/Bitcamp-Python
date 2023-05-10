from plates import is_valid

def main():
    # call test functions
    test_min_max_characters()
    test_Start_with_two_numbers()
    test_numbers_in_the_middle()
    test_number_0()
    test_isalnum()
    test_punctuation()

# vanity plates length must be max 6 characters and min 2 characters
def test_min_max_characters(): 
    assert is_valid("AA") is True
    assert is_valid("ABCDEF") is True
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False

# All vanity plates must start with at least two letters
def test_Start_with_two_numbers():
    assert is_valid("AA") is True
    assert is_valid("A2") is False
    assert is_valid("2A") is False
    assert is_valid("22") is False

# Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
def test_numbers_in_the_middle():
    assert is_valid("AAA222") is True
    assert is_valid("AAA22A") is False
    assert is_valid("aaa2bb") is False
# The first number used cannot be a ‘0’(
def test_number_0():
    assert is_valid("CS50") is True
    assert is_valid("CS05") is False

def test_punctuation():
    assert is_valid("PI#.14") is False
    assert is_valid("PI3!14") is False
    assert is_valid("PI 14") is False

# No periods, spaces, or punctuation marks are allowed

def test_isalnum():
    assert is_valid("A$") is False
    assert is_valid("AA.AA66") is False
    assert is_valid("$1") is False
    assert is_valid("123456") is False
    

if __name__ == "__main__":
    main()
