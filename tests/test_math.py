# test_math_operations.py

import pytest
from  pytestproject.math import add, subtract, multiply, divide

class MathOperationsTest:
    @pytest.mark.parametrize("a, b, expected", [
        (5, 2, 7),     # a + b = 5 + 2 = 7
        (-10, 3, -7),  # a + b = -10 + 3 = -7
        (0, 0, 0)      # a + b = 0 + 0 = 0
    ])
    def test_add(self, a, b, expected):
        result = add(a, b)
        assert result == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 3, 7),    # a - b = 10 - 3 = 7
        (5, -2, 7),    # a - b = 5 - (-2) = 7
        (0, 0, 0)      # a - b = 0 - 0 = 0
    ])
    def test_subtract(self, a, b, expected):
        result = subtract(a, b)
        assert result == expected

    @pytest.mark.parametrize("a, b, expected", [
        (5, 2, 10),     # a * b = 5 * 2 = 10
        (-3, 4, -12),   # a * b = -3 * 4 = -12
        (0, 10, 0)      # a * b = 0 * 10 = 0
    ])
    def test_multiply(self, a, b, expected):
        result = multiply(a, b)
        assert result == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),     # a / b = 10 / 2 = 5
        (5, -2, -2.5),  # a / b = 5 / (-2) = -2.5
        (8, 4, 2),      # a / b = 8 / 4 = 2
    ])
    def test_divide(self, a, b, expected):
        result = divide(a, b)
        assert result == expected

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(10, 0)
