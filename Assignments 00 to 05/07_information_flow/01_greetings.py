# Problem Statement
# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.
# Here's a sample run of the program (user input in bold italics):
# What's your name? Sophia
# Greetings Sophia!

def greet(person_name):
    """
    Prints a warm greeting using the provided name.
    """
    print("Hello there, " + person_name + "! Welcome!")

def main():
    name_input = input("What's your name? ")  # Ask user for their name
    greet(name_input)  # Call greet with the entered name

if __name__ == '__main__':
    main()
