
import time
import keyboard
import pyautogui
import win32api
import win32con

time.sleep(5)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)


while not keyboard.is_pressed('q'):
    start = pyautogui.locateCenterOnScreen('mobb.png', region=(390,35,1240,880), confidence=0.90)
    if start is not None:
        pyautogui.moveTo(start)  # Moves the mouse to the coordinates of the image
        click()
while not keyboard.is_pressed('q'):
    start = pyautogui.locateCenterOnScreen('mobd.png', region=(390,35,1240,880), confidence=0.90)
    if start is not None:
        pyautogui.moveTo(start)  # Moves the mouse to the coordinates of the image
        click()
while not keyboard.is_pressed('q'):
    start = pyautogui.locateCenterOnScreen('mobg.png', region=(390,35,1240,880), confidence=0.90)
    if start is not None:
        pyautogui.moveTo(start)  # Moves the mouse to the coordinates of the image
        click()
while not keyboard.is_pressed('q'):
    start = pyautogui.locateCenterOnScreen('mobh.png', region=(390,35,1240,880), confidence=0.90)
    if start is not None:
        pyautogui.moveTo(start)  # Moves the mouse to the coordinates of the image
        click()
