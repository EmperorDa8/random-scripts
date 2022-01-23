import requests
from bs4 import BeautifulSoup
import os


url="https://www3.hilton.com/en/hotels/nigeria/transcorp-hilton-abuja-ABUHITW/about/amenities.html"
rs=requests.get(url)

ss=BeautifulSoup(rs.text,"html.parser")

imags=ss.find_all("img")

for i in imags:
    print(i["src"])