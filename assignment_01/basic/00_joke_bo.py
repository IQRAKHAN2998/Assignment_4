joke_msg = """Why did the Python developer go broke?
Because he kept using except: but never caught anything! 😅"""


def jokes():
    user_input = input("What do you want: ").lower()
    if user_input == "joke":
        print(joke_msg)
    else:
        print("Sorry i only tell joke")

if __name__ == "__main__":
    jokes()