import requests
from bs4 import BeautifulSoup
import json

def getstock_data(symbol):

    headers={"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    url=f"https://finance.yahoo.com/quote/{symbol}"

    rr=requests.get(url, headers=headers)

    soup=BeautifulSoup(rr.text,"html.parser")
    #print(soup.title.text) to get stock webpage title

    # to find tag with stock price element
    stock_data={
    f"{symbol}>>open_price":soup.find("div",{"class":"D(ib) Mend(20px)"}).find_all("span")[0].text,
    f"{symbol}>>changes":soup.find("div",{"class":"D(ib) Mend(20px)"}).find_all("span")[1].text
    }
    return stock_data

# to loop thru list of stock symbol
symb=["BTC-USD","ETH-USD","SHIB-USD","DOGE-USD"]
datastock=[]
for i in symb:
    datastock.append(getstock_data(i))
    print("loading", i)

# to open a new file and write the datastock into json
with open ("stockdata.json","w")as fil:
    json.dump(datastock,fil)
    print("finished")
    
