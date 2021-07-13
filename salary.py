s = int(input("Enter annual salary: "))
y = int(input("Enter years on job: "))
if s >= 30000 and y >= 2:
    print("you qualify for the loan")
elif s < 30000 and y < 2:
    print("not enough years nor salary to qualify")

elif s >= 30000 and y < 2:
    print("Not enough years to qualify")

elif s < 30000 and y >= 2:
    print("not enough salary to qualify")
