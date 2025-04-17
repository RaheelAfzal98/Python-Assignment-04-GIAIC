# Problem Statement
# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements
# The first even number is 0:
# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38


def main():
    even_numbers = []  # Create an empty list to store the even numbers
    
    # This for-loop starts at 0 and counts up to 19 (for a total of 20 numbers)
    for i in range(20):
        even_numbers.append(i * 2)  # Add the even number to the list
    
    # Print the list of even numbers
    print(" ".join(map(str, even_numbers)))  # Join the list elements into a string, separated by spaces

# Call the main function when "run", no need to edit anything below!
if __name__ == "__main__":
    main()
