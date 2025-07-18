import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="term-dep-calc", description="Calculate Term Deposit Interest"
    )
    parser.add_argument(
        "--deposit", help="The whole dollar amount for initial deposit."
    )

    parser.parse_args(argv)

    print("Use -h or --help to see usage")


if __name__ == "__main__":
    main()
