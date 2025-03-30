def read_phone_numbers():
    # """
    # Ask the user for names/numbers to story in a phonebook (dictionary).
    # Returns the phonebook.
    # """
    phonebook = {}                   # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    # """
    # Prints out all the names/numbers in the phonebook.
    # """
    for name in phonebook:                               # Dictionary ke har name (key) ke liye
        print(str(name) + " -> " + str(phonebook[name])) # Name aur number print karo


def lookup_numbers(phonebook):
    # """
    # Allow the user to lookup phone numbers in the phonebook
    # by looking up the number associated with a name.
    # """
    while True:
        name = input("Enter name to lookup: ")       # User se name input
        if name == "":
            break                                    # Agar user blank enter kare to loop break
        if name not in phonebook:
            print(name + " is not in the phonebook")   # Agar naam phonebook me nahi hai
        else:
            print(phonebook[name])                    # Agar naam mil jaye to number print karo


def main():
    phonebook = read_phone_numbers()  # Phonebook input lo
    print_phonebook(phonebook)  # Sare numbers print karo
    lookup_numbers(phonebook)  # Lookup system start karo



# Python boilerplate.
if __name__ == '__main__':
    main()