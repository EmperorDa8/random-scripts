from tkinter import *
from tkinter import ttk
from pytube import YouTube
import os


root=Tk()
root.geometry("500x600")
root.configure(bg="black")
root.title("Youtube Downloader")



def download():
    quality = combo1.get()
    
    if quality=="360 MP4":
        URl=YouTube(link.get())
        video=URl.streams.first()
        video.download()
        Label(root,text="download completed",font="arial 22",bg="green",fg="red").place(x=180,y=470)

# icon
icon_image=PhotoImage(file="C:\\Users\\HP\\Downloads\\youtube-logo-png-31812.png")
root.iconphoto(False,icon_image)

# logo 
logo_img=PhotoImage(file="C:\\Users\\HP\\Downloads\\youtube-logo-png-31812.png")
logo_label=Label(root,image=logo_img,background="black").pack(padx=5,pady=5)


labe=Label(root,text="ENTER THE LINK HERE ",font="arial 20 bold").place(x=20,y=250)


link=StringVar()
link_enter=Entry(root,width=14,textvariable=link,font="arial 30").place(x=20,y=310)


#button
dw_btn=Button(root,text="DOWNLOAD",font="arial 25",bg="teal",fg="red",command=download).place(x=130,y=370)
#combbox
option=("240 MP4","360 MP4","720 MP4", "MP3")
combo1=ttk.Combobox(root,values=option,font="Roboto 23 bold",width=7,state="r")
combo1.place(x=340,y=310)
combo1.set("360 MP4")
                                                                        
root.mainloop()