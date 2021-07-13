from random import randint
c = [0, 0, 0, 0, 0, 0]
nt = int(input("Enter number of rolls\n>"))
for i in range(nt):
    roll = randint(1, 6)
    c[roll -1] += 1

for i in range(6):
    print("Number of times side", i + 1, "was rolled", c[i])
    print("Percentage is", c[i] / nt)
