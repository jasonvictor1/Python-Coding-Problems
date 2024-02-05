
# Define a function to calculate the sum of cubes of all numbers up to a given number
def cube_sum(num):
    sum = 0  # Initialize sum to 0
    for n in range(num + 1):  # Iterate over numbers from 0 to num
        sum = sum + n ** 3  # Add the cube of the current number to sum
    return sum  # Return the total sum of cubes

# Prompt the user to enter a number
user_num = int(input('Enter a number: '))

# Call the cube_sum function with the user's input and store the result in 'result'
result = cube_sum(user_num)

# Print the result, the sum of cubes of numbers up to the entered number
print('Your sum of cubes are: ', result)
