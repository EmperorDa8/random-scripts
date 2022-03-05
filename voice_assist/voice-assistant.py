import datetime
from gtts import gTTS
import playsound
import speech_recognition as srr
import subprocess
import time
import os
from mylink import my_mail_url


def speak(texts):
    tet=gTTS(text=texts, lang="en")
    filename="5voice.mp3"
    tet.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    

def sp_audio():
    data=srr.Recognizer()
    with srr.Microphone() as source:
        aud=data.listen(source)
        said=" "
        
        try:
            said=data.recognize_google(aud)
            print(said)
        except Exception :
            print("please speak clearly!")
    return said.lower()
            

def note(text):
    date=datetime.datetime.now()
    file_name= str(date).replace(":","-")+"-textnote.txt"
    with open(file_name,"w")as fil:
        fil.write(text)
    browser="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"   
    subprocess.Popen(["notepad.exe",file_name])
    return

def open_browser():
    browser="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"  
    subprocess.Popen([browser,"www.youtube.com"])
    return

def open_gmail():
    browser="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" 
    subprocess.Popen([browser,my_mail_url])
    return

wake="risa"    
while True:

    text_d= sp_audio()
    if text_d.count(wake)>0:
        speak("please, give command?")
        text_d= sp_audio()
        
        notes_strs=["take this down","keep this","record text"]
        for phrase in notes_strs:
            if phrase in text_d:
                speak("what do you want write?")
                comm=sp_audio()
                note(comm)
                speak("command done")
        
        if "browser" in text_d:
            speak("should i open browser, yes or no!")
            time.sleep(2)
            cmd_text=sp_audio()
            if "yes" in cmd_text:
                open_browser()
                speak("process executed")
        
        if "gmail" in text_d:
            speak("should i open your gmail!, yes or no")
            time.sleep(2)
            cmd_text=sp_audio()
            if "yes" in cmd_text:
                open_gmail()
                speak("process executed")  
                
    if "stop" in text_d:
        break
            
