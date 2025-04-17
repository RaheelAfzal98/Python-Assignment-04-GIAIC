# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.
# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.



def main(): 

    first_input = input("Please enter the first number: ") # Prompt the user to enter the first number.

    first_number = int(first_input) # Read the input and convert it to an integer.

    second_input = input("Please enter the second number: ") # Prompt the user to enter the second number.

    second_number = int(second_input) # Read the input and convert it to an integer.

    total_number = first_number + second_number # Calculate the sum of the two numbers.

    print(f"The Sum of first number {first_number} and second number {second_number} the total is {total_number}") # Print the total sum with an appropriate message.


if __name__ == "__main__": # This is the entry point of the program.
    main()