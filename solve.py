import sympy
import tkinter

def sol(self):
    self.equations = []
    root = tkinter.Tk()
    root.title("solve")
    root.iconbitmap("S_calc_logo.ico")
    root.geometry("500x500")
    lbl = tkinter.Label(root, text="equations:")
    lbl.grid(row=0, column=0)
    lstbox = tkinter.Listbox(root)
    lstbox.grid(row=1, column=0)
    def add():
        add_win = tkinter.Tk()
        add_win.iconbitmap("S_calc_logo.ico")
        add_win.title("add")
        lbl1 = tkinter.Label(add_win, text="equation(Please don't write\n space between symbols):")
        lbl1.grid(row=0, column=0)
        ety1 = tkinter.Entry(add_win)
        ety1.grid(row=1, column=0)
        lbl2 = tkinter.Label(add_win, text="=")
        lbl2.grid(row=1, column=1)
        ety2 = tkinter.Entry(add_win)
        ety2.grid(row=1, column=2)
        def add_in_list():
            ety1get = ety1.get()
            ety2get = ety2.get()
            self.equation = "(" + ety1get + ")" + "-(" + ety2get + ")"
            lstbox.insert("end", "(" + ety1get + ")" + "=" + "(" + ety2get + ")")
            self.equations.append(self.equation)
        btn = tkinter.Button(add_win, text="add", command=add_in_list)
        btn.grid(row=2, column=0)
        add_win.mainloop()
    btn1 = tkinter.Button(root, text="add equations", command=add)
    btn1.grid(row=2, column=0)
    def submit():
        self.ans = sympy.solve(self.equations)
        root.destroy()
    btn2 = tkinter.Button(root, text="Submit", command=submit)
    btn2.grid(row=2, column=1)
    root.mainloop()
    return self.ans
