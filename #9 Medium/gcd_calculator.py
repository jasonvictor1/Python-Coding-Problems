
# Define a function to compute the greatest common divisor (GCD) of two numbers
def compute_gcd(x, y):
    smaller = min(x, y)  # Determine the smaller of the two numbers
    gcd = 1  # Initialize gcd to 1
    
    # Iterate from 1 to 'smaller' (inclusive) to find the highest number that divides both 'x' and 'y'
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i  # Update 'gcd' if 'i' is a common divisor of both 'x' and 'y'
    
    return gcd  # Return the greatest common divisor

# Prompt the user to enter the first number
num1 = int(input("Enter first number: "))

# Prompt the user to enter the second number
num2 = int(input("Enter second number: "))

# Call the compute_gcd function with 'num1' and 'num2' as arguments
gcd = compute_gcd(num1, num2)

# Print the GCD of 'num1' and 'num2'
print("GCD of", num1, "and", num2, "is", gcd)
