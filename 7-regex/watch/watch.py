# Watch on YouTube

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    If the string `s` contains an `iframe` tag, then extract the `src` attribute from the `iframe` tag.
    If the `src` attribute contains the string `youtube`, then replace the `src` attribute with a
    shortened, shareable `youtu.be` URL.

    :param s: the string to be parsed
    :return: the value of the variable `url`
    """
    iframe = re.search(r'<iframe.*src="(.*?)".*>', s)
    if iframe:
        # `url = iframe.group(1)` is assigning the value of the first group in the regular expression
        # to the variable `url`.
        url = iframe.group(1)
        if 'youtube' in url:
            return re.sub(r'^https?:\/\/(www\.)?youtube\.com\/embed\/', 'https://youtu.be/', url)
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    main()
