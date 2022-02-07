import threading
import requests
from bs4 import BeautifulSoup
import os
import time

def get_src(url):
    rs=requests.get(url)
    
    ss=BeautifulSoup(rs.text,"html.parser")
    
    imags=ss.find_all("img")
    
    for i in imags:
        time.sleep(1)
        print(i["src"])
        
    
    
def page_links(url):
    rs=requests.get(url)
    ss=BeautifulSoup(rs.text,"html.parser")
    imags=ss.find_all("a")
    links=[]
    for i in imags:
        time.sleep(1)
        print(i["href"])
        
        
links="https://www3.hilton.com/en/hotels/nigeria/transcorp-hilton-abuja-ABUHITW/about/amenities.html"

t1=threading.Thread(target=get_src, args=(links,))
t2=threading.Thread(target=page_links, args=(links,))

t1.start()
t2.start()


t1.join()
t2.join()

print("totally done!")