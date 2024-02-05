
import random  # Import the random module for generating random numbers

print('To stop anytime, enter: q')  # Instruction for the user to quit the game

score = 0  # Initialize the score to 0

# Start an infinite loop to keep the guessing game running
while True:
    num = random.randint(0, 10)  # Generate a random number between 0 and 10
    guess = input("Guess a number between 0 to 10: ")  # Prompt the user for a guess
    
    # Check if the user wants to quit the game
    if guess == 'q':
        print('Game Over.')
        break  # Exit the loop to end the game
    
    guess_num = int(guess)  # Convert the guess to an integer
    
    # Check if the guess is equal to the generated number
    if guess_num == num:
        print('CONGRATS, you guessed it correctly')
        score += 10  # Increase the score by 10
        print('Your new score:', score)  # Print the new score
    else:
        print('Your guess did not match')
        print('The number was:', num)  # Reveal the correct number
