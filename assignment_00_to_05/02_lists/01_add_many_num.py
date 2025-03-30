#Write a function that takes a list of numbers and returns the sum of those numbers.

def add_numbers(*numb)-> list:
    total = 0
    for number in numb:
        total += number

    return total
    
ans = add_numbers(1,2,3,4,5)
print(ans)

if __name__ == '__main__':
    add_numbers()