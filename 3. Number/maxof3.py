# Prompt the user to enter the first number and convert the input to an integer
num1 = int(input("Enter the first number here: "))

# Prompt the user to enter the second number and convert the input to an integer
num2 = int(input("Enter the second number here: "))

# Prompt the user to enter the third number and convert the input to an integer
num3 = int(input("Enter the third number here: "))

# Use the max() function to determine the largest of the three numbers
largest = max(num1, num2, num3)

# Print out the largest number with a message
print("The largest number here is:", largest)
