# Prompt the user to input a year
year = input('year you want to check: ')

# Convert the input string to an integer
year_num = int(year)

# Check if the year is divisible by 4 to determine if it's a leap year
if year_num % 4 == 0:
    print(year_num, 'is a leap year')
else:
    print(year_num, 'is not a leap year')
