
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
        raise ValidationException("Deposit invalid amount")

def _validate_interest(interest):
    if interest < 0 or interest > 10.00:
        raise ValidationException("Interest invalid amount")

def _validate_years(years):
    return

def _validate_months(months):
    return

def _validate_freq(freq):
    return
