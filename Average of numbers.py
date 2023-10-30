# Prompt the user to enter the number of numbers they want to input
num_input = int(input("How many numbers do you want to enter?: "))

# Initialize a variable to store the total sum of the numbers
total = 0

# Loop through the range of the number of inputs the user specified
for i in range(0, num_input):
    # Prompt the user to enter a number for each iteration
    elem = int(input("Enter element: "))
    # Add the entered number to the total sum
    total += elem

# Calculate the average of the entered numbers
avg = total/num_input

# Print the average, rounded to 2 decimal places
print("Average of elements you have entered: ", round(avg, 2))
