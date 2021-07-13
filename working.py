def funct1(x):
    i = 0
    a = []
    while i < x:
        a.append(i)
        i += 1
    return a

def f2(a):
    for i in a:
        print(f"{i}")

x = int(input("> "))
a = funct1(x)
funct2(a)
