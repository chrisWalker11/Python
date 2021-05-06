import random
while True:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    if d1 == d2:
        print(f"You rolled {d1} and {d2}\nYou rolled doubles!")
    else:
        print(f"you rolled {d1} and {d2}")
    end = input("do you want to roll again Y/N\n>").upper()
    if end == "N":
        break
print("goodbye!")
