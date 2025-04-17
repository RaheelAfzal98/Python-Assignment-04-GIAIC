# Problem Statement
# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48


import random

def main():
    # Random number between 0 and 99
    number_to_guess = random.randint(0, 99)

    # Ask the user for their first guess
    guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

    # Keep asking until the correct number is guessed
    while guess != number_to_guess:
        if guess > number_to_guess:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        guess = int(input("Enter a new number: "))

    # If guess is correct
    print(f"Congrats! The number was: {number_to_guess}")

if __name__ == "__main__":
    main()


