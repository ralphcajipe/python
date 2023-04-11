# CS50 P-Shirt

import os
import sys

from PIL import Image, ImageOps


# Checking if the number of command-line arguments is less than 3.
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
# Checking if the number of command-line arguments is greater than 3.
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
# Checking if the input file exists.
elif not os.path.exists(sys.argv[1]):
    sys.exit("Input does not exist")
# Checking if the input file is not a .jpg, .jpeg, or .png file.
elif (
    not sys.argv[1].endswith(".jpg")
    and not sys.argv[1].endswith(".jpeg")
    and not sys.argv[1].endswith(".png")
):
    sys.exit("Invalid input")
# Checking if the output file is not a .jpg, .jpeg, or .png file.
elif (
    not sys.argv[2].endswith(".jpg")
    and not sys.argv[2].endswith(".jpeg")
    and not sys.argv[2].endswith(".png")
):
    sys.exit("Invalid output")
# Checking if the input and output file extensions are not the same.
elif sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".png"):
    sys.exit("Input and output have different extensions")

# Opening the shirt.png file and then opening the input file. Then it is fitting the input file to the
# size of the shirt.png file. Then it is pasting the input file onto the shirt.png file. Then it is
# saving the output file.
shirt = Image.open("shirt.png")
size = shirt.size
photo = Image.open(sys.argv[1])
photo = ImageOps.fit(
    photo, size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5)
)
photo.paste(shirt, shirt)
photo.save(sys.argv[2])
