import csv
import pytest
from  pytestproject.math import add,subtract

def read_test_data(file_path):
    test_data = []
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
     
        for row in reader:
            test_data.append((int(row['a']), int(row['b']), int(row['expected'])))
    return test_data

class MathOperationsTest:
    @pytest.mark.parametrize("a, b, expected", read_test_data("pytestproject/test_data.csv"))
    def test_add(self, a, b, expected):
        result = add(a, b)
        assert result == expected
        
    @pytest.mark.parametrize("a, b, expected", read_test_data("pytestproject/test_data.csv"))
    def test_subtract(self, a, b, expected):
        result = subtract(a, b)
        assert result == expected
