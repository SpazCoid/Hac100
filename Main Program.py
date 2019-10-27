from newsapi import NewsApiClient
import requests
import json
import datetime
import sqlite3
import schedule
import time
import datetime
from clockwork import clockwork
api = clockwork.API("363f27ed4ba0582e3aae07c8e951a88febe5dda2")

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
def NewsSMS(msg):

    
    message = clockwork.SMS( to ="07533777040",message = msg)
    response = api.send(message)

    if response.success:
        print (response.id)
    else:
        print (response.error_code)
        print (response.error_description)


def NewsSearch():
    url = ('https://newsapi.org/v2/top-headlines?'
        
       
       'q=Brexit&'
       'apiKey=009afc89be70404a83dc7b99067d3812')
    NewsReturns = requests.get(url).json()
    json_status = NewsReturns['status']
    jsonList = NewsReturns['articles']
    ListLen = len(jsonList)
    
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
                    Text = str(jsonList[i]['title']+ " / " + jsonList[i]['url'])
                    cursor = conn.cursor()
                    cursor.execute("INSERT OR IGNORE INTO News Values (?,?,?,?,?)" , (jsonList[i]['title'],jsonList[i]['description'],jsonList[i]['url'],jsonList[i]['publishedAt'],jsonList[i]['content']))
                    conn.commit()
                    #print("Article Saved") 
                    
                else:
                    #print("News Search ran, however there has been no new news for the targeted search")
                    break
                i=i+1        
            conn.close()
            

            
            
            
            
            
        
    return

def clock():
    starttime=time.time()
    ten=0
    while True:
        Timer()
        time.sleep(1)
        ten=ten+1
        print(ten)
        if (ten == 5):
            NewsSearch()
            ten = 0




clock()
