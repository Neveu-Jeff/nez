from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('mobbleu.png', region=(390,35,1240,880), confidence=0.9) != None:
        print("oui")
        time.sleep(0.5)
    else:
        print("non")
        time.sleep(0.5)
