
# Define functions for basic arithmetic operations

def add(num1, num2):
    # Return the sum of num1 and num2
    return num1 + num2

def subtract(num1, num2):
    # Return the difference of num1 and num2
    return num1 - num2

def multiply(num1, num2):
    # Return the product of num1 and num2
    return num1 * num2

def divide(num1, num2):
    # Return the division of num1 by num2
    return num1 / num2

def modulo(num1, num2):
    # Return the remainder of num1 divided by num2
    return num1 % num2

# Prompt the user to input the first number, operation, and the second number
num1 = int(input("Enter first number: "))
operation = input("What you want to do(+, -, *, /, %):")
num2 = int(input("Enter second number: "))

# Initialize result variable to store the outcome of the operation
result = 0

# Perform the operation based on the user's input
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
elif operation == '%':
    result = modulo(num1, num2)
else:
    print("Invalid operation. Please enter: +, -, *, /, or %")

# Print the result of the operation
print(num1, operation, num2, '=', result)
