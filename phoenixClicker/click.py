import pyautogui
x1 = 987
y1 = 968
x2 = 986
y2 = 864
while True:
#pyautogui.click(pyautogui.locateOnScreen('p.png'))
pyautogui.moveTo(x1, y1)
pyautogui.click(x1, y1)
pyautogui.moveTo(x2, y2)
pyautogui.click(x2, y2)
