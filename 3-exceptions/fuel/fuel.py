# Fuel Gauge

# Set active flag
input_fraction_active = True

# Get user input
while input_fraction_active:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            # Prompt user again
            continue
        if y == 0:
            # Prompt user again
            continue
        break
    except (ValueError, ZeroDivisionError):
        pass

# Outputs x/y as a percentage rounded to the nearest integer
percentage = int((x / y) * 100)

if percentage < 1:
    print("E", end="")
elif percentage >= 99:
    print("F", end="")
else:
    print(f"{percentage}%", end="")

# Print a new line so that the user’s cursor (and subsequent prompt)
# doesn’t remain on the same line as your program’s own prompt.
print("\n", end="")