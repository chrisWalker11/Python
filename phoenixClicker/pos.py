import pyautogui



print("start with agent of choice")
input("press enter once over agent")
print(pyautogui.position())
px = input("input x coordinate for agent: ")
py = input("input y coordinate for agent: ")
with open("variables.py", "w") as f:
    f.writelines("x1 = " + px + '\n')
    f.writelines("y1 = " + py + '\n')


print("put cursor  over agent confirm")
input("press enter once over confirm")
print(pyautogui.position())
lx = input("input x coordinate for confirm: ")
ly = input("input y coordinate for confirm: ")
with open("variables.py", 'a') as f:
    f.writelines("x2 = " +  lx + '\n')
    f.writelines("y2 = " + ly)
