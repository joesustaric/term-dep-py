import pytest

import src.cli as cli


def test_cli_with_help_flag(capsys):
    with pytest.raises(SystemExit):
        cli.main(["--help"])

    captured = capsys.readouterr()
    assert "Calculate Term Deposit Interest" in captured.out


def test_cli_with_no_args(capsys):
    cli.main([])

    captured = capsys.readouterr()

    assert captured.err == "Use -h or --help to see usage"


# def test_cli_with_custom_args(capsys):
#     # Easy to test with any arguments
#     cli.main(['--amount', '1000', '--interest', '5.5'])
#
#     captured = capsys.readouterr()
#
#     # Assert your expectations
#     assert "Ok" in captured.out
