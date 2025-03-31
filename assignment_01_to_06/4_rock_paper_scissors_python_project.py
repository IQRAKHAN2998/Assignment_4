# Rock, paper, scissors Python Project
# In this Kylie Ying tutorial, you will work with random.choice(),
#  if statements, and getting user input. This is a great project to 
# help you build on the fundamentals like conditionals and functions.


import random

def get_computer_choice(difficulty):
    choices = ["rock", "paper", "scissors"]
    
    if difficulty == "easy":
        return random.choice(choices)  # Random choice
    elif difficulty == "hard":
        return "rock"  # Always picks rock for predictability
    
    # Smart AI (tries to counter last player move)
    last_move = input("Enter your last move for AI training (rock/paper/scissors): ").strip().lower()
    if last_move == "rock":
        return "paper"
    elif last_move == "paper":
        return "scissors"
    else:
        return "rock"

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "🎉 You win!"
    return "💻 Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors with AI Difficulty! 🤖")
    
    difficulty = input("Choose difficulty (easy/hard/smart): ").lower()
    if difficulty not in ["easy", "hard", "smart"]:
        print("❌ Invalid difficulty level! Defaulting to 'easy'.")
        difficulty = "easy"
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        if user_choice == "exit":
            print("👋 Thanks for playing! See you next time.")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Try again.")
            continue

        computer_choice = get_computer_choice(difficulty)
        print(f"Computer chose: {computer_choice}")

        print(get_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()


