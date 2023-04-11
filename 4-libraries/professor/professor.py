# Little Professor

import random


def main():
    """
    It gets the level from the user and then calls the answer_input function with the level as an
    argument.
    """
    level = get_level()
    answer_input(level)


def get_level():
    """
    It returns the level of the player.
    """
    # If the user does not input 1, 2, or 3, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except ValueError:
            # Invalid level
            continue


def generate_integer(level):
    """
    It generates a random integer between 1 and 10.

    :param level: The level of the integer to be generated
    """
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


def answer_input(level):
    """
    :param level: The level of the question
    """
    correct_answers = 0
    for i in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        print(num1, "+", num2, "=", sep=" ", end=" ")

        answer = int(input(""))
        # If answer is numeric, allow the user up to three tries in total.
        # If the user has still not answered correctly after three tries,
        # the program should output the correct answer to the question.
        for j in range(1, 3):
            if answer == int(answer) and answer == num1 + num2:
                correct_answers += 1
                break
            elif answer != num1 + num2:
                print("EEE")
                print(num1, "+", num2, "=", sep=" ", end=" ")
                answer = int(input(""))
            elif answer != int(answer):
                print("EEE")
                print(num1, "+", num2, "=", sep=" ", end=" ")
                answer = int(input(""))

        # Printing the correct answer to the question.
        else:
            print("EEE")
            print(f"{num1} + {num2} = {num1 + num2}")

    # The program should ultimately output the user’s score
    print(f"Score: {correct_answers}/10")


if __name__ == "__main__":
    main()
