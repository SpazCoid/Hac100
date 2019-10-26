import ctypes
from tkinter import *
from tkinter import messagebox
from tkinter import Tk
import hashlib


def Root():
    global root, width, height

#---SETTING UP MAIN WINDOW
    root = Tk()
    root.attributes('-fullscreen', True)
    root.bind('<Escape>',lambda e: root.destroy())
    root.configure(background="#cdfbff")
    MainLogin()
    root.mainloop()


def MainLogin():
    global User_IDvar, User_PASSvar, frameLogin, frameLoginButtons

#---MAIN LOGIN FRAME
    frameLogin = Frame(root)
    frameLogin.pack()
    frameLogin.configure(background="#cdfbff")
    Label(frameLogin, text="User Login Screen",font=("Helvetica 15 bold") , background = "#cdfbff").grid(row=1,column=0)

#---SPACE
    Label(frameLogin, text="\t\t", background="#cdfbff").grid(row=2,column=0, )

#---USERNAME ENTRY
    Label(frameLogin, text = "Username", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=3, column=0)
    User_IDvar = StringVar()
    User_ID = Entry(frameLogin, textvariable=User_IDvar).grid(row=3,column=1)

    Label(frameLogin, text = "Password", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=4,column=0)
    User_PASSvar = StringVar()
    User_PASS = Entry(frameLogin, textvariable=User_PASSvar, show='*').grid(row=4,column=1)

    frameButtonL = Frame(root)
    frameButtonL.pack()
    frameButtonL.configure(background="#cdfbff")

    #---SPACE
    Label(frameLogin, text="\t\t", background="#cdfbff").grid(row=5,column=0, )
    
    #7f82ff - Colour for buttons
    b1 = Button(frameButtonL,text="Login",background="#7f82ff").grid(row=1,column=0)
    Label(frameButtonL, text="      ", background="#cdfbff").grid(row=1,column=1)
    b2 = Button(frameButtonL,text="Cancel", background="#7f82ff").grid(row=1,column=2)

def Login():

    user = User_IDvar.get()
    pwd = User_PASSvar.get()

    key = hashlib.sha256(str(pwd).encode()).hexdigest()
    
    if key == PWDvar.get():
        main()


Root()
