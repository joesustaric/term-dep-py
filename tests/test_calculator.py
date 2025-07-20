from src import calculator
from src.models.term_deposit_details import InterestFreq, TermDepositDetails


def test_calc_interest_deposit_10000_interest_1_point_1_monthly_0_years_3_months():
    deposit, interest, term_years, term_months = 10000, 0.011, 0, 3

    term_dep_details = TermDepositDetails(
        deposit,
        interest,
        term_years,
        term_months,
        InterestFreq.MONTH
        )

    calculator.calculate_interest_total(term_dep_details)

    correct_interest = 28

    assert correct_interest == term_dep_details.total_interest()

def test_calc_interest_deposit_10000_interest_1_point_1_monthly_3_years():
    deposit, interest, term_years, term_months = 10000, 0.011, 3, 0

    term_dep_details = TermDepositDetails(
        deposit,
        interest,
        term_years,
        term_months,
        InterestFreq.MONTH
        )

    calculator.calculate_interest_total(term_dep_details)

    correct_interest = 335

    assert correct_interest == term_dep_details.total_interest()

def test_calc_interest_deposit_10000_interest_1_point_1_quarterly_3_years():
    deposit, interest, term_years, term_months = 10000, 0.011, 3, 0

    term_dep_details = TermDepositDetails(
        deposit,
        interest,
        term_years,
        term_months,
        InterestFreq.QUARTER
        )

    calculator.calculate_interest_total(term_dep_details)

    correct_interest = 335

    assert correct_interest == term_dep_details.total_interest()

def test_calc_interest_deposit_10000_interest_1_point_1_annually_3_years():
    deposit, interest, term_years, term_months = 10000, 0.011, 3, 0

    term_dep_details = TermDepositDetails(
        deposit,
        interest,
        term_years,
        term_months,
        InterestFreq.ANNUAL
        )

    calculator.calculate_interest_total(term_dep_details)

    correct_interest = 334

    assert correct_interest == term_dep_details.total_interest()

def test_calc_interest_deposit_10000_interest_1_point_1_maturity_3_years():
    deposit, interest, term_years, term_months = 10000, 0.011, 3, 0

    term_dep_details = TermDepositDetails(
        deposit,
        interest,
        term_years,
        term_months,
        InterestFreq.MATURITY
        )

    calculator.calculate_interest_total(term_dep_details)

    correct_interest = 330

    assert correct_interest == term_dep_details.total_interest()

def test_calc_several_random_cases():
    cases = [
        [TermDepositDetails(60000, 0.011, 4, 11, InterestFreq.MONTH), 3333],
        [TermDepositDetails(10000, 0.011, 3, 1, InterestFreq.QUARTER), 345],
        [TermDepositDetails(10000, 0.027, 4, 0, InterestFreq.ANNUAL), 1125],
    ]

    for term_dep_details, result in cases:
        calculator.calculate_interest_total(term_dep_details)

        assert result == term_dep_details.total_interest()

