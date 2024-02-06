
import math  # Import the math module to use the sqrt function

# Prompt the user to enter the lengths of the sides of a triangle
a = float(input("Enter first side: "))  # Length of the first side
b = float(input("Enter second side: "))  # Length of the second side
c = float(input("Enter third side: "))  # Length of the third side

# Calculate the semi-perimeter of the triangle
s = (a + b + c) / 2

# Calculate the area of the triangle using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Print the area of the triangle
print("Area of your triangle is: ", area)
