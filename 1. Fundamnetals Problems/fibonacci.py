# Define a function to compute the Fibonacci sequence up to a given number
def fibonacci(num):
    # Initialize a list with the first two numbers of the Fibonacci sequence
    fibo = [0, 1]

    # Set the initial index for iteration (since the first two numbers are already defined)
    i = 2

    # Continue until the sequence has reached the desired number of terms
    while i <= num:
        # Calculate the next Fibonacci number by adding the last two numbers in the list
        next_fibo = fibo[i-1] + fibo[i-2]

        # Append the calculated Fibonacci number to the list
        fibo.append(next_fibo)

        # Increment the index for the next iteration
        i += 1

    # Return the generated Fibonacci sequence
    return fibo


# Call the fibonacci function with the argument 9 and print the result
print(fibonacci(9))
