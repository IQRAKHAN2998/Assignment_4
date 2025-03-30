def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0  # Formula apply kar raha hai

def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # User se input lena
    celsius = fahrenheit_to_celsius(fahrenheit)  # Conversion function call karna
    print(f"Temperature: {fahrenheit}F = {celsius}C")  # Output print karna

if __name__ == "__main__":
    main()
