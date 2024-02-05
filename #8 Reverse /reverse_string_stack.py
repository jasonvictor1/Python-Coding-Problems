
# Define a function to reverse a string using a stack
def reverse_stack(str):
    # Create an empty stack (list to use as stack)
    stack = []
    # Push all characters of string to stack
    for char in str:
        stack.append(char)
    # Initialize an empty string for the reversed version
    rev = ''
    # Pop all characters of string from the stack and add it to 'rev'
    while len(stack) > 0:
        last = stack.pop()  # Pop the last character from the stack
        rev = rev + last  # Add the popped character to 'rev'
    # Return the reversed string
    return rev

# Prompt the user to enter a string
usr_str = input('What is your string:')
# Call the reverse_stack function to reverse the entered string
reverse = reverse_stack(usr_str)
# Print the reversed string
print('Reversed is: ', reverse)
