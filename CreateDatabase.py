import sqlite3
def test():

    conn = sqlite3.connect("UserDB.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE if NOT EXISTS Users
        ([username]  VARCHAR(20)   PRIMARY KEY,[userpass]    VARCHAR(64) NOT NULL,[Address] VARCHAR(64) NOT NULL,[Postcode] VARCHAR(8) NOT NULL,[PhoneNum] INT(11) NOT NULL)''')

test()