# Felipe’s Taqueria


def main():
    """
    Enables a user to place an order, prompting them for items,
    one per line, until the user inputs control-d.
    """

    # Initialize total cost of all items inputted
    total = 0

    # Menu of Felipe’s Taqueria
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    active = True

    while active:
        try:
            item = input("Item: ")
        except EOFError:
            # Move user’s cursor to a new line if user inputs control-d
            print("\n", end="")
            break
        except KeyError:
            pass
        else:
            total = compute_total(total, item, menu)


def compute_total(total, item, menu):
    """Compute the total cost of all items inputted thus far."""

    # To avoid or catch any KeyError
    item = item.title()

    if item in menu:
        total += menu[item]
        print(f"Total: ${total:.2f}")
    return total


if __name__ == '__main__':
    main()