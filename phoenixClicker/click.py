import pyautogui 
from variables import *
for i in range(int(input("enter number of clicks: "))):
    pyautogui.moveTo(x1, y1)
    pyautogui.click(x1, y1)
    pyautogui.moveTo(x2, y2)
    pyautogui.click(x2, y2)
