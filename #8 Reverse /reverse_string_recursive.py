
# Define a function to reverse a string using recursion
def reverse_recur(str):
    # Base case: if the string is empty, return the string itself
    if len(str) == 0:
        return str
    else:
        # Recursive case: call reverse_recur with the string except the first character
        # and then add the first character to the end of the result
        return reverse_recur(str[1:]) + str[0]

# Prompt the user to enter a string
str = input("Enter your string: ")

# Call the reverse_recur function to reverse the entered string
rev_str = reverse_recur(str)

# Print the reversed string
print('Reverse of your string: ', rev_str)
