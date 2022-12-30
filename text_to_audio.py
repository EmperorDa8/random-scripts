from gtts import gTTS
import os

def convert_text_to_audio(textfile):
    with open(textfile)as fil:
        data=fil.read()
    language="en"
    audio=gTTS(text=data,lang=language)
    print("loading")
    audio.save("C:\\Users\\HP\\Documents\\audiotext\\testing.wav")
    os.system("C:\\Users\\HP\\Documents\\audiotext\\testing.wav")
    print("process done")
    return audio
convert_text_to_audio("C:\\Users\\HP\\Documents\\filetest.txt")