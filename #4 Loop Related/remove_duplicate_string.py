
# Define a function named 'remove_duplicate' that takes a string 'your_str' as its argument
def remove_duplicate(your_str):
    result = ""  # Initialize an empty string 'result' to store the characters without duplicates

    # Iterate over each character in the string 'your_str'
    for char in your_str:
        if char not in result:
            result += char  # Add the character to 'result' if it's not already present

    return result  # Return the string after removing duplicates

# Prompt the user to enter a string
user_input = input("What is your string?: ")

# Call the 'remove_duplicate' function with the user input and store the result in 'no_duplicate'
no_duplicate = remove_duplicate(user_input)

# Print the string after removing duplicates
print("Without duplicate: ", no_duplicate)
