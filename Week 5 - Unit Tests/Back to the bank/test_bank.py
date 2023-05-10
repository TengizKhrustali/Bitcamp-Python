from bank import value


def main():
    test_bank_0()
    test_bank_20()
    test_bank_100()


def test_bank_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello, how are you") == 0
    assert value("HELLO") == 0

def test_bank_20():
    
    assert value("h") == 20
    assert value("H") == 20
    assert value("hi") == 20
    assert value("how are you?") == 20

def test_bank_100():
    assert value("cat") == 100
    assert value(" ") == 100
    assert value("$$") == 100
    assert value("y o ") == 100
    
    
if __name__ == "__main__":
    main()

