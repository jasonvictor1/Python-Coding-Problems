
# Define a function to calculate compound interest
def compound_interest(principle, rate, time):
    # Calculate the compound interest using the formula: A = P(1 + r/n)^(nt)
    # For simplicity, n (number of times interest applied per time period) is assumed to be 1
    interest = principle * ((1 + rate / 100) ** time)
    return interest

# Prompt the user to enter the principal amount borrowed
principle = int(input("Money you borrowed: "))

# Prompt the user to enter the interest rate
interest_rate = float(input("Interest Rate: "))

# Prompt the user to enter the time duration for the investment or loan
time = float(input("Overall Duration: "))

# Calculate the total amount due after applying compound interest
total_due = compound_interest(principle, interest_rate, time)

# Print the total interest amount due
print("Interest Amount is:", total_due)
