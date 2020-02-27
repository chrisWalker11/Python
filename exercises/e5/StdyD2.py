#convert pounds to kilograms and inches to centimeters write variables to reflect this
name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kilograms = weight * 2.2
cm = height * 2.54

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall and he's {cm} tall")
print(f"He's {weight} pounds & He's' {kilograms}) kg.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky try to get it exactly right
total = age + height + weight
print(f"If i add {age}, {height}, and {weight} I get {total}.")
