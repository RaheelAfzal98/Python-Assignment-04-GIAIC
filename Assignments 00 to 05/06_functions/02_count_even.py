# Problem Statement
# Fill out the function count_even(lst) which
# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),
# and then prints the number of even numbers in the list.
# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def count_odd(lst):
    """
    Returns the number of odd numbers in the list.
    >>> count_odd([1, 2, 3, 4])
    2
    >>> count_odd([2, 4, 6, 8])
    0
    """
    count = 0  # Stores the count of odd numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 != 0:  # If the current number in the list is odd
            count += 1  # Add one to our count!

    print(count)  # Print out how many odd numbers we counted above

def get_numbers():
    """
    Reads in numbers from the user until they press enter and returns the resulting list.
    """
    numbers = []  # Make an empty list to store numbers
    user_input = input("Enter a number or press enter to stop: ")  # Get user input for a number
    while user_input != "":  # While the user doesn't enter nothing...
        numbers.append(int(user_input))  # Cast the user input into an integer and add it to the list
        user_input = input("Enter a number or press enter to stop: ")  # Get the next user input

    return numbers

def main():
    numbers = get_numbers()
    count_odd(numbers)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
