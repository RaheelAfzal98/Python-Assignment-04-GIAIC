# Problem Statement
# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.
# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:
# Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'
# If the user enters anything else we print out:
# Sorry I only tell jokes
# You should use the three constants:
# PROMPT JOKE SORRY
# which contain the strings for the prompt asked to the user, the joke to print out if the user enters Joke and the sorry message if the user enters anything else.
# Your program will need to use an if statement which checks if the user input is Joke:
# if user_input == "Joke":
# Recall that == is a comparison which tests if two values are equal to one another.
# Here is a full run of the program (user input is in blue):
# What do you want? Joke Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'



# Define constants
PROMPT = "What do you want? "
JOKE = ("Here is a joke for you! Why do programmers prefer dark mode? "
        "Because light attracts bugs.")
SORRY = "Sorry I only tell jokes"

# Define the main function
def main():
    user_input = input(PROMPT)
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

# Entry point
if __name__ == "__main__":
    main()
