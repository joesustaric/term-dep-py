from decimal import ROUND_HALF_UP, Decimal
from enum import Enum


class InterestFreq(Enum):
    MONTH = 1
    QUARTER = 2
    ANNUAL = 3
    MATURITY = 4

ITERATIONS_PER_YEAR = {
    InterestFreq.MONTH: 12,
    InterestFreq.QUARTER: 4,
    InterestFreq.ANNUAL: 1
}

DAYS_PER = {
    InterestFreq.MONTH: 30.42,
    InterestFreq.QUARTER: 91.25,
    InterestFreq.ANNUAL: 365.0
}

class TermDepositDetails:
    def __init__(
            self, deposit: Decimal, interest: float, term: int, interest_freq: InterestFreq
            ):

        self.deposit = deposit
        self.interest = interest
        self.term = term
        self.interest_freq = interest_freq
        self.total_money = deposit

    def interest_payment_periods(self) -> int:
        return self.term * ITERATIONS_PER_YEAR[self.interest_freq]

    def total_interest(self) -> int:
        rounded = int(Decimal(self.total_money).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        return (rounded - self.deposit)

def calculate_interest_total(term_dep_details: TermDepositDetails) -> int:

    _calc_all_interest(term_dep_details)

    return term_dep_details.total_interest()

def _calc_all_interest(term_dep_details: TermDepositDetails):

    if term_dep_details.interest_freq == InterestFreq.MATURITY:
        term_dep_details.total_money += term_dep_details.deposit * term_dep_details.interest * term_dep_details.term
        return

    counter = term_dep_details.interest_payment_periods()
    while counter != 0:
        term_dep_details.total_money += _calc_interest_chunk(term_dep_details)
        counter -= 1

def _calc_interest_chunk(term_dep_details: TermDepositDetails):

    raw_interest = (term_dep_details.total_money * term_dep_details.interest)
    daily_interest = (raw_interest / DAYS_PER[InterestFreq.ANNUAL])
    result = daily_interest * DAYS_PER[term_dep_details.interest_freq]

    return result
