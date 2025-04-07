import random

rounds = 5

def main():
    print("Welcome to the Hight-Low Game!")
    print('_____________________________')

    your_score = 0

    for i in range(rounds):
        print(f"round {i + 1} ")

        # computer number
        computer_num : int = random.randint(1,100)
        your_num :int = random.randint(1,100)
        print(f"your number is {your_num}")

        # user input higher and lower
        choice: str = input("Do you think your number is higher or lower than the computer's?: ")
                            
        # highr and lower conditions
        higher_correct: bool = choice == "higher" and your_num > computer_num
        lower_correct : bool = choice == "lower" and your_num < computer_num

        # if else condition with or
        if higher_correct or lower_correct:
            print(f"You were right! The computers was ,{computer_num}")
            
            # score
            your_score += 1
        
        else:
            print(f"Aww that's incorrect. The computers number was , {computer_num}")

        print(f"Your score is now, {your_score}")
        print("******************************")

    print("Thankx for playing")

if __name__ == "__main__":
    main()