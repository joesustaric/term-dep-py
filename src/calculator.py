from decimal import ROUND_HALF_UP, Decimal
from .models.term_deposit_details import TermDepositDetails, InterestFreq, DAYS_PER


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
