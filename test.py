import ctypes
from tkinter import *
from tkinter import messagebox
from tkinter import Tk
import hashlib
import sqlite3
import os


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

#---CREATING THE MAIN STARTUP FRAME
    frameStart = Frame(root)
    frameStart.pack()
    frameStart.configure(background="#cdfbff")
    Label(frameStart, text="Program Main Screen",font=("Helvetica 35 bold") , background = "#cdfbff").grid(row=1,column=0, sticky=NSEW)
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
    b2 = Button(frameButtonS,height=5, width=16 ,background="#7f82ff" ,text = "Create New Account", command=lambda: [AccCreation(), frameStart.destroy(), frameButtonS.destroy()]).grid(row=3,column=0)

    #---SPACE
    Label(frameButtonS, text="\t\t", background="#cdfbff").grid(row=4,column=0,sticky=NSEW)

    #---BUTTON TO REDIRECT USER TO ACCOUNT CREATION
    b3 = Button(frameButtonS,height=5, width=16 ,background="#7f82ff" ,text = "Quit", command=lambda: [quit()]).grid(row=5,column=0)

def AccCreation():
    global User_NAMEvar, User_PASSvar, User_ADDRvar, User_POSTCvar, User_PHONUMvar
#---Account Creation Frame
    frameAccCreate = Frame(root)
    frameAccCreate.pack()
    frameAccCreate.configure(background="#cdfbff")
    Label(frameAccCreate, text="Account Creation Screen",font=("Helvetica 35 bold") , background = "#cdfbff").grid(row=1,column=0)

#---SPACE
    Label(frameAccCreate, text="\t\t\t\t", background="#cdfbff").grid(row=2,column=0)

#---FRAME FOR THE INPUT SECTION
    frameAccDet = Frame(root)
    frameAccDet.pack()
    frameAccDet.configure(background="#cdfbff")

    #---USERNAME ENTRY
    Label(frameAccDet, text = "Username", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=1, column=0)
    User_NAMEvar = StringVar()
    User_NAME = Entry(frameAccDet, textvariable=User_NAMEvar).grid(row=1,column=1)

    #---PASSWORD ENTRY
    Label(frameAccDet, text = "Password", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=2, column=0)
    User_PASSvar = StringVar()
    User_PASS = Entry(frameAccDet, textvariable=User_PASSvar, show='*').grid(row=2,column=1)

    #---ADDRESS ENTRY
    Label(frameAccDet, text = "Address", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=3, column=0)
    User_ADDRvar = StringVar()
    User_ADDR = Entry(frameAccDet, textvariable=User_ADDRvar).grid(row=3,column=1)

    #---POSTCODE ENTRY
    Label(frameAccDet, text = "Postode", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=4, column=0)
    User_POSTCvar = StringVar()
    User_POSTC = Entry(frameAccDet, textvariable=User_POSTCvar).grid(row=4,column=1)

    #---PHONE NUMBER ENTRY
    Label(frameAccDet, text = "Phone Number", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=5, column=0)    
    User_PHONUMvar = StringVar()
    User_PHONUM = Entry(frameAccDet, textvariable=User_PHONUMvar).grid(row=5,column=1)

#---CREATING THE BUTTON FRAME FOR THE USER TO USE
    frameButtonAC = Frame(root)
    frameButtonAC.pack()
    frameButtonAC.configure(background="#cdfbff")

    #---ADD ACCOUNT TO DATABASE
    b1 = Button(frameButtonAC, height=5, width=16,background="#7f82ff" ,text = "Create Account", command=lambda: [AddNewAcc(), frameAccDet.destroy(), frameButtonAC.destroy()]).grid(row=1,column=0)
 
def AddNewAcc():
    user = User_NAMEvar.get()
    pwd = User_PASSvar.get()
    addr = User_ADDRvar.get()
    postc = User_POSTCvar.get()
    phonum = User_PHONUMvar.get()

    user_hash = hashlib.sha256(str(user).encode()).hexdigest()
    user_id = user_hash[:8]
    user_pwd = hashlib.sha256(str(pwd).encode()).hexdigest()

    conn = sqlite3.connect("UserDB.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users VALUES (?,?,?,?,?,?)", (user_id,user,user_pwd,addr,postc,phonum))
    conn.commit()
    conn.close()
    Login()


def Login():
    global User_NAMEvar, User_PASSvar, frameLogin, frameLoginButtons

#---MAIN LOGIN FRAME
    frameLogin = Frame(root)
    frameLogin.pack()
    frameLogin.configure(background="#cdfbff")
    Label(frameLogin, text="User Login Screen",font=("Helvetica 35 bold") , background = "#cdfbff").grid(row=1,column=0)

#---SPACE
    Label(frameLogin, text="\t\t", background="#cdfbff").grid(row=2,column=0, )

#---USERNAME ENTRY
    Label(frameLogin, text = "Username", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=3, column=0)
    User_NAMEvar = StringVar()
    User_NAME = Entry(frameLogin, textvariable=User_NAMEvar).grid(row=3,column=1)

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
    global User_IDvar 
#---GRABS USER AND PASSWORD VARIABLES FROM INPUT BOX
    user = User_NAMEvar.get()
    pwd = User_PASSvar.get()

#---GRAB DETAILS FROM THE DATABASE
    conn = sqlite3.connect("UserDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT userpass FROM Users WHERE username=?", (user))


#---PASSWORD IS HASHED SO IT CAN BE COMPARED TO ONE IN DATABASE
    key = hashlib.sha256(str(pwd).encode()).hexdigest()
    
    if key == PWDvar.get():

        main()


Root()
