from decimal import ROUND_HALF_UP, Decimal
from enum import Enum
import math


class InterestFreq(Enum):
    MONTH = 1
    QUARTER = 2
    ANNUAL = 3
    MATURITY = 4

PERIODS_PER_YEAR = {
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
            self, deposit: Decimal, interest: float, term_years: int,
            term_months: int, interest_freq: InterestFreq
            ):

        self.deposit, self.interest = deposit, interest
        self.term_years, self.terms_months = term_years, term_months
        self.interest_freq, self.total_money = interest_freq, deposit

    def interest_payment_periods(self) -> int:
        result = self.term_years * PERIODS_PER_YEAR[self.interest_freq]

        if self.interest_freq == InterestFreq.MONTH:
            result += self.terms_months
        elif self.interest_freq == InterestFreq.QUARTER:
            result += math.floor(self.terms_months / 4)

        return result

    def month_remainders(self) -> int:
        if self.interest_freq == InterestFreq.QUARTER:
            return self.terms_months % 4
        elif self.interest_freq == InterestFreq.MATURITY:
            return self.terms_months
        return 0

    def total_interest(self) -> int:
        rounded = int(
            Decimal(self.total_money).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            )
        return (rounded - self.deposit)
