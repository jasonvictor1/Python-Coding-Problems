
def get_bulls_cows(number, user_guess):
    bulls_cows = [0, 0]  # Initialize bulls_cows list: [bulls, cows]
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            bulls_cows[0] += 1  # Increment bulls if digit is in the correct place
        elif user_guess[i] in number:
            bulls_cows[1] += 1  # Increment cows if digit is correct but in the wrong place
    return bulls_cows

# Assuming 'remaining_try' and 'secret_number' are defined earlier in the code
while remaining_try > 0:
    player_guess = input("Enter your guess: ")
    
    if player_guess == secret_number:
        print("Yay, you guessed it!")
        print("YOU WIN.")
        break
    else:
        bulls_cows = get_bulls_cows(secret_number, player_guess)  # Get bulls and cows count
        
        print("Bulls: ", bulls_cows[0])
        print("Cows: ", bulls_cows[1])

        remaining_try -= 1  # Decrement the number of tries left

        if remaining_try < 1:
            print("You lost the game.")
            break
