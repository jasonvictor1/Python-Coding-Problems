
# Define a function to convert a binary number to its decimal equivalent
def binary_to_decimal(binary):
    decimal = 0  # Initialize a variable to store the decimal equivalent
    i = 0  # Counter for the position of each binary digit

    # Loop through each digit of the binary number
    while(binary != 0):
        last_digit = binary % 10  # Get the last digit of the binary number
        curr_decimal = last_digit * pow(2, i)  # Convert the current binary digit to its decimal value
        decimal = decimal + curr_decimal  # Add the current decimal value to the total
        binary = binary // 10  # Remove the processed digit from the binary number
        i += 1  # Move to the next digit position

    return decimal  # Return the computed decimal value

# Prompt the user to enter a binary number and convert it to an integer
num = int(input('Enter binary number: '))

# Call the function to convert the entered binary number to decimal
decimal = binary_to_decimal(num)

# Print the decimal equivalent of the binary number
print('Your decimal equivalent is: ', decimal)
