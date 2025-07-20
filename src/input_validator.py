import re

VALID_FREQ_CHARS = r'^[matq]$'

class ValidationException(Exception):
    pass

def validate_inputs(deposit, interest, years, months, freq):
    _validate_deposit(deposit)
    _validate_interest(interest)
    _validate_years(years)
    _validate_months(months)
    _validate_freq(freq)

def _validate_deposit(deposit):
    if deposit < 0 or deposit > 1000000:
        raise ValidationException(f"Deposit invalid amount {deposit} - needs 1 - 1000000")

def _validate_interest(interest):
    if interest < 0 or interest > 1.0:
        raise ValidationException(f"Interest invalid amount {interest} - needs 0.0-1.0")

def _validate_years(years):
    if years < 0 or years > 5:
        raise ValidationException(f"Year invalid count {years} - needs 0-5")

def _validate_months(months):
    if months < 0 or months > 11:
        raise ValidationException(f"Months invalid count {months} - needs 0-11")

def _validate_freq(freq):
    if len(freq) != 1:
        raise ValidationException(
            f"Frequency invalid {freq} - needs m=monthly, a=annual q=quarterly, t=maturity"
            )
    if not re.match(VALID_FREQ_CHARS, freq):
        raise ValidationException(f"Frequency invalid {freq}")
