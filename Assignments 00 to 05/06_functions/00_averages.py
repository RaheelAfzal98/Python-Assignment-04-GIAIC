# Problem Statement
# Write a function that takes two numbers and finds the average between the two.


def find_average(num1, num2):
    """
    Takes two numbers and returns their average.
    """
    return (num1 + num2) / 2

def main():
    # Ask user for two numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Calculate and print the average
    average = find_average(number1, number2)
    print("The average of", number1, "and", number2, "is:", average)

if __name__ == '__main__':
    main()
