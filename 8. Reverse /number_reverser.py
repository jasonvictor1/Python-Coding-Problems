
# Define a function to reverse a given number
def reverse_num(num):
    reverse = 0  # Initialize 'reverse' to 0 to store the reversed number
    while(num > 0):  # Loop until 'num' is greater than 0
        last_digit = num % 10  # Extract the last digit of 'num'
        reverse = reverse * 10 + last_digit  # Append 'last_digit' to 'reverse'
        num = num // 10  # Remove the last digit from 'num'
    return reverse  # Return the reversed number

# Prompt the user to enter a number
n = int(input("Enter number: "))

# Call the reverse_num function and store its return value in 'reverse'
reverse = reverse_num(n)

# Print the reversed number
print("Reverse of the number:", reverse)
