# Adieu, Adieu

# Importing the inflect module.
import inflect

# Creating an instance of the inflect module.
p = inflect.engine()

# Creating an empty list called names.
names = []

# Creating an empty string called adieu_to_names.
adieu_to_names = ""

# Keep asking the user for a name until the user inputs control-d.
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        # Move user’s cursor to a new line if user inputs control-d
        print("\n", end="")
        break

# Joining the names in the list names with commas and an "and".
adieu_to_names = p.join(names)

# Printing the string "Adieu, adieu, to " followed by the string in the variable adieu_to_names.
print(f"Adieu, adieu, to {adieu_to_names}")
