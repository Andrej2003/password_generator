from tkinter import *
from tkinter import ttk
from generator import pswd
root = Tk()
frm = ttk.Frame(root, padding=10, border=150)
frm.grid()
text = ttk.Label(frm, text=f"{pswd}").grid(column=0, row=0)
ttk.Button(frm, text="Copy", command=root.clipboard_append(pswd)).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
root.mainloop()
