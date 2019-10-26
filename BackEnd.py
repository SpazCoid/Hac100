from newsapi import NewsApiClient
import requests
import json

url = ('https://newsapi.org/v2/top-headlines?'
        
       'q=Lorry&'
       #'sources=bbc-news&'
       'apiKey=009afc89be70404a83dc7b99067d3812')

NewsReturns = requests.get(url).json()


json_status = NewsReturns['status']
print("API STATUS: " + json_status)

jsonList = NewsReturns['articles']
ListLen = len(jsonList)

print(NewsReturns['totalResults'])
print(ListLen)

for i in range(ListLen):
    with open('Hac100/ArticleRecords.json','a') as p:
        json.dump(jsonList[i],p)
        p.write('\n')
    #print("API List: " + str(jsonList[i]))
    print(i)
    i=i+1



