types_of_people = 10 #set types of people to 10
x = f"There are {types_of_people} types of people."#sets variable x to fstring

binary = "binary"#assigns string value binary to variable binary
do_not = "don't"#assigns string don't to variable do_not
y = f"Those who know {binary} and those who {do_not}."#sets variable y to fstring

print(x)#print variable x
print(y)#print variable y

print(f"I said: {x}")#prints formatted string contaning variable x
print(f"I also said: '{y}'")#prints formatted string contanting variable y

hilarious = False #sets variable hilarious to boolean false
joke_evaluation = "Isn't that joke so funny?! {}"#sets variable joke_Evaluation to string 'isnt that joke funny'

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)
