from twttr import shorten

def main():
    test_upper()
    test_lower()
    test_symbols()

def test_upper():
    assert shorten("TEN") == "TN"

def test_lower():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("aeiou") == ""

def test_symbols():
    assert shorten("HELLO$$") == "HLL$$"

if __name__ == "__main__":
    main()
