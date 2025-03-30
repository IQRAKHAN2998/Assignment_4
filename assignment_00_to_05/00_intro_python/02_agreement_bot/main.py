# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!"

def fav_animal():
    favorite_animal = input("What is your favorite animal? ")
    msg =(f"My favorite animals is also \033[1m{favorite_animal}")
    print(msg)

if __name__ == '__main__':
    fav_animal()