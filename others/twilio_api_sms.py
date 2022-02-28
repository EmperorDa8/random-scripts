import requests
from bs4 import BeautifulSoup
import os
from twilio.rest import Client

headlines=[]

def get_page_job(url):
    rr=requests.get(url)
    res=rr.content
    soup=BeautifulSoup(res, "html.parser") 

    tag=soup.find('td',class_='featured w')
    tag2=tag.find_all("a")
    for i, item in enumerate(tag2):
        try:
            title=item.text
            link=item.attrs['href']
        
        except Exception :
            pass
        
        new=f"{i} :: {title}___{link}"+"<br>"
        headlines.append(new)
    return headlines

get_page_job("https://www.nairaland.com/")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = os.environ['TWILIO_ACCOUNT_SID']="AC99b078101f43726470332cde12c2e89b"
auth_token = os.environ['TWILIO_AUTH_TOKEN']="24f7140adbdd00ad2ff94943be66f637"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body= str(headlines[1]),
                              from_='+19107254583',
                              to='+234 703 482 4573' )

print(message.body)