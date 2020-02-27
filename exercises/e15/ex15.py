from sys import argv #from sys module import argument variable

script, filename = argv #unpacks argument variable seperates the arguments given

txt = open(filename) #opens the filename given in the argv

print(f"Here's your file {filename}:") #prints out the name of the filename
print(txt.read())#reads txt files

print("Type the filename again")
file_again = input("> ")#prompts for input in this case looking for the filename again

txt_again = open(file_again)#opens the file from the above input

print(txt_again.read())#prints out the contents of the file

txt.close()

txt_again.close()
