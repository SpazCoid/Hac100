
import ctypes
from tkinter import *
from tkinter import Tk

def Root():
    global root
    root = Tk()
    
    user32 = ctypes.windll.user32
    width  = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)



    root.geometry(f'{width}x{height}')
    root.mainloop()

Root()
