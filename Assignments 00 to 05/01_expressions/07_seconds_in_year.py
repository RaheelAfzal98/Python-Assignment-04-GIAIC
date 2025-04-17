# Problem Statement
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):
# There are 5 seconds in a year!
# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.


# Constants
DAYS_IN_YEAR: int = 365
HOURS_IN_DAY: int = 24
MINUTES_IN_HOUR: int = 60
SECONDS_IN_MINUTE: int = 60

def main():
    # Ask the user how many years they want to calculate for
    years: int = int(input("Enter the number of years: "))

    # Calculate seconds in the given number of years
    seconds_in_year: int = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    total_seconds: int = years * seconds_in_year

    # Print the result
    print(f"\nThere are {total_seconds} seconds in {years} year(s)!")

# Run the program
if __name__ == '__main__':
    main()
