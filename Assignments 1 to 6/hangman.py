import random

# Word list with simple clues
word_bank = {
    "elephant": "A large animal with a trunk.",
    "python": "A popular programming language and a snake.",
    "guitar": "A musical instrument with strings.",
    "pizza": "A popular Italian dish with cheese.",
    "planet": "Earth is one of these.",
}

def mask_word(word, correct):
    return " ".join([ch if ch in correct else "_" for ch in word])

def word_guess_game():
    word, clue = random.choice(list(word_bank.items()))
    correct_guesses = set()
    wrong_guesses = set()
    max_wrong = 5

    print("== Word Guess Challenge ==")
    print("Clue:", clue)

    while len(wrong_guesses) < max_wrong:
        print("\nWord:", mask_word(word, correct_guesses))
        print(f"Wrong attempts left: {max_wrong - len(wrong_guesses)}")
        print(f"Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in correct_guesses or guess in wrong_guesses:
            print("You've already tried that letter.")
            continue

        if guess in word:
            correct_guesses.add(guess)
            print(f"Nice! '{guess}' is correct.")
        else:
            wrong_guesses.add(guess)
            print(f"Sorry, '{guess}' is not in the word.")

        if all(char in correct_guesses for char in word):
            print("\n🎉 You guessed the word:", word)
            break
    else:
        print("\n💀 Out of attempts! The word was:", word)

word_guess_game()
