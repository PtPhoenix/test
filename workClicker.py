import pyautogui
import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


#print(pyautogui.size())
while True:
    pyautogui.click(10, 184, duration=1)
    pyautogui.click(30, 184, duration=1)
    pyautogui.click(30, 304, duration=1)
    pyautogui.click(125, 100, duration=1)
    pyautogui.click(125, 1100, duration=10)
    pyautogui.moveRel(1000, 30, duration=1)
    time.sleep(600)