import pytest

import src.cli as cli

from .test_input_validator import ValidationException


def test_cli_with_no_args(capsys):

    with pytest.raises(SystemExit):
        cli.main()

    captured = capsys.readouterr()
    result = (
        "poetry run cli: error: the following arguments are required:"
        " --deposit, --interest, --years"
        )

    assert result in captured.err


def test_cli_with_help_flag(capsys):

    with pytest.raises(SystemExit):
        cli.main(["--help"])

    # Not asserting on the description
    # just that there is something showing how to use in the --help menu
    description = "Calculate Term Deposit Interest"
    deposit_flag = " --deposit DEPOSIT "
    interest_flag = "--interest INTEREST "
    years_flag = "--years YEARS"
    months_flag = "--months MONTHS"
    freq_flag = "--frequency FREQUENCY"

    captured = capsys.readouterr()

    assert description in captured.out
    assert deposit_flag in captured.out
    assert interest_flag in captured.out
    assert years_flag in captured.out
    assert months_flag in captured.out
    assert freq_flag in captured.out

def test_cli_validates_args(capsys):

    with pytest.raises(ValidationException):
        cli.main([
            "--deposit", "10000",
            "--interest", "0.011",
            "--years", "3",
            "--months", "45",
            "--frequency", "asdf"
            ])

    result = "invalid"

    captured = capsys.readouterr()

    assert result in captured.err


#     with pytest.raises(SystemExit):
#         cli.main([
#             "--deposit", "10000",
#             "--interest", "0.011",
#             "--years", "3",
#             "--months", "0",
#             "--"])

#     result = "error: the following arguments are required: --interest, --length"

#     captured = capsys.readouterr()

#     assert result in captured.err

