# Last element print karne ka function
def get_last_element(lst):
    print(lst[-1])  # List ka last element print karega

# User se list input lene ka function
def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

# Function call aur last element print karna
def main():
    lst = get_lst()
    if lst:  # Ensure list empty na ho
        get_last_element(lst)
    else:
        print("List is empty.")

if __name__ == '__main__':
    main()
2