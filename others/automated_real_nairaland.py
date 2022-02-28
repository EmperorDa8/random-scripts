import schedule
import requests
from bs4 import BeautifulSoup
from My_IDs import email_addrs,password,username
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

now=datetime.datetime.now()
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



def send_email():
    get_page_job("https://www.nairaland.com/")
    time.sleep(8)
    print("composing email....")
    
    #Auntenticate
    server="smtp.gmail.com"
    port="465"
    From=email_addrs
    To=email_addrs
    Pass=password
    
    # message body
    
    mesg=MIMEMultipart()
    
    mesg["Subject"] = "Automated Nairaland news" +str(now.day) + "-" +str(now.month) + "-" +str(now.year)
    
    mesg["From"]=From
    mesg["To"]= To
    
    mesg.attach(MIMEText(str(headlines), "html"))
    print("initializing server....")
    
    Server=smtplib.SMTP_SSL(host=server,port=port)
    Server.set_debuglevel(1)
    Server.ehlo()
    Server.login(email_addrs,Pass)
    Server.sendmail(From, To, mesg.as_string())
    
    print("Email sent!")
    
    Server.quit()
    
    
schedule.every(24).hours.do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)


