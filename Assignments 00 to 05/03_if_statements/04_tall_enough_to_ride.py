# Problem Statement
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.
# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like
# Here's two sample runs (user input is in bold italics):
# How tall are you? 100
# You're tall enough to ride!
# How tall are you? 10
# You're not tall enough to ride, but maybe next year!
# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)

MIN_REQUIRED_HEIGHT: int = 50  # Minimum height to be tall enough to ride

def main():
    # Prompt the user to enter their height
    user_height = float(input("Please enter your height: "))

    # Compare the user's height with the minimum required height
    if user_height >= MIN_REQUIRED_HEIGHT:
        print("You're tall enough to go on the ride!")
    else:
        print("You're not tall enough, but maybe next time!")

# Code to run the program
if __name__ == '__main__':
    main()
