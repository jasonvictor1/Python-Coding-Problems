# Define a function to print the multiplication table for a given number up to 10.
def multiplication_table(n):
    # Initialize a counter 'i' to 1.
    i = 1
    # Continue the loop until 'i' is less than or equal to 10.
    while i <= 10:
        # Print the multiplication of 'i' and 'n'.
        print(i, 'X', n, '=', i*n)
        # Increment the counter 'i' by 1.
        i += 1


# Call the 'multiplication_table' function with 5 as an argument to print the multiplication table for 5.
multiplication_table(5)
