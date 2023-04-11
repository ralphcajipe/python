# Deep Thought

# Prompt user for an answer
prompt = "What is the answer to the Great Question of Life, " \
         "the Universe and Everything? "

answer = input(prompt)

# Cases
forty_two = "forty two"
forty_two_title = "Forty Two"
# Cases with hyphen won't be a problem due to their absence of space in between

# If user answers number 42.
# Remove spaces on either side if there are
if answer.strip() == "42":
    print("Yes")

# If user answers in lowercase with hyphen
# Remove spaces on either side if there are
elif answer.strip() == "forty-two":
    print("Yes")
# If user answers in titlecase with hyphen
# Remove spaces on either side if there are
elif answer.strip() == "Forty-Two":
    print("Yes")

# If user answers in lowercase with space in between
# Remove spaces on either side if there are
elif answer.lstrip().rstrip() == forty_two:
    print("Yes")
# If user answers in titlecase with space in between
# Remove spaces on either side if there are
elif answer.lstrip().rstrip() == forty_two_title:
    print("Yes")

# If user answers in mixed case with space in between
# Remove spaces on either side if there are
elif answer.upper().lower().lstrip().rstrip() == forty_two:
    print("Yes")
else:
    print("No")