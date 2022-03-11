import requests
from bs4 import BeautifulSoup
import os

# exception handling in sys argv

save_path=r"C:\Users\USER\mp3_folder"
page="https://justnaija.com/music/artistes/joeboy-ng/"
rr=requests.get(page)

soup=BeautifulSoup(rr.content,"html5lib")
item=soup.findAll("div", class_="mu-o-unit-c")
if len(item) >0:
    for it in item:
        sav=it.find("a")["href"]
        name=it.find("a").text
        print(f"downloading..{name}..{sav}")
        paths=os.path.join(save_path, name+".mp3")    
        with open(paths, "wb") as fil:
            fil.write(requests.get(sav).content)
    print("process done")               
else:
    print("not found")
    
