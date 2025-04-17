# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.
# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
# Here is an example run of the program (user input is in bold italics):
# How many (apple) do you want?: 2
# How many (durian) do you want?: 0
# How many (jackfruit) do you want?: 1
# How many (kiwi) do you want?: 0
# How many (rambutan) do you want?: 1
# How many (mango) do you want?: 3
# Your total is $99.5

def main():
    # Fruit prices per unit
    fruit_prices = {
        'apple': 1.5,
        'durian': 50.0,
        'jackfruit': 80.0,
        'kiwi': 1.0,
        'rambutan': 1.5,
        'mango': 5.0
    }

    total = 0.0

    for fruit in fruit_prices:
        try:
            count = int(input(f"Enter quantity of {fruit}: "))
        except ValueError:
            count = 0  # If input isn't valid, treat it as 0
        total += fruit_prices[fruit] * count

    print(f"Total amount due: ${total}")


if __name__ == "__main__":
    main()
