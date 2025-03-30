MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print("remove element:", last_elem)


# Prompts the user to enter one element of the list at a time and returns the resulting list.
def get_lst():
    
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()