
# Define a function named 'dec_to_binary' that converts a decimal number to its binary representation
def dec_to_binary(n):
    bits = []  # Initialize an empty list to store the binary digits

    # Keep dividing the number by 2 and store the remainder (0 or 1) until the number is greater than 0
    while n > 0:
        bits.append(n % 2)  # Append the remainder to the list
        n //= 2  # Floor division to get the quotient for the next iteration

    bits.reverse()  # Reverse the list to get the correct binary representation

    binary = ''  # Initialize an empty string for the binary number
    for bit in bits:
        binary += str(bit)  # Convert each bit to a string and concatenate

    return binary  # Return the binary representation

# Prompt the user to enter a decimal number and convert it to an integer
num = int(input("Your decimal number: "))

# Call the 'dec_to_binary' function with the user input and store the result in 'binary'
binary = dec_to_binary(num)

# Print the binary representation of the entered decimal number
print("Your binary is:", binary)
