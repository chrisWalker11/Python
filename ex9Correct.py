def s():

    while True:
        try:
           score = int(input("Enter score: "))
        except ValueError:
            print("invalid try again")
            continue
        if score < 0 or score > 100:
            print("invalid try again")
        else:
            return score

def g(score):

    if score <= 100 and score >= 90:
        grade = "A"
    if score <= 89 and score >= 80:
        grade = "B"
    if score <= 79 and score >= 70:
        grade = "C"
    if score <= 69 and score >= 60:
        grade = "D"
    if score <= 59:
        grade = "F"
    return grade

def main():
   score = s()
   grade = g(score)
   print(f"Letter grade is {grade} for score {score}")

main()


