import pytest

def test_passing():
    assert True

def test_failing():
    assert False

@pytest.mark.slow
def test_slow():
    import time
    time.sleep(2)
    assert True

@pytest.mark.parametrize("input,expected", [(1, 2), (2, 4), (3, 6)])
def test_multiplication(input, expected):
    assert input * 2 == expected
