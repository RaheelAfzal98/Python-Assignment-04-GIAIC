def calculate_weight_on_planet(weight_on_earth, planet):
    # Define the gravity constants for each planet as a dictionary
    planet_gravities = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Get the gravity constant for the selected planet
    gravity_constant = planet_gravities.get(planet)
    
    if gravity_constant is None:
        return "Invalid planet name"
    
    # Calculate the weight on the selected planet
    weight_on_planet = weight_on_earth * gravity_constant
    # Return the weight rounded to 2 decimal places
    return round(weight_on_planet, 2)

# Main program
def main():
    # Prompt user for their weight on Earth
    weight_on_earth = float(input("Enter a weight on Earth: "))
    
    # Prompt user for the planet they want to check weight on
    planet = input("Enter a planet: ")

    # Calculate and display the weight on the chosen planet
    result = calculate_weight_on_planet(weight_on_earth, planet)
    if isinstance(result, float):
        print(f"The equivalent weight on {planet}: {result}")
    else:
        print(result)  # If it's an invalid planet name

if __name__ == "__main__":
    main()
