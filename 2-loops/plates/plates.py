# Vanity Plates

# To access string constants
import string


def main():
    """Prompts the user for a vanity plate and check if Valid or Invalid."""
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """Check if plate meets all requirements to be tagged as Valid."""

    # All vanity plates must start with *at least* two letters.
    if not s[0:2].isalpha():
        return False

    # Plates may contain a maximum of 6 characters (letters or numbers)
    # and a minimum of 2 characters.
    if not 2 <= len(s) <= 6:
        return False

    # Numbers can't be used in the middle of a plate; must come at the end.
    # The first number used cannot be a zero ‘0’.
    for i in range(len(s)):
        character = s[i]
        if character.isdigit():
            if character == '0':
                return False
            elif not s[i].isdigit():
                return False
            break

    # No periods, spaces, or punctuation marks are allowed.
    punctuation_marks = string.punctuation

    for character in s:
        if character.isspace():
            return False
        if character == punctuation_marks:
            return False

    # is_valid(s) function must return something
    return True


# Main
if __name__ == '__main__':
    main()