# Define a function to remove duplicate items from a list
def remove_duplicate(items):

    # Create an empty list to store unique items
    unique = []

    # Iterate through each item in the provided list
    for item in items:

        # Check if the current item is not already in the unique list
        if item not in unique:

            # If the item is unique, add it to the unique list
            unique.append(item)

    # Return the list containing only unique items
    return unique


# Sample list of numbers with duplicates
numbers = [22, 11, 3, 1, 4, 5, 5, 2, 2, 11, 66, 89]

# Test the function with the sample list and print the result
print(remove_duplicate(numbers))
