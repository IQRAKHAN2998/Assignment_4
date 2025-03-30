def print_multiple(message: str , repeats: int):
    for i in range(repeats):
        print(message)
        

def main():
    message = input("type a message: ")
    repeats = int(input("Enter a number: "))
    print_multiple(message , repeats)



if __name__ == '__main__':
    main()