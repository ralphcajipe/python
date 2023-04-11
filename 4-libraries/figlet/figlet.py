# Frank, Ian and Glen’s Letters

import sys
import random
from pyfiglet import Figlet

# Check for command line arguments
# No command-line arguments if user would like to output text in random font
# Usage: python figlet.py
if len(sys.argv) == 1:
    user_input = input("Input: ")
    font = random.choice(Figlet().getFonts())
    print(Figlet(font=font).renderText(user_input))

# Two command-line arguments if the user would like to output text in a specific font
# for example: python figlet.py -f slant
# len(sys.argv) == 3 means 3 arguments (for example, figlet.py -f slant)
elif len(sys.argv) == 3:
    # Check for -f or --font
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        # Check if the font is valid
        if sys.argv[2] in Figlet().getFonts():
            user_input = input("Input: ")
            print(Figlet(font=sys.argv[2]).renderText(user_input))
        # Else invalid font
        else:
            print("Invalid usage")
            sys.exit(1)
    # Else not -f nor --font
    else:
        print("Invalid usage")
        sys.exit(1)

# Else unknown command-line arguments
else:
    print("Invalid usage")
    sys.exit(1)