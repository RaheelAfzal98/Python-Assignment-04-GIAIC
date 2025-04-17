# Problem Statement
# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!
# Here's a sample run (user input is in blue):
# Enter a number: 42 The ones digit is 2



def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    """
    ones_digit = num % 10  # Use modulo to find the ones digit
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Get user input
    print_ones_digit(num)  # Call the function to print the ones digit

if __name__ == '__main__':
    main()
