# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """


def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    """
    return low <= n <= high

# Example usage
def main():
    num = int(input("Enter a number: "))
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

    if in_range(num, lower, upper):
        print(f"{num} is within the range [{lower}, {upper}]")
    else:
        print(f"{num} is outside the range [{lower}, {upper}]")

if __name__ == '__main__':
    main()
