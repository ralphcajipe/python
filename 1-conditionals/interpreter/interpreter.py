# Math Interpreter

# Approach 1
expression = input("Expression: ")
x, y, z = expression.split(" ")
expression = eval(expression)
print(f"{expression:.1f}")

# Approach 2
# interpret = eval(input("Expression: "))
# print(f"{interpret:.1f}")