<<<<<<< HEAD
import pytest
from calculator import add, subtract, multiply, divide
=======
<<<<<<< HEAD
from calculator import add, subtract, multiply
=======
from calculator import add, subtract
>>>>>>> main
>>>>>>> main

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_subtract():
    assert subtract(5, 3) == 2

def test_subtract_negative():
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
    assert subtract(2, 5) == -3

def test_multiply():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(-2, 3) == -6
<<<<<<< HEAD

def test_divide():
    assert divide(6, 3) == 2

def test_divide_float():
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
=======
=======
    assert subtract(2, 5) == -3
>>>>>>> main
>>>>>>> main
