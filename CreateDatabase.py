import sqlite3
def test():

    conn = sqlite3.connect("UserDB.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE if NOT EXISTS Users
        ([UserID]  VARCHAR(8)   NOT NULL,[Username] VARCHAR(20) NOT NULL,[UserPass]    VARCHAR(64) NOT NULL,[Address] VARCHAR(64) NOT NULL,[Postcode] VARCHAR(8) NOT NULL,[PhoneNum] INT(11) NOT NULL,[NotifMed] BOOLEAN(1) NOT NULL,[NotifNews] BOOLEAN(1) NOT NULL, PRIMARY KEY(UserID))''')
    cursor.execute('''CREATE TABLE if NOT EXISTS Medication
        ([MedID] VARCHAR(8) NOT NULL,[MedicationName] VARCHAR(20) NOT NULL,[MedicationDesc] VARCHAR(64) NOT NULL,[MedicationDose] VARCHAR(20) NOT NULL, PRIMARY KEY(MedID) )''')
    
    cursor.execute('''CREATE TABLE if NOT EXISTS Link
        ([UserID] VARCHAR(8) NOT NULL,[MedID] VARCHAR(8) NOT NULL,[TimeMedHour] VARCHAR(2) NOT NULL,[TimeMedMin] VARCHAR(2) NOT NULL, FOREIGN KEY(UserID) REFERENCES Users(UserID), FOREIGN KEY(MedID) REFERENCES Medication(MedID) )''')
    

    conn.execute('''Create Table IF NOT EXISTS News
             (Title                     TEXT  (50) NOT NULL,
              Description               TEXT (50)            NOT NULL,
              URL                       TEXT (50)           NOT NULL,
              publishedAt               TEXT (15)           NOT NULL,
              Content                   TEXT (500)           NOT NULL,
              Sent                      Boolean(1)           NOT NULL,
              PRIMARY KEY (Title)
              UNIQUE(Title,URL)
              );''')



    #cursor.execute("INSERT OR IGNORE INTO Users Values (?,?,?,?,?,?,?,?)" , ('Test1234','TestAccount1234','d519397a4e89a7a66d28a266ed00a679bdee93fddec9ebba7d01ff27c39c1a99','TestAddress123', 'TestPostcode123', "07533777040", '1' , '1' ))
    #cursor.execute("INSERT OR IGNORE INTO Users Values (?,?,?,?,?,?,?,?)" , ('Test5678','TestAccount5678','1a77bb65d1d544957d895bde9602a4a42712a33335ae897a712d068fef6fb9a8','TestAddress567', 'TestPostcode567', "07421749700", '1' , '1' ))
    cursor.execute("INSERT OR IGNORE INTO Medication Values (?,?,?,?)" , ('DRUG0001','Paracetamol','Painkiller','500' ))
    cursor.execute("INSERT OR IGNORE INTO Medication Values (?,?,?,?)" , ('DRUG0002','Asprin','Painkiller','250' ))
    cursor.execute("INSERT OR IGNORE INTO Link Values (?,?,?,?)" , ('user1','DRUG0001','09','00' ))
    cursor.execute("INSERT OR IGNORE INTO Link Values (?,?,?,?)" , ('user1','DRUG0002','09','01' ))
    cursor.execute("INSERT OR IGNORE INTO Link Values (?,?,?,?)" , ('user2','DRUG0001','08','59' ))
    cursor.execute("INSERT OR IGNORE INTO Link Values (?,?,?,?)" , ('user2','DRUG0002','09','02' ))
    conn.commit()
    conn.close()

test()
