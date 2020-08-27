import tkinter as tk
import time

OptionList = [
"Shrek",
"BeeMovie"
] 


app = tk.Tk()

app.geometry('200x300')

variable = tk.StringVar(app)
variable.set(OptionList)

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="Selected item {}".format(variable.get()))

variable.trace("w", callback)

app.mainloop()

while True:
    if variable.get()== "BeeMovie":
        import TextSpammerBeeMovie.py
    else:
        import TextSpammer.py
