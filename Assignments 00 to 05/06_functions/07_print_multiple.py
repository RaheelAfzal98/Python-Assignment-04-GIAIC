# Problem Statement
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.
# Here's a sample run of the program (user input is in blue):
# Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!



def print_multiple(message, repeats):
    """
    Prints the given message the specified number of times.
    """
    for _ in range(repeats):  # Loop to repeat the message the specified number of times
        print(message)


def main():
    message = input("Please type a message: ")  # Get the message from the user
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get the number of repeats
    print_multiple(message, repeats)  # Call the function to print the message


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
