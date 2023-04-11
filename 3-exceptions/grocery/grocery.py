# Grocery List

# Make an empty list for storing items.
items = []

adding_item_active = True

# Add items
while adding_item_active:
    try:
        line = input()
        items.append(line)
    except EOFError:
        # Move user’s cursor to a new line if user inputs control-d
        print("\n", end="")
        break

# Make an empty dictionary for storing counts.
counts = {}

for item in items:
    if item not in counts:
        counts[item] = 1
    else:
        counts[item] += 1

# Show user’s grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item.
for item in sorted(counts):
    print(f"{counts[item]} {item.upper()}")