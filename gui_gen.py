from tkinter import *
from tkinter import ttk
from generator import pswd
root = Tk()
frm = ttk.Frame(root, padding=10, border=150)
frm.grid()
ttk.Label(frm, text=f"{pswd}").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()