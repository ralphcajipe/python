# Importing the random and sys modules.
import random
import sys

# Asking the user to input a level.
# If the user does not input a positive integer, the program should prompt again.
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue

# Generate a random number between 1 and the level that the user inputs.
number = random.randint(1, level)

# Asking the user to input a guess.
# If the user does not input a positive integer, the program should prompt again.
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            break
    except ValueError:
        continue

# Checking if the guess is not equal to the random number.
while guess != number:
    # Checking if the guess is greater than the number. If it is, it will print "Too large!"
    # and ask the user to input a guess again.
    try:
        if guess > number:
            print("Too large!")
        # Checking if the guess is less than the number. If it is, it will print "Too small!"
        # and ask the user to input a guess again.
        elif guess < number:
            print("Too small!")
        guess = int(input("Guess: "))
    except ValueError:
        continue

# If the guess is the same as the random number,
# the program should output: Just right! and exit.
sys.exit("Just right!")