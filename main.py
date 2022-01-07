from tkinter import *
from pygame import *
import os
from PIL import ImageTk, Image
import stagger
import io
import eyed3
import os,sys
from io import BytesIO
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image
import cv2




m=Tk()
m.title("music player")
m.geometry('1000x600')
l = Label(m, text = "MY MUSICPLAYER")
l.config(font=("Courier", 44))
mixer.init()
songsframe = LabelFrame(text="Song Playlist",font=("times new roman",15,"bold"),bg="pink",fg="white",bd=5,relief=GROOVE)
songsframe.place(x=600,y=70,width=400,height=500)
scrol_y = Scrollbar(songsframe,orient=VERTICAL)
playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",bg="white",fg="green",height=500,relief=GROOVE)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)
os.chdir("C://Users//Aman gautam//PycharmProjects//pythonProject//songs")
songtracks = os.listdir()

my_var = StringVar()
my_var.set("")
t = Label(m, textvariable=my_var)
t.place(x=200, y=200)

label = Label(m)
# label.grid(row=0, column=0)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

for track in songtracks:
    playlist.insert(END,track)
def play():
    mixer.music.load(playlist.get(ACTIVE))
    mp3 = stagger.read_tag(playlist.get(ACTIVE))
    my_var.set(mp3.artist)

    t.pack()
    track = MP3(playlist.get(ACTIVE))
    tags = ID3(playlist.get(ACTIVE))
    pict = tags.get("APIC:").data
    im = Image.open(BytesIO(pict))

    test = ImageTk.PhotoImage(im)


    label1 = Label(image=test)
    label1.image = test
    #bg = PhotoImage(file=label1)
    # Position image
    label1.place(x= 200, y = 200,height=200,width=300)





    mixer.music.play()

# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

def hand():
    hand_cascade = cv2.CascadeClassifier('C://Users//Aman gautam//PycharmProjects//pythonProject//palm.xml')
    show_frames()


def pause():

    mixer.music.pause()
def resume():
    mixer.music.unpause()
def stop():
    #t.after(1000, t.destroy())
    my_var.set("")
    mixer.music.stop()
mixer.music.set_volume(0.7)
B = Button(text="play", command=play,width=15,height=2)
B.place(x=25, y=200)
B1 = Button(text="pause", command=pause,width=15,height=2)
B1.place(x=25, y=300)
B2 = Button(text="resume", command=resume,width=15,height=2)
B2.place(x=25,y=400)
B3 = Button(text="stop", command=stop,width=15,height=2)
B3.place(x=25, y=500)
B4=Button(text="hand gesture mode", command=hand,width=15,height=2)
B4.place(x=400, y=400)

l.pack()
m.mainloop()