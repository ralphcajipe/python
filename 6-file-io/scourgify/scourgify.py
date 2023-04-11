# Scourgify

# Importing the csv, sys, and os modules.
import csv
import sys
import os

if len(sys.argv) == 1:
    # Example: python scourgify.py
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    # Example: python scourgify.py 1.csv 2.csv 3.csv
    sys.exit("Too many command-line arguments")
elif os.path.isfile(sys.argv[1]) is False:
    # Example: python scourgify.py invalid_file.csv
    sys.exit("Could not read " + sys.argv[1])
else:
    # Example: python scourgify.py before.csv after.csv
    # Opening the file in read mode.
    with open(sys.argv[1], "r") as before:
        # Opening the file in write mode.
        with open(sys.argv[2], "w") as after:
            # Creating a reader and writer object.
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            # Iterating through the reader object and writing to the writer
            # object, after.csv, whose columns should be, in order of
            # first, last, and house.
            for row in reader:
                writer.writerow(
                    {
                        "first": row["name"].split(",")[1].strip(),
                        "last": row["name"].split(",")[0].strip(),
                        "house": row["house"],
                    }
                )
