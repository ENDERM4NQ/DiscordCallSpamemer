import pydirectinput
import pyautogui
from time import sleep as wait
from os import system
system("title "+"BY ENDERMANQ")

print('''
 ▄▄·  ▄▄▄· ▄▄▌  ▄▄▌      .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
▐█ ▌▪▐█ ▀█ ██•  ██•      ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
██ ▄▄▄█▀▀█ ██▪  ██▪      ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
▐███▌▐█ ▪▐▌▐█▌▐▌▐█▌▐▌    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
·▀▀▀  ▀  ▀ .▀▀▀ .▀▀▀      ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀
You must be using the Discord APP, be in fullscreen, and go to DM's with the target.
''')

wait(0.1)

print("Warning, you cannot stop the program until all the calls have been completed.")
missedcalls = int(input("\nHow many calls would you like to spam? -> "))

for _ in range(missedcalls):
    pyautogui.moveTo(1450, 46)
    pydirectinput.doubleClick()
    pyautogui.moveTo(1223, 212)
    pyautogui.doubleClick()
    pyautogui.moveTo(1571, 38)
    pyautogui.doubleClick()
