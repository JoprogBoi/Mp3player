import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

root=Tk()
root.title("Josiah's music player")
root.iconbitmap(r'C:\Users\Dessalegn\Downloads\J image icon.ico')
root.minsize(height=700, width=665)

mixer.init()
#playlist--------------

playlist=Listbox(root, selectmode=SINGLE,bg="DodgerBlue", fg="white", font=('arial' ,15 ),width=60, height=25) #Original width = 40
playlist.grid(columnspan=100) #Original columnspan = 5

os.chdir(r"C:\Users\Dessalegn\music")
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="play", command=playsong)
playbtn.config(font=('arial', 20), bg="DodgerBlue", fg="white", padx=30, pady=30) #Original padx and pady = 7
playbtn.grid(row=1,column=0)
playbtn.place(x=-10, y=600)

pausebtn=Button(root,text="Pause", command=pausesong)
pausebtn.config(font=('arial',20),bg="Dodgerblue2",fg="white", padx=30, pady=30) #Original padx and pady = 7
pausebtn.grid(row=1, column=1)
pausebtn.place(x=123, y=600)

stopbtn=Button(root,text="Stop", command=stopsong)
stopbtn.config(font=('arial',20),bg="Dodgerblue2",fg="white", padx=30, pady=30) #Original padx and pady = 7
stopbtn.grid(row=1, column=2)
stopbtn.place(x=282, y=600)

resumebtn=Button(root,text="Resume", command=resumesong)
resumebtn.config(font=('arial',20),bg="Dodgerblue2",fg="white", padx=65, pady=30) #Original padx and pady = 7
resumebtn.grid(row=1, column=3)
resumebtn.place(x=420, y=600)

mainloop()