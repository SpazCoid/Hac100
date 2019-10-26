import sqlite3

conn = sqlite3.connect("UserDB.db")
c = conn.cursor()
c.execute('''CREATE TABLE if NOT EXISTS Users
    ([username]  VARCHAR(20)   PRIMARY KEY,[pswd]    VARCHAR(20) NOT NULL)''')

