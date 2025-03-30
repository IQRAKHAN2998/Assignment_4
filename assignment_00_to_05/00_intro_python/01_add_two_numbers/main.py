# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

def main():
    print("This program adds two numbers.")
    num1 : str = int(input("Enter first number: "))
    num2  : str = int(input("Enter second number: "))
    total : int = num1 + num2
    print(f"The total is " + str(total))
    

if __name__ == '__main__':
    main()