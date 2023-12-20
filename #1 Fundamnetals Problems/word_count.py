# Input text string
text = 'Love to watch movie'

# Initialize a variable to keep track of word count
count = 0

# Loop through each character in the text
for char in text:
    # Check if the character is a space
    if char == ' ':
        # If it's a space, increase the count by 1
        count += 1

# Add 1 to the count to account for the last word in the text (since words = spaces + 1)
count += 1

# Print the final word count
print(count)
