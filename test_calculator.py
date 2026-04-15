from calculator import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_subtract():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(2, 5) == -3

def test_multiply():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(-2, 3) == -6