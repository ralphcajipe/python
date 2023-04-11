# Just setting up my twttr version 2


def main():
    """
    It takes a word as input, and prints the word with all vowels removed.
    """
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    """
    It takes a word as an argument, and returns a new word with all vowels removed

    :param word: The word to shorten
    :return: The word with all vowels removed.
    """
    vowels_to_omit = "AEIOUaeiou"

    for character in vowels_to_omit:
        word = word.replace(character, "")
    return f"{word}"


if __name__ == "__main__":
    main()


"""
# Just setting up my twttr version 1

text = input("Input: ")

vowels_to_omit = "AEIOUaeiou"

for character in vowels_to_omit:
    text = text.replace(character, "")

print(f"Output: {text}")
"""