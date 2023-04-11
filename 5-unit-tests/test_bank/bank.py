# Home Federal Savings Bank version 2


def main():
    """
    The function `main()` prompts the user for a greeting, then passes the greeting to the function
    `value()` which returns a value based on the greeting
    """
    # Prompt bank to greet
    prompt = "Greeting: "

    greeting = input(prompt).strip()
    print(value(greeting))


def value(greeting):
    """
    If the greeting starts with "hello" or "Hello", return "$0".
    If the greeting starts with "h" or "H", return "$20".
    Otherwise, return "$100"

    :param greeting: The string that you want to check
    :return: the value of the greeting.
    """
    # Using String startswith() Method
    if greeting.startswith("hello") or greeting.startswith("Hello"):
        return 0
    elif greeting.startswith("h") or greeting.startswith("H"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
