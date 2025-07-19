from .models.term_deposit_details import DAYS_PER, InterestFreq, TermDepositDetails

DECREMENT_AMOUNT = 1

def calculate_interest_total(term_dep_details: TermDepositDetails):

    if term_dep_details.interest_payment_periods() == InterestFreq.MATURITY:
        term_dep_details.total_money += (term_dep_details.deposit *
                                         term_dep_details.interest * term_dep_details.term)
    else:
        _calc_all_interest_payment_period(term_dep_details)

def _calc_all_interest_payment_period(term_dep_details: TermDepositDetails):
        counter = term_dep_details.interest_payment_periods()
        while counter != 0:
            term_dep_details.total_money += _calc_interest_for_a_period(term_dep_details)
            counter -= DECREMENT_AMOUNT

def _calc_interest_for_a_period(term_dep_details: TermDepositDetails):

    raw_interest = (term_dep_details.total_money * term_dep_details.interest)
    daily_interest = (raw_interest / DAYS_PER[InterestFreq.ANNUAL])

    return daily_interest * DAYS_PER[term_dep_details.interest_freq]
