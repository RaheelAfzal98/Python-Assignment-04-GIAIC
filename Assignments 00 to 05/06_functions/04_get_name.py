# Problem Statement
# Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.
# Here's a sample run of the program where the name we've decided to return is Sophia (the autograder expects the returned name to be Sophia):
# Howdy Sophia ! 🤠


def get_name():
    """
    Returns the name as a string.
    """
    return "Sophia"  # Return the name as instructed

def main():
    name = get_name()  # Call get_name() function to retrieve the name
    print("Howdy " + name + " ! 🤠")  # Print the greeting with the retrieved name

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
