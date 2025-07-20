from .models.term_deposit_details import DAYS_PER, InterestFreq, TermDepositDetails

DECREMENT_AMOUNT = 1
END_CONDITION = 0

def calculate_interest_total(term_dep_details: TermDepositDetails):
    _calc_all_interest_payment_periods(term_dep_details)
    _calc_remainder_months(term_dep_details)

def _calc_all_interest_payment_periods(term_dep_details: TermDepositDetails):
    if term_dep_details.interest_freq == InterestFreq.MATURITY:
        term_dep_details.total_money += (term_dep_details.deposit *
                                         term_dep_details.interest * term_dep_details.term_years)
        return

    counter = term_dep_details.interest_payment_periods()
    while counter != END_CONDITION:
        term_dep_details.total_money += _calc_interest_full_payment_periods(term_dep_details)
        counter -= DECREMENT_AMOUNT

def _calc_interest_full_payment_periods(term_dep_details: TermDepositDetails):
    raw_interest = (term_dep_details.total_money * term_dep_details.interest)
    daily_interest = (raw_interest / DAYS_PER[InterestFreq.ANNUAL])

    return daily_interest * DAYS_PER[term_dep_details.interest_freq]

# These below functions are very similar to the above.
# I decided to not refactor these together because im treating this as
# separate business logic on how to handle remainder months as just
# Monthly interest calcs. Except for when its quarterly and there are further
# quarters to pay.

def _calc_remainder_months(term_dep_details: TermDepositDetails):
    counter = term_dep_details.month_remainders()
    while counter != END_CONDITION:
        term_dep_details.total_money += _calc_interest_remaining_months_period(term_dep_details)
        counter -= DECREMENT_AMOUNT

def _calc_interest_remaining_months_period(term_dep_details: TermDepositDetails):
    raw_interest = (term_dep_details.total_money * term_dep_details.interest)
    daily_interest = (raw_interest / DAYS_PER[InterestFreq.ANNUAL])

    return daily_interest * DAYS_PER[InterestFreq.MONTH]

