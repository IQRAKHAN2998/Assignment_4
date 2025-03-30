# User se number input lena
curr_value = int(input("Enter a number: "))

# Jab tak value 100 se chhoti hai, loop chalay
while curr_value < 100:
    print(curr_value, end=" ")  # Print value space ke sath
    curr_value *= 2  # Value ko double karein

print(curr_value)  # Jab loop khatam ho, last value print karein
