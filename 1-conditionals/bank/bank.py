# Home Federal Savings Bank

# Prompt bank to greet
prompt = "Greeting: "

greeting = input(prompt).strip()

# Using String startswith() Method

if greeting.startswith("hello") or greeting.startswith("Hello"):
    print("$0")
elif greeting.startswith('h') or greeting.startswith("H"):
    print("$20")
else:
    print("$100")