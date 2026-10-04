import pytest
from src.calculator import (
    summe, durchschnitt, prozent,
    add, subtract, multiply, divide
)

def test_summe():
    assert summe(2, 3) == 5

def test_durchschnitt():
    assert durchschnitt([2, 4, 6]) == 4

def test_prozent():
    assert prozent(200, 10) == 20

def test_add():
    assert add(5, 7) == 12

def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(20, 4) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

