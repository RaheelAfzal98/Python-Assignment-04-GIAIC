# Problem Statement
# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements
# The first even number is 0:
# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38


TOTAL_EVEN_NUMBERS = 20

def print_even_numbers(count):
    number = 0
    for _ in range(count):
        print(number, end=" ")
        number += 2

def main():
    print("First", TOTAL_EVEN_NUMBERS, "even numbers:")
    print_even_numbers(TOTAL_EVEN_NUMBERS)

if __name__ == '__main__':
    main()
