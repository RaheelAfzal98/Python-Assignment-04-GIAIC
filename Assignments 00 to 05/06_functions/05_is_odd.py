# Problem Statement
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd



def main():
    for i in range(10, 20):  # Iterate through numbers 10 to 19
        if is_even(i):
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
            
def is_even(value: int):
    """
    Checks to see if a value is even. If it is, returns true.
    """
    
    return value % 2 == 0  # If value is divisible by 2, it is even


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
