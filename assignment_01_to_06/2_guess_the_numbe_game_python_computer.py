# Guess the Number Game Python Project (computer)
# In this Kylie Ying tutorial, you will learn how to work with Python's 
# random module, build functions, work with while loops and conditionals,
#  and get user input.

import random

def number_guessing_game():
    print(" Welcome to the Number Guessing Game!")

    for _ in range(5):  # 5 rounds
        target = random.randint(1, 100)
        guess = None

        while guess != target:
            guess = int(input("Guess a number (1-100): "))
            print("Too low!" if guess < target else "Too high!" if guess > target else f"🎉 Correct! The number was {target}.\n")

if __name__ == "__main__":
    number_guessing_game()
