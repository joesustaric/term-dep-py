from src.input_validator import validate_inputs, ValidationException
import pytest

def test_deposit_input():
    input_1 = [-234, 0.011, "1", "3", "m"]
    input_2 = [100000300, 0.011, "1", "3", "m"]

    with pytest.raises(ValidationException):
        validate_inputs(
            input_1[0], input_1[1], input_1[2], input_1[3], input_1[4]
            )

    with pytest.raises(ValidationException):
        validate_inputs(
            input_2[0], input_2[1], input_2[2], input_2[3], input_2[4]
            )


def test_bad_interest_input():
    input_1 = [1234, -0.011, "1", "3", "m"]
    input_2 = [1234, 10.01, "1", "3", "m"]

    with pytest.raises(ValidationException):
        validate_inputs(
            input_1[0], input_1[1], input_1[2], input_1[3], input_1[4]
            )

    with pytest.raises(ValidationException):
        validate_inputs(
            input_2[0], input_2[1], input_2[2], input_2[3], input_2[4]
            )


def test_bad_years_input():
    return

def test_bad_months_input():
    return

def test_bad_freq_input():
    return
