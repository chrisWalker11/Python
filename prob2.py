import random
while True:
    roll = random.randint(0,6)
    print("You rolled . . .", roll)
    roll_again = input("Do you want to roll again? ")
    if roll_again == "N":
        print("Goodbye!")
        break

