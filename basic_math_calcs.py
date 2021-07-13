import math
r = float(input("Enter radius of the cylinder: "))
h = float(input("Enter height of the cylinder: "))

a = math.pi*r*r
sa = ((2*math.pi*r)*h) + ((math.pi*r**2)*2)
v = math.pi * r * r * h

print("The area is : %.2f" %a)
print("The surface area is: %.2f" %sa)
print("the volume is %.2f" %v)
