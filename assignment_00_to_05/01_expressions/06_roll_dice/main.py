#Simulate rolling two dice, and prints results of each roll as well as the total.
import random 

dice :int  = 6

def roll_dice():
    
    dice1 :int = random.randint(1, dice)
    dice2 :int = random.randint(1, dice)

    total :int = dice1 + dice2

    print("Dice have", dice, "sides each.")
    print("First die:", dice1)
    print("Second die:", dice2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    roll_dice()