import random

DONE_LIKELIHOOD = 0.2         # 20% chance of stopping

def chaotic_counting():
    for i in range(10):       # Loop chalega 10 tak
        curr_num = i + 1      # i starts from 0, so 1 add kar ke 1-10 tak counting milegi

        if done():            # done() check karega agar counting stop karni hai ya nahi
            return            # Agar done() True return kare, toh function yahin end ho jayega!
        print(curr_num)       # Agar done() False ho, toh number print hoga


def done():
    # """ Returns True with a probability of DONE_LIKELIHOOD """

    if random.random() < DONE_LIKELIHOOD:
        return True             # Kuch chance ke sath True dega (randomly)
    return False                # Baaki time False dega


def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")  
    chaotic_counting()             # chaotic_counting() ko call karega
    print("I'm done")              # Jab chaotic_counting() khatam ho jaye, toh print karega "I'm done"


if __name__ == "__main__":
    main()