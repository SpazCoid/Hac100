from newsapi import NewsApiClient
import requests
import json
import datetime
import sqlite3
import schedule
import time
import datetime
from clockwork import clockwork
api = clockwork.API("366aec027c364b3314327812f33da2557d51a731")

def NewTimer():#Sends SMS related to Perscription
    conn=sqlite3.connect("UserDB.db")
    cur = conn.cursor()
    cur.execute("SELECT Users.PhoneNum, Link.TimeMedHour, Link.TimeMedMin , Medication.MedicationName , Link.AmountLeft,Link.UserID FROM Users,Link,Medication WHERE NotifMed = ? AND Users.UserID = Link.UserID AND Medication.MedID = Link.MedID", [1])
    #Pulling the PhoneNumber for a User aswell as the Time they need to take their medication, the name of the medication and the amount of medication they have left.
    data=cur.fetchall()
    datalen=len(data)
    j=0
    #iterate through the array of phonenumbers from the database that have opped into the service
    for j in range(datalen):
        now=datetime.datetime.now().replace(microsecond=0)
        #defining vars for function
        PHONENUMBER=data[j][0]
        HOUR=data[j][1]
        MIN=data[j][2]
        MED=data[j][3]
        AmountLeft=data[j][4]
        UserID=data[j][5]
        #Translating the time in the database to a version that is readable by the computer
        SpecifiedTime=now.replace(hour=int(HOUR),minute=int(MIN),second=0,microsecond=0)
        NewAmountLeft=0
        #checks to see if the current system time is the same as the time required for the perscription
        if(now == SpecifiedTime):
            #checks to see if there is medication availible to be taken
            if(AmountLeft>0):
                #Checks to see if there is more than or less than 5 medication left
                if(AmountLeft>0 and AmountLeft <= 5): 
                    NewAmountLeft= AmountLeft-1
                    reminder = str("Its Time to take your medication of " + MED + ". You now have " + str(NewAmountLeft) + " Medication Left. This Means you need to top up ASAP before they run out.")
                if(AmountLeft>5):
                    NewAmountLeft= AmountLeft-1
                    reminder = str("Its Time to take your medication of " + MED + ". You now have " + str(NewAmountLeft) + " Medication Left.")
                #sends the message to the user
                message = clockwork.SMS(to=PHONENUMBER, message = reminder)
                #gathers the response
                response = api.send(message)

                #check to see if the msg was delivered or not
                if response.success:
                    print ("responseID" + response.id)
                    #print("Amount left before taking pill " + str(AmountLeft))
                    #updates the database with the new value of the Medication
                    cur.execute("UPDATE Link SET AmountLeft = ? WHERE UserID = ? AND TimeMedHour = ? AND TimeMedMin = ?",(NewAmountLeft,UserID,HOUR,MIN))
                    
                    #print("New amount of pills left " + str(NewAmountLeft))
                else:
                    
                    print("responseErrorCODE" + response.error_code)
                conn.commit()
            #If there is no Medication left then we fall into this statment which will inform the user that there is no more medication
            else:
                #sends msg to user
                message = clockwork.SMS(to=PHONENUMBER, message = "WARNING! THERE IS NO MORE OF YOUR MEDICATION " + MED )
                response = api.send(message)
                #gathers response
                if response.success:
                    print ("responseID" + response.id)
                else:
                    print("responseErrorCODE" + response.error_code)
    cur.close()


def NewNewsSMS():
    conn=sqlite3.connect("UserDB.db")
    cur = conn.cursor()
    cur.execute("SELECT PhoneNum FROM Users WHERE NotifMed = ?", [1])
    phn =cur.fetchall()
    cur.execute("SELECT Title, URL, Sent FROM News WHERE Sent = ?",[0])
    nws = cur.fetchall()
    phnlen=len(phn)
    nwslen=len(nws)
    j=0
    l=0
    #iterate through the array of phonenumbers from the database that have opped into the service
    for j in range(phnlen):
        for l in range(nwslen):
            PHONENUMBER = phn[j][0]
            TITLE = nws[l][0]
            URL = nws[l][1]
            BODY = str(TITLE + " / " + URL)
            message = clockwork.SMS(to = PHONENUMBER , message = TITLE)
            response = api.send(message)
            if response.success:
                print ("responseID" + response.id)
                cur.execute("UPDATE News SET Sent = ? WHERE URL = ?",("1",URL))
                print("Sent")

            else:
                print("responseErrorCODE" + response.error_code)
            conn.commit()
    cur.close()

def NewsSearch():
    url = ('https://newsapi.org/v2/top-headlines?'
        
       'category = general&'
       'q=Manchester&'
       'apiKey=009afc89be70404a83dc7b99067d3812')
    NewsReturns = requests.get(url).json()
    print(NewsReturns)
    json_status = NewsReturns['status']
    jsonList = NewsReturns['articles']
    ListLen = len(jsonList)
    TextList = []
    if json_status == 'ok':
        i=0
        for i in range(ListLen):
            Title = jsonList[i]['title']
            Description = jsonList[i]['description']
            URL = jsonList[i]['url']
            publishedAt = jsonList[i]['publishedAt']
            Content = jsonList[i]['content']

            conn=sqlite3.connect("UserDB.db")
            cur = conn.cursor()
            for Title in (jsonList):
                cur.execute("SELECT count (*) FROM News WHERE Title = ?", [jsonList[i]['title']])
                data=cur.fetchone()
                if data[0] ==0:
                    cursor = conn.cursor()
                    cursor.execute("INSERT OR IGNORE INTO News Values (?,?,?,?,?,?)" , (jsonList[i]['title'],jsonList[i]['description'],jsonList[i]['url'],jsonList[i]['publishedAt'],jsonList[i]['content'],0))
                    conn.commit()
                    #print("Article Saved") 
                    
                else:
                    #print("News Search ran, however there has been no new news for the targeted search")
                    break
                i=i+1        
            conn.close()
            

            
            
            
            
           
        
    return

def clock():
    ten=0
    five = 0
    while True:
        NewTimer()
        time.sleep(1)
        ten=ten+1
        five=five+1
        print(ten)
        if (ten == 30):
            NewsSearch()
            ten = 0
        if (five == 15):
            NewNewsSMS()
            five = 0




clock()
