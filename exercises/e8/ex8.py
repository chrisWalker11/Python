formatter = "{} {} {} {}" #assigns variable formatter to four {}

print(formatter.format(1, 2, 3, 4)) #format function passes the four values into the {}
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))# passes the formatter variable into format which then prints four {} for each {} in the orginial variable
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
))# passes each string that is seperated by commas into the {}s in the fromatter variable
