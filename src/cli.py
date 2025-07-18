import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="poetry run cli", description="Calculate Term Deposit Interest"
    )
    parser.add_argument(
        "--deposit", help="The whole dollar amount for initial deposit.",
        type=int, required=True
    )

    parser.parse_args(argv)

    print("Use -h or --help to see usage")


if __name__ == "__main__":
    main()
