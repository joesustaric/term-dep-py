import argparse
from decimal import Decimal


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
        type=Decimal, required=True
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
        type=int, required=True
    )

    parser.parse_args(argv)
    # args = parser.parse_args(argv)
    # deposit = args.deposit
    # interest = args.interest
    # length = args.length


if __name__ == "__main__":
    main()
