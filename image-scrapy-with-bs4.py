import os,requests
from bs4 import BeautifulSoup

#urls="https://www.airbnb.com/scarborough-united-kingdom/stays"

def imageodownloader(url,folder):
    # to get create directory using os module
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    rr= requests.get(url)
    soup=BeautifulSoup(rr.text,"html.parser")

    imgs=soup.find_all("img")

    for i in imgs:
        linkname=i["alt"]
        link=i["src"]
        with open (linkname+".jpg","wb")as fi:
            ser=requests.get(link)
            fi.write(ser.content)
            print("downloading"+ linkname)
            
imageodownloader("https://www.airbnb.com/scarborough-united-kingdom/stays","travel")
