#Name : Tasha Margie Musau
#Date : 24/02/2026

#Program to show tkinter

from tkinter import *

def hello():
    print("Hello from Bob")

root = Tk()
root.geometry("600x600")

frame_one = Frame(root)
frame_one.pack()

button_one = Button(frame_one,text = "Say Hello",command = hello)
button_one.pack()


root.mainloop()