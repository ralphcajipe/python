# Outdated

# Make a list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Get date
while True:
    date = input("Date: ")

    # For a format like 9/8/1636, look for a forward slash.
    if "/" in date:
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if month > 12 or month < 1:
                # Reprompt
                continue
            elif day > 31 or day < 1:
                # Reprompt
                continue
            elif year < 0:
                # Reprompt
                continue
        except ValueError:
            pass
        else:
            # Format month and day with leading zero
            print(f"{year}-{month:02}-{day:02}", end="")
            break

    # For a format like September 8, 1636, look for a space.
    elif " " in date:
        try:
            # Remove comma for clean positions
            date = date.replace(',', '')

            month, day, year = date.split(" ")
            month = int(months.index(month) + 1)
            day = int(day)
            year = int(year)
            if month > 12 or month < 1:
                # Reprompt
                continue
            elif day > 31 or day < 1:
                # Reprompt
                continue
            elif year < 0:
                # Reprompt
                continue
        except ValueError:
            pass
        else:
            # Format month and day with leading zero
            print(f"{year}-{month:02}-{day:02}", end="")
            break

# Print a new line so that the user’s cursor (and subsequent prompt)
# doesn’t remain on the same line as your program’s own prompt.
print("\n", end="")