# Problem Statement
# Print 10 random numbers in the range 1 to 100.
# Here is an example run:
# 45 79 61 47 52 10 16 83 19 12
# Each time you run your program you should get different numbers
# 81 76 70 1 27 63 96 100 32 92
# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:
# value = random.randint(1, 6)


import random  # Import the random module to generate random numbers

def main():
    # Loop 10 times to generate 10 random numbers
    for _ in range(10):
        # Generate a random number between 1 and 100 (inclusive)
        value = random.randint(1, 100)
        # Print the number with a space, without starting a new line
        print(value, end=" ")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
