import ctypes
from tkinter import *
from tkinter import messagebox
from tkinter import Tk
import hashlib
import sqlite3


def Root():
    global root, width, height

#---SETTING UP MAIN WINDOW
    root = Tk()
    root.attributes('-fullscreen', True)
    root.bind('<Escape>',lambda e: root.destroy())
    root.configure(background="#cdfbff")
    StartUp()
    root.mainloop()

def StartUp():

    frameStart = Frame(root)
    frameStart.pack()
    frameStart.configure(background="#cdfbff")
    Label(frameStart, text="COIDWARE",font=("Helvetica 35 bold") , background = "#cdfbff").grid(row=1,column=0, sticky=NSEW)
    #---SPACE
    Label(frameStart, text="\t\t", background="#cdfbff").grid(row=2,column=0,sticky=NSEW )
    Label(frameStart, text="\t\t", background="#cdfbff").grid(row=3,column=0,sticky=NSEW )
    Label(frameStart, text="\t\t", background="#cdfbff").grid(row=4,column=0,sticky=NSEW )

#---CREATING THE BUTTON FRAME FOR THE USER TO USE
    frameButtonS = Frame(root)
    frameButtonS.pack()
    frameButtonS.configure(background="#cdfbff")


#---BUTTON TO REDIRECT USER TO LOGIN SCREEN
    b1 = Button(frameButtonS, height=5, width=16,background="#7f82ff" ,text = "Login", command=lambda: [Login(), frameStart.destroy(), frameButtonS.destroy()]).grid(row=1,column=0)
 
#---SPACE
    Label(frameButtonS, text="\t\t", background="#cdfbff").grid(row=2,column=0,sticky=NSEW)   

#---BUTTON TO REDIRECT USER TO ACCOUNT CREATION
    b2 = Button(frameButtonS,height=5, width=16 ,background="#7f82ff" ,text = "Create New Account", command=lambda: [AccountCreate(), frameStart.destroy(), frameButtonS.destroy()]).grid(row=3,column=0)

#---SPACE
    Label(frameButtonS, text="\t\t", background="#cdfbff").grid(row=4,column=0,sticky=NSEW)

#---BUTTON TO REDIRECT USER TO ACCOUNT CREATION
    b3 = Button(frameButtonS,height=5, width=16 ,background="#7f82ff" ,text = "Quit", command= quit()).grid(row=5,column=0)

def Login():
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

#---PASSWORD ENTRY
    Label(frameLogin, text = "Password", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=4,column=0)
    User_PASSvar = StringVar()
    User_PASS = Entry(frameLogin, textvariable=User_PASSvar, show='*').grid(row=4,column=1)

#---CREATING BUTTONS
    frameButtonL = Frame(root)
    frameButtonL.pack()
    frameButtonL.configure(background="#cdfbff")

    #---SPACE
    Label(frameLogin, text="\t\t", background="#cdfbff").grid(row=5,column=0, )
    
    #7f82ff - Colour for buttons
    b1 = Button(frameButtonL,text="Login",background="#7f82ff").grid(row=1,column=0)
    Label(frameButtonL, text="      ", background="#cdfbff").grid(row=1,column=1)
    b2 = Button(frameButtonL,text="Cancel", background="#7f82ff", command=lambda: [StartUp(), frameLogin.destroy(), frameButtonL.destroy()]).grid(row=1,column=2)

def LoginCheck():

#---GRABS USER AND PASSWORD VARIABLES FROM INPUT BOX
    user = User_IDvar.get()
    pwd = User_PASSvar.get()

#---PASSWORD IS HASHED SO IT CAN BE COMPARED TO ONE IN DATABASE
    key = hashlib.sha256(str(pwd).encode()).hexdigest()
    
    if key == PWDvar.get():
        main()


Root()
