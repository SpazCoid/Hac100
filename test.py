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
    buttn1 = Button(frameButtonS, height=5, width=16,background="#7f82ff" ,text = "Login", command=lambda: [Login(), frameStart.destroy(), frameButtonS.destroy()]).grid(row=1,column=0)
 
    #---SPACE
    Label(frameButtonS, text="\t\t", background="#cdfbff").grid(row=2,column=0,sticky=NSEW)   

    #---BUTTON TO REDIRECT USER TO ACCOUNT CREATION
    buttn2 = Button(frameButtonS,height=5, width=16 ,background="#7f82ff" ,text = "Create New Account", command=lambda: [AccCreation(), frameStart.destroy(), frameButtonS.destroy()]).grid(row=3,column=0)

    #---SPACE
    Label(frameButtonS, text="\t\t", background="#cdfbff").grid(row=4,column=0,sticky=NSEW)

    #---BUTTON TO REDIRECT USER TO ACCOUNT CREATION
    buttn3 = Button(frameButtonS,height=5, width=16 ,background="#7f82ff" ,text = "Quit", command=lambda: [quit()]).grid(row=5,column=0)

def AccCreation():
    global User_NAMEvar, User_PASSvar, User_ADDRvar, User_POSTCvar, User_PHONUMvar, User_NOTIFMEDvar, User_NOTIFNEWSvar
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

#---MEDICATION SMS NOTIFICATION SETTING
    Label(frameAccDet, text = "Medication SMS Notifications (check to turn on)", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=6, column=0)    
    User_NOTIFMEDvar = IntVar()
    User_NOTIFMED = Checkbutton(frameAccDet,onvalue=1, offvalue=0, var=User_NOTIFMEDvar).grid(row=6,column=1)

#---NEWS SMS NOTIFICATION SETTING
    Label(frameAccDet, text = "News SMS Notifications (check to turn on)", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=7, column=0)    
    User_NOTIFNEWSvar = IntVar()
    User_NOTIFNEWS = Checkbutton(frameAccDet,onvalue=1, offvalue=0, var=User_NOTIFNEWSvar).grid(row=7,column=1)

#---CREATING THE BUTTON FRAME FOR THE USER TO USE
    frameButtonAC = Frame(root)
    frameButtonAC.pack()
    frameButtonAC.configure(background="#cdfbff")

    #---ADD ACCOUNT TO DATABASE
    buttn1 = Button(frameButtonAC, height=5, width=16,background="#7f82ff" ,text = "Create Account", command=lambda: [AddNewAcc(), frameAccDet.destroy(),frameAccCreate.destroy(), frameButtonAC.destroy()]).grid(row=1,column=0)
 
def AddNewAcc():
    user = User_NAMEvar.get()
    pwd = User_PASSvar.get()
    addr = User_ADDRvar.get()
    postc = User_POSTCvar.get()
    phonum = User_PHONUMvar.get()
    notifm = User_NOTIFMEDvar.get()
    notifn = User_NOTIFNEWSvar.get()

    user_hash = hashlib.sha256(str(user).encode()).hexdigest()
    user_id = user_hash[:8]
    user_pwd = hashlib.sha256(str(pwd).encode()).hexdigest()

#---CREATING ACCOUNT ACCESS FRAME
    user = user_LoggedInvar.get(pwd).encode().hexdigest()

    conn = sqlite3.connect("UserDB.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users VALUES (?,?,?,?,?,?,?,?)", (user_id,user,user_pwd,addr,postc,phonum,notifm,notifn))
    conn.commit()
    conn.close()
    Login()

def AccountAccessMain():
    user = userID
    LoggedIn = user_LoggedInvar
    LogVar = ("Currently Logged in as:", LoggedIn)
#---CREATING ACCOUNT ACCESS FRAME
    frameAccMenu = Frame(root)
    frameAccMenu.pack()
    frameAccMenu.configure(background="#cdfbff")
    Label(frameAccMenu, text=LogVar,font=("Helvetica 35 bold") , background = "#cdfbff").grid(row=1,column=0, sticky=NSEW)
#---SPACE
    Label(frameAccMenu, text="\t\t", background="#cdfbff").grid(row=2,column=0,sticky=NSEW )
    Label(frameAccMenu, text="\t\t", background="#cdfbff").grid(row=3,column=0,sticky=NSEW )
    Label(frameAccMenu, text="\t\t", background="#cdfbff").grid(row=4,column=0,sticky=NSEW )

#---CREATING THE BUTTON FRAME FOR THE USER TO USE
    frameButtonAS = Frame(root)
    frameButtonAS.pack()
    frameButtonAS.configure(background="#cdfbff")

    #---BUTTON TO REDIRECT USER TO MEDICATION ENTRY SCREEN
    buttn1 = Button(frameButtonAS, height=5, width=16,background="#7f82ff" ,text = "Medication Menu", command=lambda: [frameAccMenu.destroy(), frameButtonAS.destroy(), MedMenu()]).grid(row=1,column=0)
 
    #---SPACE
    Label(frameButtonAS, text="\t\t", background="#cdfbff").grid(row=2,column=0,sticky=NSEW)   

    #---BUTTON TO REDIRECT USER TO ACCOUNT CREATION
    buttn2 = Button(frameButtonAS,height=5, width=16 ,background="#7f82ff" ,text = "Notifications", command=lambda: [NotifToggle(), frameAccMenu.destroy(), frameButtonAS.destroy()]).grid(row=3,column=0)

    #---SPACE
    Label(frameButtonAS, text="\t\t", background="#cdfbff").grid(row=4,column=0,sticky=NSEW)

    #---BUTTON TO REDIRECT USER TO ACCOUNT CREATION
    buttn3 = Button(frameButtonAS,height=5, width=16 ,background="#7f82ff" ,text = "Log Out", command=lambda: [StartUp(), frameAccMenu.destroy(), frameButtonAS.destroy()]).grid(row=5,column=0)

def MedMenu():
    user = userID
    frameMedMenu = Frame(root)
    frameMedMenu.pack()
    frameMedMenu.configure(background="#cdfbff")
    Label(frameMedMenu, text="User Medication Menu",font=("Helvetica 35 bold") , background = "#cdfbff").grid(row=1,column=0, sticky=NSEW)

#---SPACE
    Label(frameMedMenu, text="\t\t\t\t", background="#cdfbff").grid(row=2,column=0)

#---DATA ENTRY
    #---MEDICATION ID ENTRY
    Label(frameMedMenu, text = "Medication ID", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=3, column=0)
    MedIDvar = StringVar()
    MedID = Entry(frameMedMenu, textvariable=MedIDvar).grid(row=3,column=1)

    #---MEDICATION NAME ENTRY
    Label(frameMedMenu, text = "Medication Name", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=4, column=0)
    MedNamevar = StringVar()
    MedName = Entry(frameMedMenu, textvariable=MedNamevar).grid(row=4,column=1)

    #---MEDICATION DESCRIPTION ENTRY
    Label(frameMedMenu, text = "Medication Description", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=5, column=0)
    MedDescvar = StringVar()
    MedDesc = Entry(frameMedMenu, textvariable=MedDescvar).grid(row=5,column=1)

    #---MEDICATION DOSE ENTRY
    Label(frameMedMenu, text = "Medication Dose", font=("Helvetica 15 bold"), background="#cdfbff").grid(row=6, column=0)
    MedDosevar = StringVar()
    MedDose = Entry(frameMedMenu, textvariable=MedDosevar).grid(row=6,column=1)
    
    i = 1
    conn=sqlite3.connect("UserDB.db")
    cur = conn.cursor()
    cur.execute("SELECT Medication.MedID, Medication.MedicationName, Medication.MedicationDesc , Medication.MedicationDose FROM Link, Medication WHERE Link.UserID = (?) AND Medication.MedID = Link.MedID", (user,))
    records=cur.fetchall()
    for record in records:

        listbox.insert(i,"Medication ID = ", record[0] , "Medication Name = ", record[1] , "Medication Description = ", record[2] , "Medication Dose = ", record[3])
        listbox.insert(i,"----------------------------------------------------------", "\n\n")
 
    listbox = Listbox(frameMedMenu, height=8, width=80).grid(row=7,column=0)

    i += 1


def Login():
    global User_NAMEvar, User_PASSvar, frameLogin, frameButtonL, userID

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
    buttn1 = Button(frameButtonL,text="Login",background="#7f82ff", command=lambda: [LoginCheck(), frameLogin.destroy(), frameButtonL.destroy()]).grid(row=1,column=0)
    Label(frameButtonL, text="      ", background="#cdfbff").grid(row=1,column=1)
    buttn2 = Button(frameButtonL,text="Cancel", background="#7f82ff", command=lambda: [StartUp(), frameLogin.destroy(), frameButtonL.destroy()]).grid(row=1,column=2)
    
def LoginCheck():
    global userID, user_LoggedInvar, frameLogin, frameButtonL
#---GRABS USER AND PASSWORD VARIABLES FROM INPUT BOX
    user = User_NAMEvar.get()
    pwd = User_PASSvar.get()

    print(user)
    print(pwd)

#---PASSWORD IS HASHED SO IT CAN BE COMPARED TO ONE IN DATABASE
    key = hashlib.sha256(str(pwd).encode()).hexdigest()

#---GRAB DETAILS FROM THE DATABASE
    conn = sqlite3.connect("UserDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT UserID, Username, UserPass FROM Users where Username=(?)", (user,))
    records = cursor.fetchall()

    for record in records:
        if key == record[2]:
            userID = record[0]
            MedIDvar = record[0]
            user_LoggedInvar = user
            print(userID)
            print(user_LoggedInvar)
            frameLogin.destroy(), frameButtonL.destroy(); AccountAccessMain()
        else:
            messagebox.showerror("Error", "Username / Password is incorrect")

Root()
