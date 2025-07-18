from decimal import Decimal, ROUND_HALF_UP

def calculate_interest(deposit: int, interest: Decimal, length: int) -> int:

    iterations_per_year = {
        "monthly": 12,
    }

    total_iterations = length * iterations_per_year["monthly"]
    running_total = deposit

    while total_iterations != 0:
        running_total =  running_total + _calc_interest_portion(running_total, interest, "monthly")
        total_iterations-= 1

    rounded_decimal= Decimal(running_total).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return int(float(rounded_decimal)) - deposit


def _calc_interest_portion(money, interest, portion):
    portion_of_year = {
        "monthly": 30.42
    }
    result = ((money * interest) / 365) * portion_of_year[portion]
    print(result)
    return result
