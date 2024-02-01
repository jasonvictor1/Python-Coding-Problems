
# Define a function named 'get_largest' that takes a list called 'nums' as its argument
def get_largest(nums):
    largest = nums[0]  # Initialize 'largest' with the first element of the list. This will hold the largest number found.

    # Iterate over each number in the list 'nums'
    for num in nums:
        if num > largest:  # Check if the current number is greater than the current 'largest' number
            largest = num  # Update 'largest' to be this number if it is greater

    return largest  # Return the largest number found in the list

# Create a list of numbers called 'my_nums'
my_nums = [0, 15, 68, 1, 0, -55]

# Call the 'get_largest' function with the list 'my_nums' and store the result in 'largest'
largest = get_largest(my_nums)

# Print the largest number found in the list
print("The largest number is: ", largest)
