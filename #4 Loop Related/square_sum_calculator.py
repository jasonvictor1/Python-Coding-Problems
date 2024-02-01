
# Define a function named 'square_sum' that takes an integer 'num' as its argument
def square_sum(num):
    sum = 0  # Initialize a variable 'sum' to 0. This will hold the sum of squares.

    # Iterate over a range from 0 to 'num' inclusive
    for i in range(num + 1):
        square = (i ** 2)  # Calculate the square of 'i'
        sum = sum + square  # Add the square of 'i' to the 'sum'

    return sum  # Return the total sum of squares

# Prompt the user to enter a number and convert it to an integer
num = int(input("Enter a number: "))

# Call the 'square_sum' function with the entered number and store the result in 'sum'
sum = square_sum(num)

# Print the sum of squares up to the entered number
print("sum of square numbers is ", sum)
