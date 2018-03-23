import requests
from bs4 import BeautifulSoup
import json


def getPage(url):
    res = requests.get(url).text
    ##print(res.text)
    soup =  BeautifulSoup(res,"html.parser")


def getInfo(soup):
    contents = soup.select('.r-ent')
    for i in contents:
        dct = {}
        dct["date"] = i.select('div.date')[0].text
        dct["title"] = each_item.select('div.title')[0].text
        dct["author"] = each_item.select('div.author')[0].text

        #get the content base on href
getPage("https://www.ptt.cc/bbs/movie/index.html")
