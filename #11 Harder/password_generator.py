
import string  # Import the string module for predefined character classes
import random  # Import the random module for generating random selections

def generate_password(size):
    # Combine ASCII letters, digits, and punctuation characters to form the pool of possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''  # Initialize an empty string for the password
    # Loop for the number of times equal to the desired password length
    for char in range(size):
        rand_char = random.choice(all_chars)  # Randomly select a character from the pool
        password = password + rand_char  # Append the random character to the password string
    return password  # Return the generated password

# Prompt the user to input the desired password length
pass_len = int(input('How many characters in your password?'))
# Call the generate_password function with the user-specified length
new_password = generate_password(pass_len)
# Print the newly generated password
print('Your new password: ', new_password)
