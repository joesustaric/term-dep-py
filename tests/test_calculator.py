from src import calculator
from src.models.term_deposit_details import InterestFreq, TermDepositDetails


def test_calc_interest_deposit_10000_interest_1_point_1_monthly_term_3():
    deposit, interest, term = 10000, 0.011, 3

    term_dep_details = TermDepositDetails(
        deposit,
        interest,
        term,
        InterestFreq.MONTH
        )

    calculator.calculate_interest_total(term_dep_details)

    correct_interest = 335

    assert correct_interest == term_dep_details.total_interest()

def test_calc_interest_deposit_10000_interest_1_point_1_quarterly_term_3():
    deposit, interest, term = 10000, 0.011, 3

    term_dep_details = TermDepositDetails(
        deposit,
        interest,
        term,
        InterestFreq.QUARTER
        )

    calculator.calculate_interest_total(term_dep_details)

    correct_interest = 335

    assert correct_interest == term_dep_details.total_interest()

def test_calc_interest_deposit_10000_interest_1_point_1_annually_term_3():
    deposit, interest, term = 10000, 0.011, 3

    term_dep_details = TermDepositDetails(
        deposit,
        interest,
        term,
        InterestFreq.ANNUAL
        )

    calculator.calculate_interest_total(term_dep_details)

    correct_interest = 334

    assert correct_interest == term_dep_details.total_interest()

def test_calc_interest_deposit_10000_interest_1_point_1_maturity_term_3():
    deposit, interest, term = 10000, 0.011, 3

    term_dep_details = TermDepositDetails(
        deposit,
        interest,
        term,
        InterestFreq.MATURITY
        )

    calculator.calculate_interest_total(term_dep_details)

    correct_interest = 330

    assert correct_interest == term_dep_details.total_interest()
