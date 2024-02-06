
# Define a function to calculate the least common multiple (LCM) of two numbers
def calculate_lcm(x, y):
    lcm = max(x, y)  # Start with the maximum of x and y as the initial guess for LCM
    
    # Keep increasing the LCM guess until it is divisible by both x and y
    while lcm % x != 0 or lcm % y != 0:
        lcm += 1
    
    return lcm  # Return the calculated LCM

# Prompt the user to enter the first number
num1 = int(input("First number: "))

# Prompt the user to enter the second number
num2 = int(input("Second number: "))

# Call the calculate_lcm function with num1 and num2 as arguments
lcm = calculate_lcm(num1, num2)

# Print the LCM of num1 and num2
print(f"LCM of {num1} and {num2} is: {lcm}")
