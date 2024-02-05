
# Define a function to check if a given number is prime
def is_prime(num):
    # Iterate from 2 to num - 1
    for i in range(2, num):
        if (num % i) == 0:  # If num is divisible by any number between 2 and num - 1, it is not prime
            return False
    return True  # If num is not divisible by any number between 2 and num - 1, it is prime

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Call the is_prime function and store the result
check_prime = is_prime(num)

# Output based on the result from the is_prime function
if check_prime:
    print('Your number is a Prime')
else:
    print('Your number is not a Prime')
