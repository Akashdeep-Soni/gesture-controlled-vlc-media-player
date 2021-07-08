from tkinter import *
from PIL import ImageTk, Image
import serial as sl
import pyautogui as pag
from time import sleep
                     
root = Tk()
root.title("VLC Process Window")
root.geometry("640x360")

s_obj = sl.Serial('com6', 9600)
sleep(2)

# BG Image        
bg = ImageTk.PhotoImage(file="bg_img.jpg")
bg_image = Label(root, image=bg).place(relwidth=1,relheight=1)

# Frame
fm = Frame(root, bg = "white")
fm.place(x=40,y=60, height=200, width=250)

title = Label(fm, text="VLC Process Window", font=("Impact",20,), fg="#d77337", bg='white')
title.place(x=10,y=10)

status = Label(fm, font=("Goudy Old Style",20,), fg="#d77337", bg='white')

def fun():
    msg = s_obj.readline().decode('utf-8').strip()
    status.config(text=msg)
    status.place(x=10,y=60)
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
    root.after(10,fun)

def start():
    root.after(1,fun)

start_bt = Button(fm, text="Start", command = start, fg="white", bg="#d77337", font=("Times New Roman",20))
start_bt.place(x=80,y=120,width=100,height=40)

root.mainloop()
