
# Define a function to reverse a given string
def reverse_string(str):
    reverse = ""  # Initialize an empty string to store the reversed string
    for char in str:  # Iterate over each character in the input string
        reverse = char + reverse  # Prepend the current character to the reverse string
    return reverse  # Return the reversed string

# Prompt the user to enter a string
str = input("Enter your string: ")

# Call the reverse_string function and store the result in 'result'
result = reverse_string(str)

# Print the reversed string
print(result)
