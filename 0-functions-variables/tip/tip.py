# Tip Calculator

def main():
    """Print the tip to leave for your server"""
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Accepts a str as input,
    remove the leading $,
    and return the amount as a float.
    """
    drop_dollars = d.replace("$", "")
    drop_dollars = float(drop_dollars)
    return drop_dollars


def percent_to_float(p):
    """
    Accepts a str as input,
    remove the trailing %,
    and return the percentage as a float
    """
    drop_percent = p.replace("%", "")
    drop_percent = float(drop_percent) / 100
    return drop_percent


main()