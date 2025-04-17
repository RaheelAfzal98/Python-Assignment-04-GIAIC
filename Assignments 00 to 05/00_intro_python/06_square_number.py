# Ask the user for a number and print its square (the product of the number times itself).
# Here's a sample run of the program (user input is in bold italics):
# Type a number to see its square: 4
# 4.0 squared is 16.0


def main():
    # Ask the user for a number
    userinput = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    userNumber = userinput ** 2
    
    # Print the result
    print(f"\nUser Number {userinput} and squared is {userNumber}.")

# Run the main function
if __name__ == "__main__":
    main()
