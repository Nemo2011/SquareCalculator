import tkinter
from tkinter import ttk
import pyperclip

def set_(self):
    root = tkinter.Tk()
    root.title("set")
    root.geometry("800x500")
    root.iconbitmap("S_calc_logo.ico")
    lbl1 = tkinter.Label(root, text="Picture Mode")
    lbl1.grid(row=0, column=0)
    combo = ttk.Combobox(root)
    combo["values"] = ("True", "False")
    if self.PictureMode == False:
        combo["values"] = ("False", "True")
    combo.current(0)
    combo.grid(row=0, column=1)
    def change():
        txt = combo.get()
        if txt == "True":
            self.Is_Picture_Mode = True
        else:
            self.Is_Picture_Mode = False
        self.PictureMode = self.Is_Picture_Mode
    btn = tkinter.Button(root, text="Change", command=change)
    btn.grid(row=0, column=2)
    lbl2 = tkinter.Label(root, text='Click "add" to add the limit symbol into your copyboard, \nClick "clear" to clear the copyboard.')
    lbl2.grid(row=1, column=0)
    def add():
        pyperclip.copy("oo")
    btn1 = tkinter.Button(root, text="add", command=add)
    btn1.grid(row=1, column=1)
    def clear():
        pyperclip.copy("")
    btn2 = tkinter.Button(root, text="clear", command=clear)
    btn2.grid(row=1, column=2)
    lbl3 = tkinter.Label(root, text='Click "add" to add the multiplication symbol into your copyboard, \nClick "clear" to clear the copyboard.')
    lbl3.grid(row=2, column=0)
    def add1():
        pyperclip.copy("*")
    btn4 = tkinter.Button(root, text="add", command=add1)
    btn4.grid(row=2, column=1)
    def clear1():
        pyperclip.copy("")
    btn5 = tkinter.Button(root, text="clear", command=clear1)
    btn5.grid(row=2, column=2)
    lbl4 = tkinter.Label(root, text='Click "add" to add the division symbol into your copyboard, \nClick "clear" to clear the copyboard.')
    lbl4.grid(row=3, column=0)
    def add2():
        pyperclip.copy("/")
    btn6 = tkinter.Button(root, text="add", command=add2)
    btn6.grid(row=3, column=1)
    def clear2():
        pyperclip.copy("")
    btn7 = tkinter.Button(root, text="clear", command=clear2)
    btn7.grid(row=3, column=2)
    root.mainloop()
