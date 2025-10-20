from calculator import add, subtract, multiply, divide, exponent

# Exponent Test Cases
def test_exponent_positive_integers():
    """
    Tests that raising a positive integer to a positive power (2 ** 3) equals 8
    """
    assert exponent(2, 3) == 8

def test_exponent_negative_base():
    """
    Tests that raising a negative base (-2) to an odd power (3) equals a negative integer (-8)
    """
    assert exponent(-2, 3) == -8

def test_exponent_zero_power():
    """
    Tests that any nonzero number raised to the power of 0 equals 1
    """
    assert exponent(5, 0) == 1
    assert exponent(-9, 0) == 1

def test_exponent_fractional_power():
    """
    Tests that raising a number to a fractional power (9 ** 0.5) equals 3.0
    """
    assert exponent(9, 0.5) == 3.0

# Addition Test Cases
def test_add_positive_integers():
    """
    Tests that adding 2 positive integers (5 and 10) equals a positive integer (15)
    """
    assert add(5, 10) == 15

def test_add_negative_integers():
    """
    Tests that adding 2 negative integers (-10 and -5) equals a negative integer (-15)
    """
    assert add(-10, -5) == -15

def test_add_positive_floats():
    """
    Tests that adding 2 positive floats (6.7 and 4.1) equals a positive float (10.8)
    """
    assert add(6.7, 4.1) == 10.8

def test_add_negative_floats():
    """
    Tests that adding 2 negative floats (-6.7 and -4.1) equals a negative float (-10.8)
    """
    assert add(-6.7, -4.1) == -10.8


# Subtraction Test Cases
def test_subtract_positive_integers():
    """
    Tests that subtracting 2 positive integers (10 - 5) equals a positive integer (5)
    """
    assert subtract(10, 5) == 5

def test_subtract_negative_integers():
    """
    Tests that subtracting 2 negative integers (-10 - (-5)) equals a negative integer (-5)
    """
    assert subtract(-10, -5) == -5

def test_subtract_positive_floats():
    """
    Tests that subtracting 2 positive floats (9.5 - 4.2) equals a positive float (5.3)
    """
    assert subtract(9.5, 4.2) == 5.3

def test_subtract_negative_floats():
    """
    Tests that subtracting 2 negative floats (-9.5 - (-4.2)) equals a negative float (-5.3)
    """
    assert subtract(-9.5, -4.2) == -5.3


# Multiplication Test Cases
def test_multiply_positive_integers():
    """
    Tests that multiplying 2 positive integers (5 * 3) equals a positive integer (15)
    """
    assert multiply(5, 3) == 15

def test_multiply_negative_integers():
    """
    Tests that multiplying 2 negative integers (-5 * -3) equals a positive integer (15)
    """
    assert multiply(-5, -3) == 15

def test_multiply_positive_and_negative():
    """
    Tests that multiplying a positive and a negative integer (5 * -3) equals a negative integer (-15)
    """
    assert multiply(5, -3) == -15

def test_multiply_with_zero():
    """
    Tests that multiplying any number by zero equals zero
    """
    assert multiply(9, 0) == 0
    assert multiply(0, -9) == 0


# Division Test Cases
def test_divide_positive_integers():
    """
    Tests that dividing 2 positive integers (10 / 2) equals a positive integer (5)
    """
    assert divide(10, 2) == 5

def test_divide_negative_integers():
    """
    Tests that dividing 2 negative integers (-10 / -2) equals a positive integer (5)
    """
    assert divide(-10, -2) == 5

def test_divide_positive_and_negative():
    """
    Tests that dividing a positive by a negative integer (10 / -2) equals a negative integer (-5)
    """
    assert divide(10, -2) == -5

def test_divide_by_zero():
    """
    Tests that dividing by zero raises a ZeroDivisionError
    """
    import pytest
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


