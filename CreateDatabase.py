import sqlite3
def test():

    conn = sqlite3.connect("UserDB.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE if NOT EXISTS Users
        ([UserID]  VARCHAR(8)   NOT NULL,[Username] VARCHAR(20) NOT NULL,[UserPass]    VARCHAR(64) NOT NULL,[Address] VARCHAR(64) NOT NULL,[Postcode] VARCHAR(8) NOT NULL,[PhoneNum] INT(11) NOT NULL, PRIMARY KEY(UserID))''')

    cursor.execute('''CREATE TABLE if NOT EXISTS Medication
        ([MedID] VARCHAR(8) NOT NULL,[MedicationName] VARCHAR(20) NOT NULL,[MedicationDesc] VARCHAR(64) NOT NULL,[MedicationDose] VARCHAR(20) NOT NULL, PRIMARY KEY(MedID) )''')

    cursor.execute('''CREATE TABLE if NOT EXISTS Link
        ([UserID] VARCHAR(8) NOT NULL,[MedID] VARCHAR(8) NOT NULL,[TimeMed] VARCHAR(10) NOT NULL, FOREIGN KEY(UserID) REFERENCES Users(UserID), FOREIGN KEY(MedID) REFERENCES Medication(MedID) )''')

    conn.close()

test()
