# Write a program to solve this age-related riddle!
# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.
# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):


def main():
    # Store Anton's age
    anton_age = 21
    
    # Beth is 6 years older than Anton
    beth_age = anton_age + 6
    
    # Chen is 20 years older than Beth
    chen_age = beth_age + 20
    
    # Drew is as old as Chen's age plus Anton's age
    drew_age = chen_age + anton_age
    
    # Ethan is the same age as Chen
    ethan_age = chen_age
    
    # Print the ages of all friends
    print(f"Anton age is {anton_age}.")
    print(f"Beth age is {beth_age}.")
    print(f"Chen age is {chen_age}.")
    print(f"Drew age is {drew_age}.")
    print(f"Ethan age is  {ethan_age}.")

# Run the main function
if __name__ == "__main__":
    main()
