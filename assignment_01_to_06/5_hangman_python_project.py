# Hangman Python Project
# In this Kylie Ying tutorial, you will learn how to work with dictionaries, 
# lists, and nested if statements. You will also learn how to work with the 
# string and random Python modules.

import random

# Possible words
word_pool = ["python", "developer", "hangman", "programming", "computer"]

def start_hangman():
    secret_word = random.choice(word_pool)
    guessed_letters, remaining_tries = set(), 6

    print("🎩 Hangman Challenge! Try to solve the mystery word. 🔤")

    while remaining_tries > 0:
        print("\nCurrent progress:", " ".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
        print(f"Tries left: {remaining_tries}")

        player_guess = input("Type a letter: ").lower()
        if not player_guess.isalpha() or len(player_guess) != 1 or player_guess in guessed_letters:
            print("⚠ Invalid attempt or duplicate entry!")
            continue

        guessed_letters.add(player_guess)
        if player_guess not in secret_word:
            remaining_tries -= 1
            print("❌ Not in the word!")

        if set(secret_word) <= guessed_letters:
            print(f"🎉 You nailed it! The word was: {secret_word}")
            return

    print(f"💀 You lost! The hidden word was: {secret_word}")

if __name__ == "__main__":
    start_hangman()
