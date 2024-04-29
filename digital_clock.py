from tkinter import *
from tkinter.ttk import *

from time import strftime


def show_time():
    time = strftime('%H:%M:%S %p')
    label.configure(text=time)
    label.after(1000, show_time)


window = Tk()

label = Label(window, text='', font='Times 40 bold', foreground='white', background='orange')
label.pack(anchor=CENTER)

show_time()

window.mainloop()

