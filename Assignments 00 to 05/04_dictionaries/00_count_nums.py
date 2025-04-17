# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.
# An example run of the program looks like this (user input is in blue):
# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


def collect_user_input():
    """
    Prompt the user to enter numbers one by one.
    Store each number in a list until the user enters 'done' (case-insensitive).
    Return the list of entered numbers.
    """
    numbers = []
    while True:
        user_input = input("Please enter a number (or 'done' to finish): ").strip().lower()
        
        if user_input == 'done':  # Stop the loop when user types 'done'
            break
        
        try:
            num = int(user_input)  # Convert the input to an integer
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")
    
    return numbers

def count_occurrences(numbers_list):
    """
    Count how many times each number appears in the list.
    Return a dictionary with the numbers as keys and their counts as values.
    """
    counts = {}
    for num in numbers_list:
        counts[num] = counts.get(num, 0) + 1
    
    return counts

def display_results(counts_dict):
    """
    Print out each number and its frequency.
    """
    for number, count in counts_dict.items():
        print(f"{number} appears {count} time{'s' if count > 1 else ''}.")

def main():
    """
    Main function to run the program.
    Collect user input, count the occurrences, and display the results.
    """
    numbers = collect_user_input()  # Collect numbers from the user
    occurrences = count_occurrences(numbers)  # Count occurrences of each number
    display_results(occurrences)  # Display the results

# Program execution starts here
if __name__ == '__main__':
    main()
