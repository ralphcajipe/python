# Lines of Code

import sys
import os

if len(sys.argv) == 1:
    # Example: python lines.py
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    # Example: python lines.py hello.py goodbye.py
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    # Example: python lines.py invalid_extension.txt
    # When we access index of sys.argv, we start at 1, not 0, because sys.argv[0] is the name of the program.
    # Where sys.argv[0] is lines.py and sys.argv[1] is an invalid extension.
    # Example: python lines.py invalid_extension.txt
    sys.exit("Not a Python file")
elif not os.path.isfile(sys.argv[1]):
    # Example: python lines.py non_existent_file.py
    sys.exit("File does not exist")
else:
    # Example: python lines.py hello.py
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
        # Count lines excluding comments and whitespace
        count = 0
        for line in lines:
            if (
                not line.startswith("#")
                and not line.lstrip().startswith("#")
                and not line.isspace()
            ):
                count += 1
        print(count)
