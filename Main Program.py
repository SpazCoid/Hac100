from newsapi import NewsApiClient
import requests
import json
import datetime
import schedule
import time
import datetime
from clockwork import clockwork
api = clockwork.API("363f27ed4ba0582e3aae07c8e951a88febe5dda2")

def Timer():
    now=datetime.datetime.now().replace(microsecond=0)
    SpecifiedTime=now.replace(hour=00,minute=10,second=0,microsecond=0)
    print(now)
    print(SpecifiedTime)
    if (now == SpecifiedTime):

        message = clockwork.SMS ( to = "07533777040", message = "test")
        response = api.send(message)

        if response.success:
            print (response.id)
        else:
            print (response.error_code)
            print (response.error_description)

def clock():
    starttime=time.time()
    while True:
        print ("tick")
        Timer()
        time.sleep(1)

def NewsSearch():
    url = ('https://newsapi.org/v2/top-headlines?'
        
       'q=Lorry&'
       'sources=bbc-news&'
       'apiKey=009afc89be70404a83dc7b99067d3812')
    NewsReturns = requests.get(url).json()
    json_status = NewsReturns['status']
    jsonList = NewsReturns['articles']
    ListLen = len(jsonList)
    
    if json_status == 'ok':
        for i in range(ListLen)
        
        
    return

clock()
