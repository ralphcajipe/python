# Working 9 to 5

# Importing the regular expression module.
import re


def main():
    # Asking the user to input a 12 hour time and then printing the 24 hour time.
    print(convert(input("Hours: ")))


def convert(s):
    """
    It takes a 12 hour time in the format hh:mm AM/PM to hh:mm AM/PM or hh AM/PM to hh AM/PM and
    converts it to a 24 hour time in the format hh:mm to hh:mm

    :param s: The input string
    :return: the 24 hour time.
    """
    # Initializing the variable `time` to an empty string.
    time = ""

    # Matching the input string to the following format: hh:mm AM/PM to hh:mm AM/PM
    if time := re.match(r"(\d{1,2}):(\d{2}) (\w{2}) to (\d{1,2}):(\d{2}) (\w{2})", s):

        # Get the hours and minutes.
        hh = int(time.group(1))
        mm = int(time.group(2))
        ampm = time.group(3)
        hh2 = int(time.group(4))
        mm2 = int(time.group(5))
        ampm2 = time.group(6)

        # If there is "60" in the input string, raise an error.
        if "60" in s:
            raise ValueError(
                "Invalid time. 60 is not a valid minute in a 12 hour time."
            )

        # Convert the hours.
        # Converting 12 AM to 00.
        if ampm == "AM" and hh == 12:
            hh = 0
        # Converting 12 PM to 12.
        elif ampm == "PM" and hh != 12:
            hh += 12

        # Convert the hours2.
        # Converting 12 AM to 00.
        if ampm2 == "AM" and hh2 == 12:
            hh2 = 0
        # Converting 12 PM to 12.
        elif ampm2 == "PM" and hh2 != 12:
            hh2 += 12

        # Convert the minutes.
        if mm == 60:
            mm = 0
            hh += 1
        if mm2 == 60:
            mm2 = 0
            hh2 += 1

        # Return the 24 hour time.
        return "{:02d}:{:02d} to {:02d}:{:02d}".format(hh, mm, hh2, mm2)

    # Else if time is in the format hh AM/PM to hh AM/PM (i.e.,9 AM to 5 PM)
    elif time := re.match(r"(\d{1,2}) (\w{2}) to (\d{1,2}) (\w{2})", s):

        # Get the hours and minutes.
        hh = int(time.group(1))
        ampm = time.group(2)
        hh2 = int(time.group(3))
        ampm2 = time.group(4)

        # Convert the hours.
        if ampm == "AM" and hh == 12:
            hh = 0
        elif ampm == "PM" and hh != 12:
            hh += 12

        # Convert the hours2.
        if ampm2 == "AM" and hh2 == 12:
            hh2 = 0
        elif ampm2 == "PM" and hh2 != 12:
            hh2 += 12

        # In the format hh AM/PM to hh AM/PM (i.e., 9 AM to 5 PM),
        # there are no minutes so set them to 00.
        mm = 0
        mm2 = 0

        # Return the 24 hour time.
        return "{:02d}:{:02d} to {:02d}:{:02d}".format(hh, mm, hh2, mm2)

    # Raise error when given "9AM to 5PM" or something equivalent with no spaces.
    elif time := re.match(r"(\d{1,2}) (\w{2}) to (\d{1,2}) (\w{2})", s):
        raise ValueError("No spaces in the input.")

    # Raise error when input is in 24 hour format
    elif time := re.match(r"(\d{1,2}):(\d{2}) to (\d{1,2}):(\d{2})", s):
        raise ValueError("Invalid time format.")

    # Raise error when input has a dash instead of "to" in the middle of the time, for example "9 AM - 5 PM"
    elif time := re.match(r"(\d{1,2}) (\w{2}) - (\d{1,2}) (\w{2})", s):
        raise ValueError("Invalid time format.")

    # Raise error when input is given single digit minute, for example "10:7 AM - 5:1 PM"
    elif time := re.match(
        r"(\d{1,2}):(\d{1,2}) (\w{2}) - (\d{1,2}):(\d{1,2}) (\w{2})", s
    ):
        raise ValueError("Invalid time format.")
    else:
        raise ValueError("Invalid time format.")


if __name__ == "__main__":
    main()
