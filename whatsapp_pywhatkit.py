import pywhatkit
import schedule
import requests
from bs4 import BeautifulSoup
import datetime


date=datetime.datetime.now()

data={}
def scrap_job():
    link="https://www.jumia.com.ng/vodka/"
    rr=requests.get(link)
    s=BeautifulSoup(rr.text, "html.parser")
    things=s.find_all("div",class_="info")
    for items in things:
        name= items.find("h3").text
        prices= items.find("div",class_="prc").text
        data[name]=prices
    return data

scrap_job()
pywhatkit.sendwhatmsg("+2348060495841",str(data),date.hour,date.minute+1)
print("sent!")