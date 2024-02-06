# Define a function to calculate the sum of digits of a given number
def get_sum_of_digits(num):
    # Initialize a variable 'sum' to store the total sum of digits
    sum = 0
    # Use a while loop to iterate as long as the number is greater than 0
    while (num > 0):
        # Extract the last digit of 'num' using modulo 10
        last_digit = num % 10
        # Add the last digit to the 'sum'
        sum = sum + last_digit
        # Remove the last digit from 'num' by integer division by 10
        num = num // 10
    # Return the calculated sum of digits
    return sum


# Ask the user to input a number and convert it to an integer
user_num = int(input("Enter a number: "))
# Call the get_sum_of_digits function with the user input and store the result in 'total'
total = get_sum_of_digits(user_num)
# Print the total sum of digits
print("The total sum of digits is: ", total)
