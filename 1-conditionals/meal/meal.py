# Meal Time

def main():
    """Main program that determines the meal time"""
    meal_time = input("What time is it? ")

    if meal_time.startswith('7') or meal_time.startswith('8'):
        print("breakfast time")
    elif meal_time.startswith('12') or meal_time.startswith('13'):
        print("lunch time")
    elif meal_time.startswith('18') or meal_time.startswith('19'):
        print("dinner time")
    else:
        pass


def convert(time):
    """
    Converts time, a str in 24-hour format,
    to the corresponding number of hours as a float.
    i.e., 7 hours and 30 minutes, returns 7.5 (i.e., 7.5 hours).
    """
    pass


if __name__ == "__main__":
    """main() function call"""
    main()