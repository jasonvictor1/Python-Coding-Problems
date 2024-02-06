
# Define a function to get the prime factors of a given number
def get_prime_factors(n):
    factors = []  # Initialize an empty list to store the prime factors
    divisor = 2  # Start with the smallest prime number

    # Keep dividing 'n' by the divisor until 'n' becomes less than 2
    while n > 2:
        if n % divisor == 0:  # If 'n' is divisible by the divisor, it is a prime factor
            factors.append(divisor)  # Add the divisor to the list of factors
            n = n // divisor  # Update 'n' to be 'n' divided by the divisor using integer division
        else:
            divisor = divisor + 1  # If not divisible, increment the divisor

    return factors  # Return the list of prime factors

# Prompt the user to enter a number
num = int(input("Enter your number: "))

# Call the get_prime_factors function and store the result in 'factors'
factors = get_prime_factors(num)

# Print the list of prime factors of the given number
print(factors)
