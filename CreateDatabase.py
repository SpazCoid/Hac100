import sqlite3
def test():

    conn = sqlite3.connect("UserDB.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE if NOT EXISTS Users
        ([userid]  VARCHAR(8)   PRIMARY KEY,[username] VARCHAR(20) NOT NULL,[userpass]    VARCHAR(64) NOT NULL,[Address] VARCHAR(64) NOT NULL,[Postcode] VARCHAR(8) NOT NULL,[PhoneNum] INT(11) NOT NULL)''')

test()