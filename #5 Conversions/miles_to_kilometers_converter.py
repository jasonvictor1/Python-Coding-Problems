
# Prompt the user to enter a distance in miles and convert it to a floating-point number
miles = float(input("Enter distance in miles: "))

# Convert the distance from miles to kilometers
# The conversion factor is 1 mile = 1.609344 kilometers
kilometers = miles * 1.609344

# Print the converted distance in kilometers
print("Distance in Kilometers:", kilometers)
