from tkinter import *
from tkinter import ttk

win = Tk()
win.title("My Weather App")
win.config(bg="blue")
win.geometry("500x500")

name = Label(text="Weather App", font=("Times New Roman", 30, "bold"))
name.place(x=25, y=50, height=50, width=450)

win.mainloop()
