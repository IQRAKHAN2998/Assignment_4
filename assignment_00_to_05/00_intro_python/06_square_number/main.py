# Ask the user for a number and print its square (the product of the number times itself).
#user input is in bold 

def square():
    square_number :float = float(input("Type a number to see its square: "))
    result: float =  square_number * square_number
    print(f"{square_number} squared is \033[1m{result}")

if __name__ == '__main__':
    square()