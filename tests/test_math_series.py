from math_series import __version__


def test_version():
    assert __version__ == '0.1.0'

"import the function that i created to test it "
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci_four():
    assert fibonacci(4) == 3

def test_fibonacci_eight():
    assert fibonacci(8) == 21

def test_lucas_four():
    assert lucas(4) == 7

def test_lucas_seven():
    assert lucas(7) == 29

def test_sum_series_four_01():
    assert sum_series(4) == 3

def test_sum_series_four_21():
    assert sum_series(4,2,1) == 7    

def test_sum_series_eight():
    assert sum_series(8) == 21

def test_sum_series_tow():
    assert sum_series(4,3,7) == 27

def test_sum_series_seven():
    assert sum_series(7,2,1) == 29   