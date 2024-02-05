
# Prompt the user to enter the principal amount borrowed
principle = int(input("Money you borrowed: "))

# Prompt the user to enter the interest rate
interest_rate = float(input("Interest Rate: "))

# Prompt the user to enter the time duration for the loan
time = float(input("Overall Duration: "))

# Calculate simple interest using the formula: Simple Interest = Principal * Rate * Time
simple_interest = principle * (interest_rate / 100) * time

# Print the calculated simple interest
print("Simple interest is:", simple_interest)
