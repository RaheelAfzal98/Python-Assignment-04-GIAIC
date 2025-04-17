import random

min_range = 1
max_range = 15

print("🤖 Hello! I'm a mind reader in training. Think of a number between 1 and 15.")
print("I'll try to guess it based on your clues. Let's begin!")

while True:
    bot_guess = random.randint(min_range, max_range)
    print(f"\nIs it... {bot_guess}?")

    response = input("Type 'c' for correct, '>' if your number is higher, '<' if it's lower: ").strip().lower()

    if response == 'c':
        print(f"Awesome! 🎉 I nailed it — your number was {bot_guess}.")
        break
    elif response == '>':
        min_range = bot_guess + 1
        print("Alright, aiming higher next time! 🔼")
    elif response == '<':
        max_range = bot_guess - 1
        print("Gotcha! Going lower next time! 🔽")
    else:
        print("⚠️ Invalid input! Please enter 'c', '>' or '<'.")
