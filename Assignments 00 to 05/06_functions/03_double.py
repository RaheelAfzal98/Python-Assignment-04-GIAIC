# Problem Statement
# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.
# Here's a sample run of the program (user input in bold italics):
# Enter a number: 2 Double that is 4


def double(num):
    """
    Takes a number and returns the result of multiplying it by 2.
    """
    return num * 2

def main():
    num = int(input("Enter a number: "))  # Ask user for a number
    result = double(num)  # Call double() function to double the number
    print("Double that is " + str(result))  # Print the result

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
