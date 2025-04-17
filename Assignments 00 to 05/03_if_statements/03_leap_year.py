# Problem Statement
# Write a program that reads a year from the user and tells whether a given year is a leap year or not.
# A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.
# In the Gregorian calendar, three criteria must be checked to identify leap years:
# The given year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is NOT a leap year; unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# Your code should use the above criteria to check for a leap year and then print either "That's a leap year!" or "That's not a leap year."


def check_leap_year(year: int):
    # Determine if the year is a leap year based on the conditions
    if year % 4 != 0:
        return "That's not a leap year."
    elif year % 100 != 0:
        return "That's a leap year!"
    elif year % 400 != 0:
        return "That's not a leap year."
    else:
        return "That's a leap year!"

def main():
    # Get the year from the user
    year = int(input("Enter a year to check: "))
    
    # Call the function to check if it's a leap year
    result = check_leap_year(year)
    
    # Output the result
    print(result)

# Call the main function when the script is executed
if __name__ == '__main__':
    main()
