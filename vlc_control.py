import serial as sl
import pyautogui as pag
from time import sleep

s_obj = sl.Serial('com6', 9600)
print("Starting")
sleep(2)
print("Successful")

while True:
    msg = s_obj.readline().decode('utf-8').strip()
    print(msg)

    if msg == "Play/Pause":
        pag.press('space',interval=0.2)
    elif msg == "VolumeUP":
        pag.press('up')
    elif msg == "VolumeDown":
        pag.press('down')
    elif msg == "Forward":
        pag.press('right')
    elif msg == "Backward":
        pag.press('left')
    else:
        print("Nothing")
