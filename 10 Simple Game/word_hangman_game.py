
import random  # Import the random module for generating random numbers

def selected_a_word():
    # Define a list of words from which to randomly select one
    words = ['working', 'hard', 'makes', 'things', 'easier', 'congrats', 'programming', 'hero']
    word = words[random.randint(0, len(words)-1)]  # Randomly select a word from the list
    return word

def get_blank_word(word):
    # Create a string that starts with the first letter of 'word' and '_' for the rest
    blank_word = word[0]
    for i in range(1, len(word)):
        blank_word += '_'
    return blank_word

def word_hangman(word, so_far, letter, try_left):
    bad_try = True  # Flag to check if the guessed letter is in the word
    # Check each character in the word
    for i in range(len(word)):
        if word[i] == letter:
            so_far = so_far[:i] + letter + so_far[i+1:]  # Update 'so_far' with the correctly guessed letter
            bad_try = False
    # If the guess was incorrect, decrement 'try_left' and print the number of tries left
    if bad_try:
        try_left -= 1
        print('Wrong Try Left: ', try_left)
    # Print the current state of 'so_far'
    print('so far you got: ', so_far)
    # Check for win or loss conditions
    if word == so_far:
        print('YAY!!! You Win')
    elif try_left == 0:
        print('Opps!!! You Lost')
    else:
        # Prompt for the next letter if the game is not over
        next_letter = input('Enter your next letter: ')
        word_hangman(word, so_far, next_letter, try_left)

# Start the game
word = selected_a_word()  # Select a word to guess
clue_word = get_blank_word(word)  # Get a blank word for the initial clue
word_hangman(word, clue_word, word[0], 5)  # Begin the hangman game
