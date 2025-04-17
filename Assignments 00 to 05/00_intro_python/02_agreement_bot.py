# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
# What's your favorite animal? cow
# My favorite animal is also cow!



def main():
    # Print a friendly message
    print("Hey there! Let's talk about animals")

    # Ask the user for their favorite animal and remove extra spaces
    animal = input("So, What's your favorite animal? ").strip()

    # Print the response using the user's input
    print(f"\nMy favorite animal is also {animal}!")


# Run the main function
if __name__ == "__main__":
    main()
