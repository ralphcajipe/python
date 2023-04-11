# camelCase to snake_case

def main():
    """Prompts user for variable name in camelCase and displays
    the corresponding name in snake_case."""
    variable = input("camelCase: ")
    print("snake_case: ", end="")

    # Pass variable as argument to snake_case function call
    snake_case(variable)


def snake_case(variable):
    """Algorithm for converting camelCase into snake_case."""
    for each_letter in variable:
        if each_letter == each_letter.upper():
            each_letter = f"_{each_letter.lower()}"
        print(each_letter, end="")
    # Required to print a new line for good readability
    print("")


if __name__ == '__main__':
    main()