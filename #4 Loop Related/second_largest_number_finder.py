
# Define a function named 'get_second_largest' that takes a list 'nums' as its argument
def get_second_largest(nums):
    largest = nums[0]  # Initialize 'largest' with the first element of the list
    second_largest = nums[0]  # Initialize 'second_largest' also with the first element

    # Iterate over the list starting from the second element
    for i in range(1, len(nums)):
        if nums[i] > largest:
            second_largest = largest  # Update 'second_largest' before updating 'largest'
            largest = nums[i]  # Update 'largest' if the current element is greater
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]  # Update 'second_largest' if current element is the second largest

    return second_largest  # Return the second largest number

# Create a list of numbers called 'my_nums'
my_nums = [44, 11, 83, 29, 25, 76, 88]

# Call the 'get_second_largest' function with the list 'my_nums' and store the result in 'second_largest'
second_largest = get_second_largest(my_nums)

# Print the second highest number found in the list
print("Second highest number is: ", second_largest)
