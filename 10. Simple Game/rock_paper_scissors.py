
# Define a function to determine the winner of a rock-paper-scissors game
def get_winner(p1, p2):
    # Check if both players chose the same item
    if p1 == p2:
        return "It's a tie!"
    # Conditions for Player 1 choosing 'rock'
    elif p1 == 'rock':
        if p2 == 'scissors':
            return "First player wins!"
        else:
            return "Second Player wins!"
    # Conditions for Player 1 choosing 'scissors'
    elif p1 == 'scissors':
        if p2 == 'paper':
            return "First player win!"
        else:
            return "Second player wins!"
    # Conditions for Player 1 choosing 'paper'
    elif p1 == 'paper':
        if p2 == 'rock':
            return "First player wins!"
        else:
            return "Second player win!"
    # Handle invalid inputs
    else:
        return "Invalid input!"

# Prompt the first player to choose rock, paper, or scissors
player1 = input("First player: rock, paper or scissors: ")

# Prompt the second player to choose rock, paper, or scissors
player2 = input("Second Player: rock, paper or scissors: ")

# Print the result of the game
print(get_winner(player1, player2))
