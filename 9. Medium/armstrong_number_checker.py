
# Define a function to check if a number is an Armstrong number
def check_armstrong(num):
    order = len(str(num))  # Calculate the number of digits in 'num'
    
    sum = 0  # Initialize sum to 0
    
    # Use 'temp' to find each digit. Then power it by 'order' and add to 'sum'
    temp = num
    while temp > 0:
        digit = temp % 10  # Get the last digit
        sum += digit ** order  # Add the digit raised to the power of 'order' to 'sum'
        temp //= 10  # Remove the last digit from 'temp'
    
    # Check if the sum of the digits raised to the power of 'order' equals the number
    return num == sum

# Prompt the user to enter a number
num = int(input('Enter your number: '))

# Call the check_armstrong function to determine if the entered number is an Armstrong number
if check_armstrong(num):
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
