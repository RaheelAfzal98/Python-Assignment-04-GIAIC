# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.


import random  # For generating random numbers

DIES_NUM_SIDES: int = 6

def main():
    # Simulate rolling two dice
    die1: int = random.randint(1, DIES_NUM_SIDES)
    die2: int = random.randint(1, DIES_NUM_SIDES)

    # Calculate the total
    total: int = die1 + die2

    # Display the results
    print("Dice have", DIES_NUM_SIDES, "sides each.")
    print(f"First die roll: {die1}")
    print(f"Second die roll: {die2}")
    print(f"Total of both rolls: {total}")

# Run the program
if __name__ == '__main__':
    main()
