# Vanity Plates version 2


def main():
    """
    The function is_valid() takes a string as input and returns True if the string is a valid vanity
    plate and False otherwise.

    Assume that any letters in the user's input will be uppercase.
    """
    plate = input("Plate: ")
    print(is_valid(plate))


def is_valid(plate):
    """
    If the length of the string is less than 2 or greater than 6, or if the first two characters are not
    letters, or if the characters after the first two characters are not digits, or if the first digit
    is a 0, then the function returns False. Otherwise, it returns True.

    :param plate: The string that is being checked
    :return: The function is_valid is returning True if the string meets all the requirements and False
    if it does not.
    """
    # This is checking if the length of the string is less than 2 or greater than 6. If it is, it
    # returns False.
    if len(plate) < 2 or len(plate) > 6:
        return False

    # This is checking if the first two characters are not letters. If they are not, it returns False.
    elif not plate[0].isalpha() or not plate[1].isalpha():
        return False

    # This is checking if the characters after the first two characters are not digits. If they are
    # not, it returns False.
    elif not plate[2:].isdigit():
        return False

    # This is checking if the first digit is a 0. If it is, it returns False.
    elif plate[2] == "0":
        return False

    # This is checking if the characters after the first two characters are digits. If they are, it
    # returns True.
    elif plate[2:].isdigit():
        return True

    # Returning False if the string does not meet the requirements.
    else:
        return False


if __name__ == "__main__":
    main()
