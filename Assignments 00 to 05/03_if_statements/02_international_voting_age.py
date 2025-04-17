# Problem Statement
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:
# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)
# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)
# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)
# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.
# Here's a sample run of the program (user input is in blue):
# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where tzhe voting age is 48.


VOTING_AGE_PETURKSBOUIPO: int = 16
VOTING_AGE_STANLAU: int = 25
VOTING_AGE_MAYENGUA: int = 48

def check_voting_eligibility(age: int, country_age: int, country_name: str):
    if age >= country_age:
        print(f"You can vote in {country_name} where the voting age is {country_age}.")
    else:
        print(f"You cannot vote in {country_name} where the voting age is {country_age}.")

def main():
    # Prompt the user for their age
    age = int(input("How old are you? "))
    
    # Check eligibility for each country
    check_voting_eligibility(age, VOTING_AGE_PETURKSBOUIPO, "Peturksbouipo")
    check_voting_eligibility(age, VOTING_AGE_STANLAU, "Stanlau")
    check_voting_eligibility(age, VOTING_AGE_MAYENGUA, "Mayengua")

# Run the main function
if __name__ == '__main__':
    main()
