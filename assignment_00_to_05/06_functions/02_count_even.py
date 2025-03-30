
def count_even(lst):

    count = 0              # Even numbers count store karne ke liye variable

    for num in lst:       # List ke har number par loop chalega
        if num % 2 == 0:  # Agar number even hai (2 se divide ho sakta hai)
            count += 1    # Even number mil gaya toh count +1 badhao

    print(count)            # Finally, total even numbers print karo
    
         
      
def get_list_of_ints():
    
    lst = []                       # Ek khaali list banayi integers store karne ke liye
    user_input = input("Enter an integer or press enter to stop: ")  # Pehla input lo

    while user_input != "":           # Jab tak user sirf enter nahi dabata...
        lst.append(int(user_input))   # Input ko integer me convert kar ke list me add karo
        user_input = input("Enter an integer or press enter to stop: ")  # Next input lo

    return lst                         # Jab user enter press kare, toh final list return karo


def main():
    lst = get_list_of_ints()        # User se numbers input le kar ek list banayega
    count_even(lst)                # Us list ke even numbers count karega



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()