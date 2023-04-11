# Regular, um, Expressions

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    """
    It returns the number of times the word "um" appears in the string s

    :param s: The string to search
    :return: The number of times the word "um" appears in the string.
    """
    # `\b` argument makes the search match only at the beginning or end of the
    # word and `re.I argument` makes the search case-insensitive.
    return len(re.findall(r"\bum\b", s, re.I))


if __name__ == "__main__":
    main()
    sys.exit(0)
