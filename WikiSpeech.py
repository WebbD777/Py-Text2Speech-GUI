# import os
# import sys
import pyttsx3
import wikipedia
import tkinter as tk

from tkinter import filedialog, Text, BOTH, END

search = ""

# import tweepy
#Create an instance of Tkinter frame
win = tk.Tk()
#Set the geometry of Tkinter frame
win.geometry("750x250")


def getSearch():
    global entry

    engine = pyttsx3.init()
    engine.say(wikipedia.summary(entry.get(), sentences=3))
    engine.runAndWait()



#root = tk.Tk()

canvas = tk.Canvas(height=650, width=700, bg="bisque")
canvas.pack(fill= BOTH, expand= True)

label = tk.Label(canvas , text="Search Wikipedia", font=(None, 23))
label.pack(pady=14)

entry = tk.Entry(canvas, width=40)
entry.pack(pady=14)

inputButton = tk.Button(canvas, text="Search", command=getSearch)#, padx=10, pady=5, fg='black', bd='#263D42')
inputButton.pack(pady=14)

print(search)

win.mainloop()
#root.mainloop()


"""
engine = pyttsx3.init()
engine.say(wikipedia.summary("Rohit Sharma", sentences=3))
engine.runAndWait()

engine = pyttsx3.init()
    engine.say(op)
    engine.runAndWait()

# print(wikipedia.summary("Rohit Sharma", sentences=3))
"""
