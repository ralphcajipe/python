# Emojize

import emoji

name = input("Input: ")
emojized = emoji.emojize(name, language='alias')
print(f"Output: {emojized}")