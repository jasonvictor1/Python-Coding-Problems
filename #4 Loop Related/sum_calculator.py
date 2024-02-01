
# Define a function called 'get_sum' that takes a list 'nums' as its parameter
def get_sum(nums):
    sum = 0  # Initialize a variable 'sum' to 0. This will store the running total.

    # Iterate over each number in the list 'nums'
    for num in nums:
        sum = sum + num  # Add the current number to the 'sum' variable

    return sum  # Return the calculated sum after going through all numbers

# Create a list of numbers
nums = [13, 89, 65, 42, 12, 11, 56]

# Call the 'get_sum' function with the 'nums' list and store the result in 'total'
total = get_sum(nums)

# Print the total sum of the elements in the list
print("The total of each elements: ", total)
