# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

def calculate_sum(values: list[int]) -> int:
    """
    Calculates and returns the total sum of all integers in the given list.
    """
    total: int = 0
    for val in values:
        total += val
    return total

# No changes needed below this line
def main():
    number_list: list[int] = [10, 20, 30, 40]  # Define a list of integers
    total_sum: int = calculate_sum(number_list)  # Call the function to compute the sum
    print(f"The total sum is: {total_sum}")  # Output the result

if __name__ == '__main__':
    main()
