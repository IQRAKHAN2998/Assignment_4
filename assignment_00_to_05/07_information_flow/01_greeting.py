def greet_name(name: str):
    return f"Greeting {name}!"

def main():
    name = input("Whats your name: ")
    print(greet_name(name))

if __name__ == '__main__':
    main()