import random

def determine_winner(player_choice, ai_choice):
    wins = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    return wins[player_choice] == ai_choice

def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    print("=== Rock vs Paper vs Scissors ===")
    print("Make your move! (type: rock / paper / scissors)")

    player = input("Your move: ").strip().lower()
    
    while player not in options:
        player = input("Oops! Invalid move. Please choose rock, paper, or scissors: ").strip().lower()
    
    computer = random.choice(options)
    print(f"The computer throws: {computer}")

    if player == computer:
        return "It's a draw! 🤝"
    elif determine_winner(player, computer):
        return "You win! 🎉"
    else:
        return "You lose! 😢"

# Play the game
result = rock_paper_scissors()
print(result)
