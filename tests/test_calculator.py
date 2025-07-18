from src import calculator


def test_calc_interest_deposit_10000_interest_1_point_1_monthly_term_3(capsys):
    deposit, interest, term = 10000, 0.011, 3

    term_dep_details = calculator.TermDepositDetails(
        deposit,
        interest,
        term,
        calculator.InterestFreq.MONTH
        )

    interest_result = calculator.calculate_interest_total(term_dep_details)

    correct_interest = 335

    assert correct_interest == interest_result

def test_calc_interest_deposit_10000_interest_1_point_1_quarterly_term_3(capsys):
    deposit, interest, term = 10000, 0.011, 3

    term_dep_details = calculator.TermDepositDetails(
        deposit,
        interest,
        term,
        calculator.InterestFreq.QUARTER
        )

    interest_result = calculator.calculate_interest_total(term_dep_details)

    correct_interest = 335

    assert correct_interest == interest_result

def test_calc_interest_deposit_10000_interest_1_point_1_annually_term_3(capsys):
    deposit, interest, term = 10000, 0.011, 3

    term_dep_details = calculator.TermDepositDetails(
        deposit,
        interest,
        term,
        calculator.InterestFreq.ANNUAL
        )

    interest_result = calculator.calculate_interest_total(term_dep_details)

    correct_interest = 334

    assert correct_interest == interest_result

def test_calc_interest_deposit_10000_interest_1_point_1_maturity_term_3(capsys):
    deposit, interest, term = 10000, 0.011, 3

    term_dep_details = calculator.TermDepositDetails(
        deposit,
        interest,
        term,
        calculator.InterestFreq.MATURITY
        )

    interest_result = calculator.calculate_interest_total(term_dep_details)

    correct_interest = 330

    assert correct_interest == interest_result
