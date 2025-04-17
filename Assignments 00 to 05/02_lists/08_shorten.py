# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.


MAX_LENGTH = 3  # Set the maximum length for the list

def shorten(lst):
    """
    Removes elements from the end of the list until it is MAX_LENGTH items long.
    Prints each item that is removed.
    """
    # Keep removing elements until the list length is equal to MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item from the list
        print(f"Removed: {removed_item}")
    
    # After the loop, the list should be at MAX_LENGTH or smaller
    print(f"List after shortening: {lst}")


def main():
    # Example list to test the shorten function
    example_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    print("Original list:", example_list)
    
    # Call shorten function to modify the list
    shorten(example_list)


if __name__ == "__main__":
    main()
