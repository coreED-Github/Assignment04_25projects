def calculate_weight_on_planet(earth_weight, planet):
    gravity_factors = {
        "Mercury": 37.6,
        "Venus": 88.9,
        "Mars": 37.8,
        "Jupiter": 236.0,
        "Saturn": 108.1,
        "Uranus": 81.5,
        "Neptune": 114.0
    }
    
    if planet in gravity_factors:
        planet_gravity = gravity_factors[planet] / 100
        planet_weight = earth_weight * planet_gravity
        return round(planet_weight, 2)
    else:
        return None

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    planet_weight = calculate_weight_on_planet(earth_weight, planet)
    
    if planet_weight is not None:
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet entered. Please try again.")

main()