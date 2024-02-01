
# Define a function named 'get_second_smallest' that takes a list 'nums' as its argument
def get_second_smallest(nums):
    smallest = nums[0]  # Initialize 'smallest' with the first element of the list
    second_smallest = nums[0]  # Initialize 'second_smallest' also with the first element

    # Iterate over the list starting from the second element
    for i in range(1, len(nums)):
        if nums[i] < smallest:
            second_smallest = smallest  # Update 'second_smallest' before updating 'smallest'
            smallest = nums[i]  # Update 'smallest' if the current element is smaller
        elif nums[i] < second_smallest and nums[i] != smallest:
            second_smallest = nums[i]  # Update 'second_smallest' if current element is the second smallest

    return second_smallest  # Return the second smallest number

# Create a list of numbers called 'my_nums'
my_nums = [44, 11, 83, 29, 25, 76, 88]

# Call the 'get_second_smallest' function with the list 'my_nums' and store the result in 'second_smallest'
second_smallest = get_second_smallest(my_nums)

# Print the second smallest number found in the list
print("Second smallest number is: ", second_smallest)
