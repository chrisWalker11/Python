#!/usr/bin/python3
import re
def isValidSSN(str):
    regex = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$"
    
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return print(str)
    else:
        return False

input_file = open('ssn.txt', 'r')
count_lines = 0
for line in input_file:
    print(isValidSSN(line))
    count_lines += 1
