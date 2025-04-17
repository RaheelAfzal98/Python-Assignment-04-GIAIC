# Problem Statement
# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


def main():
    user_list = []  # Create an empty list to store user inputs
    
    while True:
        # Prompt the user to enter a value
        value = input("Enter a value: ")
        
        # If the user presses enter without typing anything, break the loop
        if value == "":
            break
        
        # Add the entered value to the list
        user_list.append(value)
    
    # Print the final list
    print("Here's the list:", user_list)


if __name__ == "__main__":
    main()
