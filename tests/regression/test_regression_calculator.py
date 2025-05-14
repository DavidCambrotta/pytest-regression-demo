import pytest
from app.calculator import add, subtract

@pytest.mark.regression
def test_add_large_numbers():
    assert add(1000, 5000) == 6000

@pytest.mark.regression
def test_subtract_zero():
    assert subtract(50, 0) == 50
