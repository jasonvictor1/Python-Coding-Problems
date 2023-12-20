# Define a function to count the number of vowels in a given sentence
def count_vowels(sentence):

    # Initialize the count variable to zero
    count = 0

    # Define a list of vowels (both lower and upper case)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # Iterate through each character in the given sentence
    for char in sentence:

        # Check if the character is in the list of vowels
        if char in vowels:

            # If it's a vowel, increment the count by 1
            count += 1

    # Return the final count of vowels
    return count


# Test the function with a sample string "Hello World"
print(count_vowels("Hello World"))
