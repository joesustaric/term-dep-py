import argparse
from decimal import Decimal


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="poetry run cli", description="Calculate Term Deposit Interest"
    )
    parser.add_argument(
        "--deposit", help="The dollar amount for initial deposit e.g. 1000",
        type=int, required=True
    )
    parser.add_argument(
        "--interest", help="The term deposit interest rate percent e.g. 1.1",
        type=Decimal, required=True
    )
    parser.add_argument(
        "--length", help="The term deposit length in years e.g. 3",
        type=int, required=True
    )

    args = parser.parse_args(argv)
    deposit = args.deposit
    interest = args.interest
    length = args.length


if __name__ == "__main__":
    main()
