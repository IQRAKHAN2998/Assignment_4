# Guess the Number Game Python Project (user)
# In this Kylie Ying tutorial, you will build a guessing game where the computer 
# has to guess the correct number. You will work with Python's random module,
#  build functions, work with while loops and conditionals, and get user input.


import random

def computer_guesses():
    print("Think of a number (1-100), and I'll guess it!")

    low, high = 1, 100
    attempts = 0

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1

        print(f"Is it {guess}?")
        user_feedback = input("Enter 'h' for too high, 'l' for too low, or 'c' for correct: ").lower()

        if user_feedback == "h":
            high = guess - 1
        elif user_feedback == "l":
            low = guess + 1
        elif user_feedback == "c":
            print(f"🎉 Guessed in {attempts} tries!")

            # Scoring system
            if attempts <= 5:
                print("🏆 Excellent! I am a genius! 🧠")
            elif attempts <= 10:
                print("🙂 Good, but I can do better.")
            else:
                print("😅 That took a while...")

            return
        else:
            print("⚠️ Invalid input!")

if __name__ == "__main__":
    computer_guesses()
