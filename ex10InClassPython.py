def methodc(x):
    y = x * 10
    print(f"in mC x is {x}")
    print(f"in mC y is {y}")
    return y

def methodb(x):
    print("in methodb x is " + str(x))
    num = methodc(x + 2)
    print("in methodb num is " + str(num))
    return "hello"

def methoda():
    message = methodb(7)
    print(message)
    return 10 * 10

def main():
    a = methoda()
    print("in main, methoda returned " + str(a))


main()
