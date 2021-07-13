import random
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
tr = int(input("enter total number of desired rolls\n>"))
for i in range(tr):
    roll = random.randint(1,6)
    if roll == 1:
        c1 += 1
    elif roll == 2:
        c2 += 1
    elif roll == 3:
        c3 += 1
    elif roll == 4:
        c4 += 1
    elif roll == 5:
        c5 += 1
    elif roll == 6:
        c6 += 1

print(f"one was rolled {c1} times")
print("percentage is ",c1 / tr)
print(" ")

print(f"two was rolled {c2} times")
print("percentage is ", c2 / tr)
print("")

print(f"three was rolled {c3} times")
print("percentage is ", c3 / tr)
print("")

print(f"four was rolled {c4} times")
print("percentage is ", c4 / tr)
print("")

print(f"five was rolled {c5} times")
print("percentage is ", c5 / tr)
print("")

print(f"six was rolled {c6} times")
print("percentage is ", c6 / tr)
print("")
print("Goodbye!")