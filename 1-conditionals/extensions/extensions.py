# File Extensions

# Prompt user for the name of a file
# and then outputs that file’s media type

prompt = "File name: "

# Behave as expected, case- and space-insensitively
filename = input(prompt).strip().lower()

# image/
if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpg"):
    print("image/jpeg")
elif filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")

# application/
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".zip"):
    print("application/zip")

# text/
elif filename.endswith(".txt"):
    print("text/plain")

# If file’s name ends with some other suffix or has no suffix at all
else:
    print("application/octet-stream")