import requests
from bs4 import BeautifulSoup
from My_IDs import email_addrs,password,username
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
headlines=[]
now=datetime.datetime.now()
def get_page(url):
    #page+=("<b>NOUN Annoucement:</b>\n"+"<br>"+"-"*10+"br")
    rr=requests.get(url)
    res=rr.content
    soup=BeautifulSoup(res, "html.parser") 
    return soup

def process_page(soup):
    tag=soup.find_all("div", class_="views-row")
    for x in tag:
        name=x.find("span").text
        link=x.find("a")["href"]
        new=f"{name}___https://nou.edu.ng/{link}"
        #concatinate the string on a new line
        headlines.append(new)
    return headlines

z=get_page("https://nou.edu.ng/announcements-view")
process_page(z)

print("composing email....")

#Auntenticate

server="smtp.gmail.com"
port="465"
From=email_addrs
To=email_addrs
Pass=password

# message body

mesg=MIMEMultipart()

mesg["Subject"] = "Automated NOUN Announcements" +str(now.day) + "-" +str(now.month) + "-" +str(now.year)

mesg["From"]=From
mesg["To"]= To

mesg.attach(MIMEText(str(headlines), "html"))
print("initializing server....")

Server=smtplib.SMTP_SSL(host=server,port=port)
Server.set_debuglevel(1)
#Server.starttls()
Server.ehlo()
Server.login(email_addrs,Pass)
Server.sendmail(From, To, mesg.as_string())

print("Email sent!")

Server.quit()