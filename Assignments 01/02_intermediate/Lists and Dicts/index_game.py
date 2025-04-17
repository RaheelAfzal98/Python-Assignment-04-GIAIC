def access_element(lst, index):
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return f"Updated list after modification: {lst}"
    except IndexError:
        return "Index out of range. Cannot modify."

def slice_list(lst, start, end):
    try:
        return f"Sliced list from index {start} to {end}: {lst[start:end]}"
    except Exception as e:
        return f"Error slicing list: {e}"

def index_game():
    sample_list = ['a', 'b', 'c', 'd', 'e']
    while True:
        print("\n--- Index Game ---")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        choice = input("Choose an operation (1-4): ")

        if choice == '1':
            index = int(input("Enter the index to access: "))
            print(access_element(sample_list, index))
        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(sample_list, index, new_value))
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(sample_list, start, end))
        elif choice == '4':
            print("Exiting the game. Bye!")
            break
        else:
            print("Invalid option. Try again.")

        print("Current list:", sample_list)

# Run the game
index_game()
