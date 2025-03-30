Scotland : int = 16
UAE : int = 25
MAYENGUA_AGE : int = 48

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Check if the user can vote in Scotlant
    if user_age >=  Scotland:
        print("You can vote in Scotland where the voting age is " + str(Scotland) + ".")
    else:
        print("You cannot vote in Scotland where the voting age is " + str(Scotland) + ".")
    
    # Check if the user can vote in UAE
    if user_age >= UAE:
        print("You can vote in UAE where the voting age is " + str(UAE) + ".")
    else:
        print("You cannot vote in UAE where the voting age is " + str(UAE) + ".")
    
    # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")



if __name__ == '__main__':
    main()