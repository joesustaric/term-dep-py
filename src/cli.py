import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(description="Calculate Term Deposit Interest")

    parser.parse_args(argv)

    print("Use -h or --help to see usage")


if __name__ == "__main__":
    main()
