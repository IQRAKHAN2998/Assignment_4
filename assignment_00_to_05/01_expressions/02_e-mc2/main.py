# user input is in bold 
#
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's 
# mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

def joules_energy():
    mass : float = float(input("Enter kilos of mass: "))
    C :int = 299792458
    energy = mass * (C ** 2)

    print("e = m * (c**2) ")
    print(f"m = {mass}")
    print(f"C = {C}")
    
    print(f"\033[1m{energy} joules of energy")

if __name__ == '__main__':
    joules_energy()

