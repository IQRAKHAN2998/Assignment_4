def double_value():
    user_input = int(input("Write a NUMBER: "))
    curr_value = user_input 
    while curr_value < 100:
        print(curr_value)
        curr_value = curr_value * 2

if __name__ == "__main__":
    double_value()