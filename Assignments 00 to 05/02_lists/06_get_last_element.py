# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.



def get_last_element(lst):
    """
    Prints the last element in the list.
    Assumes the list is non-empty.
    """
    print(f"The last element is: {lst[-1]}")


def main():
    # Prompt the user for the number of elements they want to input
    n = int(input("How many elements would you like to enter? "))

    # Create an empty list to store user input
    user_list = []

    # Collect elements from the user and append to the list
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    # Call the function to print the last element
    get_last_element(user_list)


if __name__ == "__main__":
    main()
