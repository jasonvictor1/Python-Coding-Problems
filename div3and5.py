# Define a function that checks if numbers up to a given number are divisible by both 3 and 5
def divisible_by_3and5(num):
    # Create an empty list to store the numbers that meet the criteria
    result = []
    
    # Loop through each number up to the given number
    for i in range(num):
        # Check if the current number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            # Add the number to the result list if it meets the criteria
            result.append(i)
    
    # Return the list of numbers that are divisible by both 3 and 5
    return result

# Prompt the user to input a number
num = int(input("Enter your number: ")) # Note: Fixed the mismatched quotation mark here

# Call the function with the user's input and store the result
result = divisible_by_3and5(num)

# Print the result
print(result)
