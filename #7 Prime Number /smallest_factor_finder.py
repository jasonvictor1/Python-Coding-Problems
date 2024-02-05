
# Define a function to find the smallest factor of a given number
def get_smallest_factor(num):
    factor = 2  # Start checking from 2, the smallest prime number
    while num % factor != 0:  # Loop until the factor divides the number evenly
        factor += 1  # Increment the factor by 1
    return factor  # Return the smallest factor

# Prompt the user to enter a number
num = int(input('Enter your number: '))

# Call the get_smallest_factor function to find the smallest factor of the entered number
smallest_factor = get_smallest_factor(num)

# Print the smallest factor
print('The smallest prime factor is: ', smallest_factor)
