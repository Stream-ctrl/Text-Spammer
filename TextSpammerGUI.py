from tkinter import *

master = Tk()

master.geometry('200x100')

def callback():
    import Choose.py
    
b = Button(master, text="Start spamming", command=callback)
b.pack(side="left")

mainloop()
