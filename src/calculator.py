from decimal import ROUND_HALF_UP, Decimal
from enum import Enum


class InterestFreq(Enum):
    MONTH = 1
    QUARTER = 2
    YEAR = 3
    MATURITY = 4

ITERATIONS_PER_YEAR = {
    InterestFreq.MONTH: 12,
    InterestFreq.QUARTER: 4,
    InterestFreq.YEAR: 1
}

DAYS_PER = {
    InterestFreq.MONTH: 30.42,
    InterestFreq.QUARTER: 91.25,
    InterestFreq.YEAR: 365
}

class TermDepositDetails:
    def __init__(
            self, deposit: Decimal, interest: float, term: int, interest_freq: InterestFreq
            ):

        self.deposit = deposit
        self.interest = interest
        self.term = term
        self.interest_freq = interest_freq
        self.total_interest = deposit

def calculate_interest_total(term_dep_details: TermDepositDetails) -> int:

    # total_iterations = term_dep_details.term * ITERATIONS_PER_YEAR[InterestFreq.MONTH]
    # running_total = term_dep_details.deposit

    # while total_iterations != 0:
    #     running_total += _calc_interest_chunk(running_total, term_dep_details)
    #     total_iterations-= 1

    # rounded_dec = Decimal(running_total).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    # return int(rounded_dec) - term_dep_details.deposit

    total_iterations = term_dep_details.term * ITERATIONS_PER_YEAR[InterestFreq.MONTH]
    foo(term_dep_details, total_iterations)

    rounded_dec = Decimal(term_dep_details.total_interest).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return int(rounded_dec) - term_dep_details.deposit

def _calc_interest_chunk(previous_total, term_dep_details: TermDepositDetails):

    raw_interest = (previous_total * term_dep_details.interest)
    daily_interest = (raw_interest / DAYS_PER[InterestFreq.YEAR])

    result = daily_interest * DAYS_PER[term_dep_details.interest_freq]

    return result


def foo(term_dep_details: TermDepositDetails, counter)-> TermDepositDetails:

    if counter == 0:
        return

    raw_interest = (term_dep_details.total_interest * term_dep_details.interest)
    daily_interest = (raw_interest / DAYS_PER[InterestFreq.YEAR])

    term_dep_details.total_interest += daily_interest * DAYS_PER[term_dep_details.interest_freq]

    counter -= 1
    foo(term_dep_details, counter)

