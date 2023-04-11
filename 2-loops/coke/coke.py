# Coke Machine

# CONSTANTS
AMOUNT_DUE = 50
cents_25 = 25
cents_10 = 10
cents_5 = 5

# Initialize coin as zero
insert_coin = 0

# Display default amount due which is 50
print(f"Amount Due: {AMOUNT_DUE}")

while insert_coin < 51:
    insert_coin = int(input("Insert Coin: "))

    # If coin is 25 cents
    if insert_coin == cents_25:
        AMOUNT_DUE = AMOUNT_DUE - insert_coin

        if AMOUNT_DUE == 0:
            print("Changed Owed: 0")
            break
        elif AMOUNT_DUE == -10:
            print("Change Owed: 10")
            break
        else:
            print(f"Amount due: {AMOUNT_DUE}")

    # Else if coin is 10 cents
    elif insert_coin == cents_10:
        AMOUNT_DUE = AMOUNT_DUE - insert_coin

        if AMOUNT_DUE == 0:
            print("Changed Owed: 0")
            break
        else:
            print(f"Amount due: {AMOUNT_DUE}")

    # Else if coin is 5 cents
    elif insert_coin == cents_5:
        AMOUNT_DUE = AMOUNT_DUE - insert_coin

        if AMOUNT_DUE == 0:
            print("Changed Owed: 0")
            break
        else:
            print(f"Amount due: {AMOUNT_DUE}")

    # Else if coin is the default amount due of 50
    elif insert_coin == 50:
        AMOUNT_DUE = AMOUNT_DUE - 0

        if AMOUNT_DUE == 0:
            print("Changed Owed: 0")
            break
        else:
            print(f"Amount due: {AMOUNT_DUE}")

    # Else invalid amount of cents
    else:
        AMOUNT_DUE = AMOUNT_DUE - 0

        if AMOUNT_DUE == 0:
            print("Changed Owed: 0")
            break
        else:
            print(f"Amount due: {AMOUNT_DUE}")