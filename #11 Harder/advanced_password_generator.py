
import string  # Import the string module to access predefined character sequences
import random  # Import the random module for generating random choices

# Print available character sequences from the string module
print('All letters')
print(string.ascii_letters)  # Print all ASCII letters (both lowercase and uppercase)
print('All lowercase characters')
print(string.ascii_lowercase)  # Print all ASCII lowercase characters
print('All uppercase characters')
print(string.ascii_uppercase)  # Print all ASCII uppercase characters

def randomPassword(size):
    # Combine ASCII letters, digits, and punctuation characters for the password character pool
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    # Ensure the password contains at least one lowercase letter, one uppercase letter, one digit, and one punctuation mark
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    
    # Fill the rest of the password length with random characters from the combined pool
    for i in range(size-4):
        password += random.choice(all_chars)
    return password  # Return the generated password

# Prompt the user for the desired password length
pass_len = int(input("What would be the password length? "))
# Generate and print three random passwords
print("First Random Password is:", randomPassword(pass_len))
print("Second Random Password is:", randomPassword(pass_len))
print("Third Random Password is:", randomPassword(pass_len))
