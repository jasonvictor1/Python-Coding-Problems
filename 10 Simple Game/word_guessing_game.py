
import random  # Import the random module to generate random numbers

def get_a_clue():
    # Define a list of word clues with missing letters represented by '-'
    clues = ['-a-e', 'y-ll-w', 's-mm-r', 'wi-t-r','s-n-y', 'l-v-','-i-e']
    # Randomly select a position from the list
    position = random.randint(0, len(clues)-1)
    # Get the clue at the selected position
    clue = clues[position]
    return clue

def check_word_match(clue, guess):
    # Check if the length of the guess matches the clue
    if len(clue) != len(guess):
        return False
    # Check each character to see if it matches or is correctly guessed
    for i in range(len(clue)):
        # If the clue character is not '-' and does not match the guess, return False
        if clue[i] != '-' and clue[i] != guess[i]:
            return False
    # If all checks pass, return True
    return True

# Start the game
word_clue = get_a_clue()
print('Your word clue:', word_clue)
answer = input('What would be the word: ')

# Check if the guessed word matches the clue
is_matched = check_word_match(word_clue, answer)

# Print the result based on whether the guess was correct or not
if is_matched is True:
    print('WOW!!! You win')
else:
    print('Opps! you missed it.')
