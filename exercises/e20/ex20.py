from sys import argv #import argv from sys module

script, input_file = argv #declare variables input_file is test.txt

def print_all(f): #define print_all function with variable f. f means file
    print(f.read()) #prints and reads the file in the function print_all

def rewind(f): #define function rewind with file variable
    f.seek(0) #rewinds to the first byte of the file

def print_a_line(line_count, f): #defines function print_a_line has file variable and line_count
    print(line_count, f.readline())#prints line_count and reads the file line

current_file = open(input_file)#opens argv input_file and inside new variable current_file

print("First let's print the whole file:\n") #prints strings with new line

print_all(current_file)#uses print_all function with current_file variable and prints the contents of the test.txt file

print("Now let's rewind, kind of like a tape.") #prints out strings

rewind(current_file)#uses rewind function with current file variable goes to the first byte of the file

print("Let's print three lines:")#prints out strings

current_line = 1 #sets variable current_line to one
print_a_line(current_line, current_file)#runs print_a_line function on the open test.txt file and reads line one

current_line = current_line + 1 #increments the line count so now its line 2
print_a_line(current_line, current_file) #runs on line two of test.txt and prints out line 2

current_line = current_line + 1 #increments the line count so now it is line 3
print_a_line(current_line, current_file) #current_line is now set to 3 so it reads that and prints out line 3
