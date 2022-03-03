from gtts import gTTS
import os

def convert_text_to_audio(textfile):
    with open("C:\\Users\\USER\\textfolder\\requirements.txt")as fil:
        data=fil.read()
    language="en"
    audio=gTTS(text=data,lang=language)
    print("loading")
    audio.save("C:\\Users\\USER\\others\\testng_audio.wav")
    os.system("others\\testng_audio.wav")
    print("process done")
    