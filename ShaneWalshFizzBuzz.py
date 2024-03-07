def fizzbuzz():
    for num in range(0, 101):
        output = ""
        if num % 3 == 0:
            output += "Fizz"
        if num % 5 == 0:
            output += "Buzz"
        print(output or num)

def main():
    fizzbuzz()

if __name__ == "__main__":
    main()
