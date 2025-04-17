import random

print("=== Mystery Number Challenge ===")

# Generate a hidden number between 1 and 15
secret_number = random.randint(1, 15)
attempts = 0

print("Can you crack the code? Try to guess the mystery number between 1 and 15.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"🎉 Spot on! You found the number in {attempts} attempt(s).")
            break
    except ValueError:
        print("Please enter a valid number.")
