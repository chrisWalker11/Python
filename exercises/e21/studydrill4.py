def add(a, b):
    print(f"ADDING {a} + {b}.\n")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}.\n")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}.\n")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}.\n")
    return a / b

age = 1
h = 2
w = 3
iq = 4

print(f"{age}\n")
print(f"{h}\n")
print(f"{w}\n")
print(f"{iq}\n")

what = add(age, subtract(h, multiply(w, divide(iq, 2))))
print(f"this is what the big nested formula comes out to {what}")


print("\n")

simple_formula = multiply(w, add(age, 1))
print(f"my formula is 3 * (1 + 1) = {simple_formula}")
