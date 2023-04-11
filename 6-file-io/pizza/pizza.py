# Pizza Py

import sys
import os
from tabulate import tabulate

if len(sys.argv) == 1:
    # Example: python pizza.py
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    # Example: python pizza.py regular.csv sicilian.csv
    sys.exit("Too many command-line arguments")
elif not os.path.isfile(sys.argv[1]):
    # Example: python pizza.py invalid_file.csv
    sys.exit("File does not exist")
elif not sys.argv[1].endswith(".csv"):
    # Example: python pizza.py regular.txt
    sys.exit("Not a CSV file")
else:
    # Example: python pizza.py regular.csv
    # Opening the file, reading the lines, splitting the lines, and
    # printing the data in a table formatted in grid.
    with open(sys.argv[1], "r") as file:
        data = file.readlines()
        data = [line.strip().split(",") for line in data]
        print(tabulate(data, headers="firstrow", tablefmt="grid"))
