
# Prompt the user to enter the mass of the first object in kilograms
mass1 = float(input("First mass: "))

# Prompt the user to enter the mass of the second object in kilograms
mass2 = float(input("Second mass: "))

# Prompt the user to enter the distance between the two objects in meters
r = float(input("Distance between the objects: "))

# Define the gravitational constant, G, in N(m^2)/(kg^2)
G = 6.673 * (10 ** -11)

# Calculate the gravitational force between the objects using Newton's law of universal gravitation
force = (G * mass1 * mass2) / (r ** 2)

# Print the gravitational force, rounded to five decimal places, in newtons
print("The gravitational force is:", round(force, 5), "N")
