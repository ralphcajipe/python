# Making Faces

def convert(message):
    """
    Accepts a str as input and returns that same input with...
    any :) converted to 🙂 (otherwise known as a slightly smiling face) and...
    any :( converted to 🙁 (otherwise known as a slightly frowning face).
    All other text should be returned unchanged.
    """

    words = message.split(" ")

    # emoticon to emoji
    emojis_dict = {
        ":)": "🙂",
        ":(": "🙁",
    }

    face_result = ""
    for word in words:
        face_result += emojis_dict.get(word, word) + " "
    print(face_result)


def main():
    """Prompts the user for input, calls convert on that input,
    and prints the result."""

    message = input("")

    # function call for convert(message)
    convert(message)


main()