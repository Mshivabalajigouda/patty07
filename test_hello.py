"""Tests for hello.py."""

from hello import get_hello_message, main


def test_get_hello_message():
    """Test that get_hello_message returns 'Hello, World!'."""
    assert get_hello_message() == "Hello, World!"


def test_main(capsys):
    """Test that main prints 'Hello, World!' to stdout."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
