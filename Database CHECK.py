import sqlite3

conn = sqlite3.connect('UserDB.db')
cursor = conn.execute("SELECT * from Users")

records=cursor.fetchall()

for record in records:
   print("UserID = ", record[0], "Username = ", record[1] , "Pass = ", record[2], "ADD = ", record[3],"POSTC = ", record[4], "PHONUM = ", record[5], "Notif Med = ", record[6], "Notif News = ", record[7])
