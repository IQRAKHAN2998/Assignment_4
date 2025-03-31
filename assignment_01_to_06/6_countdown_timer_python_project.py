# Countdown Timer Python Project
# In this Code With Tomi tutorial, 
# you will learn how to build a countdown timer using the time Python module.
#  This is a great beginner project to get you used to working with while loops in Python.


import time

def timer(count):
    """Displays a decreasing countdown from the given seconds."""
    while count > 0:
        mm, ss = divmod(count, 60)
        print(f"{mm:02d}:{ss:02d}", end="\r")
        time.sleep(1)
        count -= 1

    print("🚨 Time Over!")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter countdown time (seconds): "))
        timer(user_input)
    except ValueError:
        print("⚠ Error! Please enter a valid integer.")