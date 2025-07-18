import pytest
from src import calculator
from decimal import Decimal

def test_calculate_interest(capsys):
    deposit, interest, length = 10000, 0.011, 3

    interest_result = calculator.calculate_interest(deposit, interest, length)

    correct_interest = 335

    assert correct_interest == interest_result
