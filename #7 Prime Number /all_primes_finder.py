
# Define a function to check if a given number is prime
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:  # If num is divisible by any number between 2 and num - 1, it is not prime
            return False
    return True  # If num is not divisible by any number between 2 and num - 1, it is prime

# Define a function to find all prime numbers up to a given number
def all_primes(num):
    primes = []  # Initialize an empty list to store prime numbers
    for n in range(2, num + 1):  # Iterate from 2 to num
        if is_prime(n) is True:  # Check if the current number is prime
            primes.append(n)  # Add the prime number to the list
    return primes  # Return the list of prime numbers

# Prompt the user to enter an upper limit
num = int(input("Enter upper limit: "))

# Call the all_primes function and store the result
primes = all_primes(num)

# Print the list of prime numbers up to the given limit
print(primes)
