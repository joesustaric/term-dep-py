from src import calculator


def test_calculate_interest(capsys):
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
