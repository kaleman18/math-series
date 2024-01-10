from math_series.series import fibonacci, lucas, sum_series




def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibonacci_eight():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected
    
def test_fibonacci_thirteen():
    actual = fibonacci(13)
    expected = 233
    assert actual == expected

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_seven():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_lucas_eleven():
    actual = lucas(11)
    expected = 199
    assert actual == expected

def test_sum_series_zero():
    actual = sum_series(0, 1, 2)
    expected = 2
    assert actual == expected

def test_sum_series_seven():
    actual = sum_series(7, 1, 2)
    expected = 29
    assert actual == expected

def test_sum_series_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_seven():
    actual = sum_series(7)
    expected = 13
    assert actual == expected
