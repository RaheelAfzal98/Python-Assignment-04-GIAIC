# Problem Statement
# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!
# Here's a sample run (user input is in blue):
# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12


def print_divisors(num):
    """
    Prints all divisors of the number num.
    """
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):  # Check divisibility from 1 to num
        if num % i == 0:  # If there's no remainder, i is a divisor
            print(i, end=' ')  # Print the divisor followed by a space
    print()  # Print a newline after the divisors


def main():
    num = int(input("Enter a number: "))  # Prompt user for input
    print_divisors(num)  # Call the function to print divisors of the number


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
