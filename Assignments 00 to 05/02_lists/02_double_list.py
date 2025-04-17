# Problem Statement
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]


def double_numbers(numbers: list[int]) -> list[int]:
    """
    Takes a list of integers and returns a new list 
    where each number is doubled.
    """
    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    return doubled

def main():
    numbers = [1, 2, 3, 4]  # Original list
    result = double_numbers(numbers)  # Get doubled list
    print(result)  # Print the new list

if __name__ == '__main__':
    main()
