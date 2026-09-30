"""Hello World program module."""


def get_hello_message() -> str:
    """Return the hello world greeting string."""
    return "Hello, World!"


def main() -> None:
    """Print the hello world greeting."""
    print(get_hello_message())


if __name__ == "__main__":
    main()
