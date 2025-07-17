import src.cli as cli


def test_enter_name_and_say_hello(capsys, monkeypatch):
    # user_input = "Joe"
    # monkeypatch.setattr("sys.stdin", io.StringIO(user_input))

    expected = "Ok\n"

    cli.main()

    captured = capsys.readouterr()

    assert captured.out == expected
