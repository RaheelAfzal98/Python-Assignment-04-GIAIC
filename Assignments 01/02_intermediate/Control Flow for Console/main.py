import random

# Constants
NUM_ROUNDS = 5

def main():
    # Initialize player's score
    score = 0

    # Start the game
    print("Welcome to the High-Low Game!")
    print("=" * 80)

    # Loop for NUM_ROUNDS
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate random numbers for both the player and the computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {player_number}")

        # Ask the player for their guess
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # If the player presses Enter without typing anything, stop the game
        if guess == "":
            print("You decided to quit the game. Thanks for playing!")
            break

        # Check if the guess is valid
        while guess not in ['higher', 'lower']:
            print("Invalid input. Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

            # If the player presses Enter without typing anything, stop the game
            if guess == "":
                print("You chose to quit the game. Thanks for playing!")
                break

        # If the player decided to quit, break out of the loop
        if guess == "":
            break

        # Determine the result
        if (guess == 'higher' and player_number > computer_number) or (guess == 'lower' and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Oops! The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")

    # End of the game
    if guess != "":
        print("Game over! Thanks for playing!")

    # Final evaluation based on score
    if score == NUM_ROUNDS:
        print("Incredible! You got a perfect score!")
    elif score >= NUM_ROUNDS // 2:
        print("Well done, you did great!")
    else:
        print("Better luck next time. Keep practicing!")

if __name__ == "__main__":
    main()
