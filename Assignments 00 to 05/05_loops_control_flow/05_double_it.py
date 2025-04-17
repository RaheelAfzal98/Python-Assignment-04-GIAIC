# Problem Statement
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.
# For example if the user enters the number 2 you would then print:
# 4 8 16 32 64 128
# Note that:
# 2 doubled is 4
# 4 doubled is 8
# 8 doubled is 16
# and so on.
# We stop at 128 because that value is greater than 100.
# Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value. Recall that you can double the value of curr_value using a line like:
# curr_value = curr_value * 2
# This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:
# while curr_value < 100:




def main():
    # Get initial number from the user
    start_number = int(input("Please enter a number: "))
    
    # Set the current value to the doubled number
    curr_value = start_number * 2
    
    # Keep doubling and printing the number until it reaches or exceeds 100
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value = curr_value * 2
    
    # Print the final number that caused the loop to end (100 or more)
    print(curr_value)

if __name__ == '__main__':
    main()
