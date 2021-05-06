def ask_for_int(prompt, low, high):
    while True:
        try:
            num = int(input(prompt))
            if num >= low and num <= high:
                return num
            else:
                print("Integer must be between", low, "and", high)
        except:
            print("Enter valid integers only. try again")

def factorial(num):
    if num <= 0:
        return 1
    else:
        return num * factorial(num - 1)
    return num

def main():
    print("Welcome")
    while True:
        x = ask_for_int("Please enter a postive integer : ", 0, 996)
        answer = factorial(x)
        print(f"the answer is {answer}")
        loop = input("Do you want toe loop again Y/N: ").upper()
        if loop == "N":
            break
    print("Goodbye")
main()
