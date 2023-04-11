# Fuel Gauge version 2


def main():
    """
    Prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
    and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
    """
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    """
    It takes a fraction as a string, and returns a tuple of the numerator and denominator

    Expects a str in X/Y format as input, wherein each of X and Y is an integer,
    and returns that fraction as a percentage, an int between 0 and 100, inclusive.
    If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
    If Y is 0, then convert should raise a ZeroDivisionError.

    :param fraction: The fraction of the total number of rows to be converted
    """
    # Splitting the fraction into a list of two strings, the numerator and denominator.
    fraction_list = fraction.split("/")

    # This is checking if the fraction is in the correct format. If the fraction is not in the correct
    # format, it will raise a ValueError.
    if len(fraction_list) != 2:
        raise ValueError
    x = fraction_list[0]
    y = fraction_list[1]
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        percentage = round((x / y) * 100)
    else:
        raise ValueError
    return percentage


def gauge(percentage):
    """
    It takes a percentage and returns a string that represents a gauge.
    Expects an int and returns a str that is:
    "E" if that int is less than or equal to 1,
    "F" if that int is greater than or equal to 99,
    and "Z%" otherwise, wherein Z is that same int.

    :param percentage: The percentage of the gauge to fill
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
