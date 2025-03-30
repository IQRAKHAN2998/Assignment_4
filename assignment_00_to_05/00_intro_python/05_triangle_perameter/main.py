#Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
#user input is in bold 

def triangle():
    side1 : float = float(input("What is the length of side 1? "))
    side2 : float = float(input("What is the length of side 2? "))
    side3 : float = float(input("What is the length of side 3? "))
    primeter =str(side1 + side2 + side3)
    print(f"The perimeter of the triangle is \033[1m{primeter}")

if __name__ == '__main__':
    triangle()