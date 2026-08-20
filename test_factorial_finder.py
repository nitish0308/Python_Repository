import pytest

from Factorial_finder import factorial_finder


@pytest.mark.parametrize("num, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (5, 120),
])
def test_factorial_finder_prints_correct_value(capsys, num, expected):
    factorial_finder(num)
    captured = capsys.readouterr()
    assert f"factorial of {num} is:{expected}" in captured.out


def test_factorial_finder_returns_none():
    # Current implementation prints instead of returning the result.
    assert factorial_finder(4) is None
