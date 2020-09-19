import pyautogui



print("start with phoenix")
input("press enter once over agent")
print(pyautogui.position())
px = input("input x coordinate for next photo: ")
py = input("input y coordinate for next photo: ")
with open("variables.py", "w") as f:
    f.writelines("x1 = " + px + '\n')
    f.writelines("y1 = " + py + '\n')


print("put cursor  over agent confirm")
input("press enter once over confirm)
print(pyautogui.position())
lx = input("input x coordinate for like: ")
ly = input("input y coordinate for like: ")
with open('variables.py', 'a') as f:
    f.writelines("x2 = " +  lx + '\n')
