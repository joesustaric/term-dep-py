import pytest

import src.cli as cli


def test_cli_with_no_args(capsys):

    with pytest.raises(SystemExit):
        cli.main()

    captured = capsys.readouterr()
    result = (
        "poetry run cli: error: the following arguments are required:"
        " --deposit, --interest, --length"
        )

    assert result in captured.err


def test_cli_with_help_flag(capsys):

    with pytest.raises(SystemExit):
        cli.main(["--help"])

    description = "Calculate Term Deposit Interest"
    deposit_flag = " --deposit DEPOSIT    The dollar amount for initial deposit e.g. 1000"
    interest_flag = "--interest INTEREST  The term deposit interest rate percent e.g. 1.1"
    length_flag = "--length LENGTH      The term deposit length in years e.g. 3"

    captured = capsys.readouterr()

    assert description in captured.out
    assert deposit_flag in captured.out
    assert interest_flag in captured.out
    assert length_flag in captured.out

# def test_cli_with_help_flag(capsys):

#     with pytest.raises(SystemExit):
#         cli.main(["--deposit", "10000"])

#     result = "error: the following arguments are required: --interest, --length"

#     captured = capsys.readouterr()

#     assert result in captured.err

