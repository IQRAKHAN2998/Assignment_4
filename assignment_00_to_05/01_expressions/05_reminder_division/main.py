# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and
#  also the remainder of the division.
#  (user input is in bold italics):

def reminder_divsion():
    to_be_divide: int = int(input("Enter an integer to be divided: "))
    divde_by : int = int(input("Enter an integer divide by: "))

    result: int = to_be_divide // divde_by
    reminder: int = to_be_divide % divde_by

    print(f"the result is divsion of \033[1m{result}\033[0m with a reminder of \033[1m{reminder}")

if __name__ == '__main__':
    reminder_divsion()