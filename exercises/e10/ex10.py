tabby_cat = "\tI'm tabbed in." # makes variable tabby_cat with escape sequence for horizontal tab
persian_cat = "I'm split\non a line." # makes variable persian_cat contain a varible with \n in the middle which is the escape sequence for a new line
backslash_cat = "I'm \\ a \\ cat." # \\ is the escape sequence for \

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""  #combines various escape sequences prints tabbed lines and then makes a new line that is also tabbed

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
