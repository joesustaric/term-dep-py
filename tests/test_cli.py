import pytest

import src.cli as cli


def test_cli_with_help_flag(capsys):
    
    with pytest.raises(SystemExit):
        cli.main(["--help"])

    description = "Calculate Term Deposit Interest"
    amount_flag = "--deposit DEPOSIT  The whole dollar amount for initial deposit."

    captured = capsys.readouterr()

    assert description in captured.out
    assert amount_flag in captured.out


def test_cli_with_no_args(capsys):

    with pytest.raises(SystemExit):
        cli.main()

    captured = capsys.readouterr()

    result = "usage: poetry run cli [-h] --deposit DEPOSIT\n"

    assert result in captured.err


# def test_cli_with_custom_args(capsys):
#     # Easy to test with any arguments
#     cli.main(['--amount', '10000', '--interest', '1.1', '--years', '3'])

#     captured = capsys.readouterr()

#     # Assert your expectations
#     assert "Ok" in captured.out
