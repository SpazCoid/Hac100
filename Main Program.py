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

def Timer():
    now=datetime.datetime.now().replace(microsecond=0)
    SpecifiedTime=now.replace(hour=00,minute=10,second=0,microsecond=0)
    if (now == SpecifiedTime):

        message = clockwork.SMS ( to = "07533777040", message = "test")
        response = api.send(message)

        if response.success:
            print (response.id)
        else:
            print (response.error_code)
            print (response.error_description)

            
def NewsSMS():
    conn=sqlite3.connect("News.db")
    cur = conn.cursor()
    cur.execute("SELECT Title, URL FROM News WHERE Sent = ?", [0])
    data=cur.fetchone()

    print(data)

    
    message = clockwork.SMS ( to = "07441906544", message = data[len(data)-1])
    response = api.send(message)

    if response.success:
        print (response.id)
        data[len(data)-1].delete()
    else:
        print (response.error_code)


def NewsSearch():
    url = ('https://newsapi.org/v2/top-headlines?'
        
       
       'q=Drugs&'
       'apiKey=009afc89be70404a83dc7b99067d3812')
    NewsReturns = requests.get(url).json()
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

            conn=sqlite3.connect("News.db")
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
        Timer()
        time.sleep(1)
        ten=ten+1
        five=five+1
        print(ten)
        if (ten == 30):
            NewsSearch()
            ten = 0
        if (five == 15):
            NewsSMS()
            five = 0




clock()
