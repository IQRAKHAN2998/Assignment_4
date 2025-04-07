# Planetary Weight Calculator
MARS = 0.378
JUPITER = 2.36
SATURN = 1.081
URANUS = 0.815
MERCURY = 0.376
VENUS = 0.889
NEPTUNE = 1.14

def main():
    earth_weight= float(input("your weight in earth: "))
    planet_name: str = input("select your palnet name: ")


    if(planet_name == "Mars"):
        gravity_factor = MARS
    elif(planet_name == "Jupiter"):
        gravity_factor = JUPITER
    elif(planet_name == "Saturn"):
        gravity_factor = SATURN
    elif(planet_name == "Uranus"):
        gravity_factor = URANUS
    elif(planet_name == "Mercury"):
        gravity_factor = MERCURY
    elif(planet_name == "Venus"):
        gravity_factor = VENUS
    else:
       gravity_factor = NEPTUNE

    # Calculate the equivalent weight on the selected planet
    plantery_weight = earth_weight * gravity_factor
    rounded = round(plantery_weight , 2)

    print(f"The equivalent weight on {planet_name}: {rounded}")
if __name__ == "__main__":
    main()