#Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

foot :int = 12

def total_inches():
    feet : float = float(input("Enter number of feet: "))
    inches : float = feet * foot
    print(f"there are {inches} inches in {feet} feet")

if __name__ == '__main__':
    total_inches()