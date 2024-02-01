
# Define a function named 'dec_to_binary' to convert a decimal number to its binary representation
# This function uses recursion
def dec_to_binary(n):
    if n > 1:
        dec_to_binary(n // 2)  # Recursively call the function with the floor division of 'n' by 2
    print(n % 2, end='')  # Print the remainder when 'n' is divided by 2, without newline, to get the binary digit

# Prompt the user to enter a decimal number and convert it to an integer
num = int(input("Your decimal number: "))

# Call the 'dec_to_binary' function with the user input
dec_to_binary(num)

# Print a newline character after the binary representation
print(" ")
