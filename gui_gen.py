from tkinter import *
from tkinter import ttk
from generator import pswd

root = Tk()
root.title("Password Generator")
root.iconbitmap("8726250_padlock_icon.ico")

frm = ttk.Frame(root, padding=10, border=150)
frm.grid()

label_style = ttk.Style()
label_style.configure("W.TLabel", font=("arial", 20))
label_pswd = ttk.Label(frm, text=f"{pswd}", style="W.TLabel")
label_pswd.grid(column=0, row=0)

button_style = ttk.Style()
button_style.configure("W.TButton", font=("arial", 20))
ttk.Button(frm, text="Copy", command=root.clipboard_append(pswd), style="W.TButton").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy, style="W.TButton").grid(column=0, row=2)

root.mainloop()
