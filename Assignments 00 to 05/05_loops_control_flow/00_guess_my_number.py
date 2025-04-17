# Problem Statement
# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

import random

def start_game():
    number_to_guess = random.randint(1, 99)
    print("Guess the number I'm thinking of—it’s somewhere between 1 and 99!")

    while True:
        try:
            player_input = int(input("Your guess: "))
        except ValueError:
            print("That's not a valid number. Try again.")
            continue

        if player_input == number_to_guess:
            print(f"Nice job! You found it. The number was {number_to_guess}.")
            break
        elif player_input > number_to_guess:
            print("Too high! Give it another shot.")
        else:
            print("Too low! Try a bit higher.")

if __name__ == '__main__':
    start_game()
