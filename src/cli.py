import argparse
import sys

from src.calculator import calculate_interest_total
from src.input_validator import ValidationException, validate_inputs
from src.models.term_deposit_details import InterestFreq, TermDepositDetails
from src.writer import print_result

TRANSLATOR = {
    "m": InterestFreq.MONTH,
    "a": InterestFreq.ANNUAL,
    "q": InterestFreq.QUARTER,
    "t": InterestFreq.MATURITY
}

def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="poetry run cli", description="Calculate Term Deposit Interest"
    )
    parser.add_argument(
        "--deposit", help="The dollar amount for initial deposit - range 1-1000000",
        type=int, required=True
    )
    parser.add_argument(
        "--interest", help="The term deposit interest rate percent - range 1 - 0.0 ",
        type=float, required=True
    )
    parser.add_argument(
        "--years", help="The term deposit length in years - range 0-5",
        type=int, required=True
    )
    parser.add_argument(
        "--months", help="The term deposit length in months - range 0-11",
        type=int, required=True
    )
    parser.add_argument(
        "--frequency",
        help="The frequency of interest payments - m=monthly, a=annual q=quarterly, t=maturity",
        type=str, required=True
    )
    try:
        args = parser.parse_args(argv)
        validate_inputs(
            args.deposit,
            args.interest,
            args.years,
            args.months,
            args.frequency.lower()
        )
        result = calculate_interest_total(
            TermDepositDetails(
                args.deposit,
                args.interest,
                args.years,
                args.months,
                TRANSLATOR[args.frequency.lower()]
            )
        )
        print_result(result)
    except ValidationException as e:
        print(e, file=sys.stderr)
        raise e

if __name__ == "__main__":
    main()
