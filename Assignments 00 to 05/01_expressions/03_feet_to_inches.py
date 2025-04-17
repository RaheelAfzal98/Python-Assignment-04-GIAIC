# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    # Ask the user to enter a length in feet
    feet: float = float(input("Enter length in feet: "))

    # Convert feet to inches
    inches: float = feet * 12

    # Display the result
    print(f"{feet} feet is equal to {inches} inches.")

# No need to modify anything below
if __name__ == '__main__':
    main()
