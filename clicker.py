import pyautogui
print('position mouse')
input("r?")
print(pyautogui.position())
cx = int(input("enter x coords: "))
cy = int(input("enter y coords: "))
for i in range(int(input("enter number of clicks: "))):
    pyautogui.click(cx, cy)
