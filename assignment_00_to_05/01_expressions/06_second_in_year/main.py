# Use Python to calculate the number of seconds in a year
days :int = 365
hour: int = 24
mint :int = 60
sec :int = 60

def seconds():
    result = days * hour * mint * sec
    print(f"There are {result} seconds in a year")

if __name__ == '__main__':
    seconds()