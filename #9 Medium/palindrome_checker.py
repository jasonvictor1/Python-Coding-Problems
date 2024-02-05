
# Prompt the user to enter a string to check if it is a palindrome
my_str = input('String to check: ')

# Reverse the string using slicing
rev_str = my_str[::-1]

# Compare the original string with its reversed version
if my_str == rev_str:
    print("It is palindrome")  # If they are equal, it is a palindrome
else:
    print("It is not palindrome")  # If they are not equal, it is not a palindrome
