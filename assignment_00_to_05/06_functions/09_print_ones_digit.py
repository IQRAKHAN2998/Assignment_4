def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    """
    ones_digit = num % 10         # Modulo 10 se ones digit milti hai
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # User se input lena
    print_ones_digit(num)                 # Function call karna

if __name__ == "__main__":
    main()
