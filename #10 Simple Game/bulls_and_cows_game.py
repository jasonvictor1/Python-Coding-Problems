
import random  # Import the random module to generate random numbers

# Generate a secret number between 10 and 99 and convert it to a string
secret_number = str(random.randint(10, 99))
print("Guess the number. It contains 2 digits.")

# Set the initial number of tries
remaining_try = 7

# Start a loop that continues until all tries are used
while remaining_try > 0:
    player_guess = input("Enter your guess: ")  # Prompt the player for a guess
    
    # Check if the player's guess matches the secret number
    if player_guess == secret_number:
        print("Yay, you guessed it!")
        print("YOU WIN.")
        break  # Exit the loop if the player guesses correctly
    else:
        # Initialize bulls and cows counters
        bulls = 0
        cows = 0
        
        # Check for bulls (correct digit in the correct place)
        if player_guess[0] == secret_number[0]:
            bulls += 1
        if player_guess[1] == secret_number[1]:
            bulls += 1
        
        # Check for cows (correct digit but in the wrong place)
        if player_guess[0] == secret_number[1]:
            cows += 1
        if player_guess[1] == secret_number[0]:
            cows += 1

        # Print the bulls and cows count after each guess
        print("Bulls: ", bulls)
        print("Cows: ", cows)

        # Decrement the number of remaining tries
        remaining_try -= 1

        # Check if there are no more tries left and declare the game lost
        if remaining_try < 1:
            print("You lost the game.")
            break
