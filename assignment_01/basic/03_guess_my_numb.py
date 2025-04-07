import random
def main():
    secret_num: int = random.randint(1 , 99)
    print("I am thinking of a number between 1  and 99...")

    guess_number = int(input("Enter your guess number: "))
   
    while guess_number != secret_num:
        if(guess_number < secret_num):
            print("Your guess is to low")
        else:
            print("Your guess is too high")

        print("***************")
        guess_number = int(input("Enter your guess number:"))
    print(f"Congrats! the number was : {secret_num}")

if __name__ == "__main__":
    main()