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
            self, deposit: Decimal, interest: float, term_years: int, term_months: int,
            interest_freq: InterestFreq
            ):

        self.deposit = deposit
        self.interest = interest
        self.term_years = term_years
        self.terms_months = term_months
        self.interest_freq = interest_freq
        self.total_money = deposit

    def interest_payment_periods(self) -> int:
        if self.interest_freq == InterestFreq.MATURITY:
            return InterestFreq.MATURITY
        return self.term_years * ITERATIONS_PER_YEAR[self.interest_freq]

    def total_interest(self) -> int:
        rounded = int(
            Decimal(self.total_money).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            )
        return (rounded - self.deposit)
