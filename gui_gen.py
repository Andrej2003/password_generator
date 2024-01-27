from tkinter import *
from tkinter import ttk
from generator import generate


def regenerate_pswd():
    label_pswd['text'] = generate()

    return label_pswd["text"]


def copy_pswd():
    copy_button["command"] = root.clipboard_clear()
    copy_button['command'] = root.clipboard_append(label_pswd['text'])


root = Tk()
root.title("Password Generator")
root.iconbitmap("8726250_padlock_icon.ico")

style = ttk.Style()
style.theme_use("default")
style.configure("TFrame", background="#d8b3fc")
style.configure("W.TLabel", font=("arial", 20))
style.configure("W.TButton", font=("arial", 20),
                foreground="black", background="white", relief="flat", borderwidth=0)
frm = ttk.Frame(root, padding=10, border=250, style="TFrame")
frm.grid()

label_pswd = ttk.Label(
    frm, text=f"{generate()}", style="W.TLabel", background="#d8b3fc")
label_pswd.grid(column=0, row=0, pady=7)

copy_button = ttk.Button(
    frm, text="Copy", command=copy_pswd, style="W.TButton")
copy_button.grid(column=0, row=1, pady=3)
ttk.Button(frm, text="Regenerate", command=regenerate_pswd,
           style="W.TButton").grid(column=0, row=2, pady=3)
ttk.Button(frm, text="Quit", command=root.destroy,
           style="W.TButton").grid(column=0, row=3, pady=3)


root.mainloop()
