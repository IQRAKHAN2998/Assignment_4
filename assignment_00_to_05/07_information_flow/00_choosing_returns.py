ADULT_AGE: int = 18   

def is_adult(age: int):
    return age >= ADULT_AGE  # Direct return kar diya

def main():
    age: int = int(input("How old is this person?: "))  
    print(is_adult(age))

if __name__ == "__main__":
    main()
