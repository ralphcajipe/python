# “Seasons of Love,” Rent 🎶

import sys

import datetime
import inflect
import re


def main():
    print(sing(input("Date of Birth: ")))


def sing(birthdate):
    """
    It takes a date in the format YYYY-MM-DD, converts it to a datetime object,
    calculates the number of minutes since that date, converts the number of
    minutes to words, and returns the result

    :param birthdate: The date the user was born
    :return: The number of minutes since the user was born.
    """
    # This is checking if the input is in the correct format.
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", birthdate):
        sys.exit("Invalid date")

    # Split the date to get the year, month and day.
    year, month, day = birthdate.split("-")

    # Convert the date to a datetime object.
    birthdate = datetime.date(int(year), int(month), int(day))

    # Calculate the number of minutes since the user was born.
    minutes = (datetime.date.today() - birthdate).days * 24 * 60

    # Convert the number of minutes to words.
    # Remove the "and" between words.
    words = inflect.engine().number_to_words(minutes).replace(" and ", " ")

    # Set the first letter of the first word to title case and conctenate the
    # rest of the words.
    words = words[0].title() + words[1:]

    # Adding the word "minutes" to the end of the string.
    words += " minutes"

    return words


if __name__ == "__main__":
    main()
    sys.exit(0)
