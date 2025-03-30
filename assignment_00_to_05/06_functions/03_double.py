def double_num(num):
    return num * 2

def main():
    num = int(input("enter a number: "))
    num2 = double_num(num)
    print(f"Double that is {num2}")

if __name__ == '__main__':
    main()