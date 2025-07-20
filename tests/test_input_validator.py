import pytest

from src.input_validator import ValidationException, validate_inputs


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
    input_2 = [1234, 1.01, "1", "3", "m"]

    with pytest.raises(ValidationException):
        validate_inputs(
            input_1[0], input_1[1], input_1[2], input_1[3], input_1[4]
            )

    with pytest.raises(ValidationException):
        validate_inputs(
            input_2[0], input_2[1], input_2[2], input_2[3], input_2[4]
            )


def test_bad_years_input():
    input_1 = [1234, 0.011, -2, "3", "m"]
    input_2 = [1234, 0.099, 6, "3", "m"]

    with pytest.raises(ValidationException):
        validate_inputs(
            input_1[0], input_1[1], input_1[2], input_1[3], input_1[4]
            )

    with pytest.raises(ValidationException):
        validate_inputs(
            input_2[0], input_2[1], input_2[2], input_2[3], input_2[4]
            )

def test_bad_months_input():
    input_1 = [1234, 0.011, 1, -1, "m"]
    input_2 = [1234, 0.099, 2, 13, "m"]

    with pytest.raises(ValidationException):
        validate_inputs(
            input_1[0], input_1[1], input_1[2], input_1[3], input_1[4]
            )

    with pytest.raises(ValidationException):
        validate_inputs(
            input_2[0], input_2[1], input_2[2], input_2[3], input_2[4]
            )

def test_bad_freq_input():
    input_1 = [1234, 0.011, 1, 1, "masdf"]
    input_2 = [1234, 0.011, 1, 1, ""]
    input_3 = [1234, 0.011, 1, 1, "m"] # (m)onthly
    input_4 = [1234, 0.011, 1, 1, "a"] # (a)nually
    input_5 = [1234, 0.011, 1, 1, "q"] # (q)uarterly
    input_6 = [1234, 0.011, 1, 1, "t"] # ma(t)urity

    with pytest.raises(ValidationException):
        validate_inputs(
            input_1[0], input_1[1], input_1[2], input_1[3], input_1[4]
            )

    with pytest.raises(ValidationException):
        validate_inputs(
            input_2[0], input_2[1], input_2[2], input_2[3], input_2[4]
            )
    try:
        validate_inputs(
            input_3[0], input_3[1], input_3[2], input_3[3], input_3[4]
            )
        validate_inputs(
            input_4[0], input_4[1], input_4[2], input_4[3], input_4[4]
            )
        validate_inputs(
            input_5[0], input_5[1], input_5[2], input_5[3], input_5[4]
            )
        validate_inputs(
            input_6[0], input_6[1], input_6[2], input_6[3], input_6[4]
            )
    except ValidationException:
        pytest.fail("Unexpected ValidationException ..")
