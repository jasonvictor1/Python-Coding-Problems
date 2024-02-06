
# Define a function to reverse the words in a given sentence
def reverse_words(sentence):
    words = sentence.split()  # Split the sentence into a list of words
    words.reverse()  # Reverse the order of words in the list
    return " ".join(words)  # Join the reversed list of words back into a sentence

# Prompt the user to enter a sentence
usr_input = input("Enter a sentence: ")

# Call the reverse_words function and store its return value in 'reverse'
reverse = reverse_words(usr_input)

# Print the sentence with its words reversed
print('Reversed words are: ', reverse)
