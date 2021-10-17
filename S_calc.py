import time
import sys
import random
import _thread
import setting
import tools
try:
    import tkinter
    from tkinter import ttk
    use_tkinter = True
except:
    use_tkinter = False
try:
    import sympy
    import solve
    tools.def_sym()
    use_sympy = True
except:
    import math
    use_sympy = False

#类#
class Square_Calc:
    
    def __init__(self):
        self.e2get = ""
        self.e3get = ""
        self.symbols = []
        self.type_text = ''
        self.again = ''
        self.Is_Picture_Mode = False
        self.PictureMode = self.Is_Picture_Mode
        self.to_do = ""
        self.answer = 0.0
        if use_sympy == False:
            self.PI = math.pi
        else:
            self.PI = sympy.pi
        self.equation = ""
        self.equations = []
        self.mode = ""
        self.modes = (
        "normal_calculation",
        "log",
        "sin",
        "cos",
        "tan",
        "gcd",
        "rectangle", 
        "square", 
        "quadrilateral",
        "diamond",
        "diamond(a*a*sina)",
        "triangle",
        "triangle(Helen)",
        "triangle(1/2absinC)",
        "circle", 
        "trapezium", 
        "parallelogram",
        "parallelogram(absina)",
        "ellipse",
        "fan",
        "arch", 
        "definite_integral",
        "indefinite_integral", 
        "differentiation",
        "limit",
        "simplify",
        "solve equations"
        )

    def set(self):
        setting.set_(self)
    
    def ask_mode(self):
        if use_tkinter == False:
            return input("\nChoose a mode(normal_calculation, sin, cos, tan, gcd, rectangle, square, quadrilateral, diamond, diamond(a*a*sina), triangle, triangle(Helen), triangle(1/2absinC), circle, trapezium, parallelogram,  parallelogram(absina), ellipse, fan, arch, differentiation or simplify):")
        else:
            return self.ask_mode_gui()

    def ask_mode_gui(self):
        root = tkinter.Tk()
        root.title("choose a mode")
        root.geometry("500x50")
        root.iconbitmap("S_calc_logo.ico")
        combo = ttk.Combobox(root)
        combo['values'] = self.modes
        combo.current(0)
        combo.grid(row=0, column=0)
        def get():
            self.mode = combo.get()
            root.destroy()
        button = tkinter.Button(root, text="submit", command=get)
        button.grid(row=0, column=1)
        root.mainloop()
        return self.mode

    def height(self):
        if use_tkinter == False:
            self.shape_height = float(input("What is the height:"))
        else:
            root = tkinter.Tk()
            root.title("height(b/h)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_height = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
        
    def width(self):
        if use_tkinter == False:
            self.shape_width = float(input("What is the width:"))
        else:
            root = tkinter.Tk()
            root.title("width(a)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_width = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
       
    def edge_length_1(self):
        if use_tkinter == False:
    	    self.shape_e_l_1 = float(input("What is the first edge length(a)"))
        else:
            root = tkinter.Tk()
            root.title("first edge length(a)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                root.destroy()
                self.shape_e_l_1 = float(entry.get())
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
    	
    def edge_length_2(self):
        if use_tkinter == False:
    	    self.shape_e_l_2 = float(input("What is the second edge length(b)"))
        else:
            root = tkinter.Tk()
            root.title("second edge length(b)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_e_l_2 = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
    	
    def edge_length_3(self):
        if use_tkinter == False:
    	    self.shape_e_l_3 = float(input("What is the third edge length(c)"))
        else:
            root = tkinter.Tk()
            root.title("third edge length(c)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_e_l_3 = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
    
    def up_length(self):
        if use_tkinter == False:
            self.shape_up_length = float(input("What is the up_length:"))
        else:
            root = tkinter.Tk()
            root.title("up length(a)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_up_length = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
        
    def down_length(self):
        if use_tkinter == False:
            self.shape_down_length = float(input("What is the down_length:"))
        else:
            root = tkinter.Tk()
            root.title("down length(b)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_down_length = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
        
    def radius(self):
        if use_tkinter == False:
            self.shape_radius = float(input("What is the radius:"))
        else:
            root = tkinter.Tk()
            root.title("radius(r)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_radius = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
        
    def long_diameter(self):
        if use_tkinter == False:
            self.shape_long_diameter = float(input("What is the long diameter:"))
        else:
            root = tkinter.Tk()
            root.title("long diameter(D)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_long_diameter = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
        
    def short_diameter(self):
        if use_tkinter == False:
            self.shape_short_diameter = float(input("What is the short diameter:"))
        else:
            root = tkinter.Tk()
            root.title("short diameter(d)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_short_diameter = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()

    def long_diagonal(self):
        if use_tkinter == False:
            self.shape_l_d = float(input("What is the long diagonal:"))
        else:
            root = tkinter.Tk()
            root.title("long diagonal(D)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_l_d = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()

    def short_diagonal(self):
        if use_tkinter == False:
            self.shape_s_d = float(input("What is the short diagonal:"))
        else:
            root = tkinter.Tk()
            root.title("short diagonal(d)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_s_d = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
        
    def central_angle(self):
        if use_tkinter == False:
            self.shape_c_a = float(input("What is the central angle:"))
        else:
            root = tkinter.Tk()
            root.title("central angle(a)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_c_a = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()

    def angle(self):
        if use_tkinter == False:
            self.shape_angle = float(input("What is the angle between them:"))
        else:
            root = tkinter.Tk()
            root.title("angle between them(a)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_angle = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()

    def d_angle(self):
        if use_tkinter == False:
            self.shape_d_angle = float(input("What is the angle between the two diagonal:"))
        else:
            root = tkinter.Tk()
            root.title("angle between two diagonal in the shape(a)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_d_angle = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()

    def dia_length(self):
        if use_tkinter == False:
            self.shape_dia_length = float(input("What is the length of each edge lines:"))
        else:
            root = tkinter.Tk()
            root.title("length of each edge lines(a)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_dia_length = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()

    def dia_angle(self):
        if use_tkinter == False:
            self.shape_dia_angle = float(input("What is the angle between two edge lines:"))
        else:
            root = tkinter.Tk()
            root.title("angle between two edge lines(a)")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.shape_dia_angle = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()

    def gcd(self, first_num, second_num):
        if use_sympy == False:
            return math.gcd(first_num, second_num)
        else:
            return sympy.gcd(first_num, second_num)

    def sin(self, angle):
        if use_sympy == False:
            return math.sin(angle * self.PI / 180)
        else:
            return sympy.sin(angle * self.PI / 180)

    def cos(self, angle):
        if use_sympy == False:
            return math.cos(angle * self.PI / 180)
        else:
            return sympy.cos(angle * self.PI / 180)

    def tan(self, angle):
        if use_sympy == False:
            return math.tan(angle * self.PI / 180)
        else:
            return sympy.tan(angle * self.PI / 180)

    def sin_calc(self):
        if use_tkinter == False:
            return self.sin(float(input("What is the angle:")))
        else:
            root = tkinter.Tk()
            root.title("angle")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.sin_angle = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
            return float(self.sin(self.sin_angle))

    def cos_calc(self):
        if use_tkinter == False:
            return self.cos(float(input("What is the angle:")))
        else:
            root = tkinter.Tk()
            root.title("angle")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.cos_angle = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
            return float(self.cos(self.cos_angle))

    def tan_calc(self):
        if use_tkinter == False:
            return self.tan(float(input("What is the angle:")))
        else:
            root = tkinter.Tk()
            root.title("angle")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.tan_angle = float(entry.get())
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
            return float(self.tan(self.tan_angle))

    def gcd_calc(self):
        if use_tkinter == False:
            return self.gcd(float(input("What is the first number:")), float(input("What is the second number:")))
        else:
            root1 = tkinter.Tk()
            root1.title("first number")
            root1.geometry("500x30")
            root1.iconbitmap("S_calc_logo.ico")
            entry1 = tkinter.Entry(root1)
            entry1.grid(row=0, column=0)
            def get1():
                self.first_number = int(entry1.get())
                root1.destroy()
            button1 = tkinter.Button(root1, text="submit", command=get1)
            button1.grid(row=0, column=1)
            root1.mainloop()

            root2 = tkinter.Tk()
            root2.title("second number")
            root2.geometry("500x30")
            root2.iconbitmap("S_calc_logo.ico")
            entry2 = tkinter.Entry(root2)
            entry2.grid(row=0, column=0)
            def get2():
                self.second_number = int(entry2.get())
                root2.destroy()
            button2 = tkinter.Button(root2, text="submit", command=get2)
            button2.grid(row=0, column=1)
            root2.mainloop()

            return self.gcd(self.first_number, self.second_number)

    def n_c(self):
        if use_tkinter == False:
            self.the_n_c = input("What do you want to calculate:")
        else:
            root = tkinter.Tk()
            root.title("formula")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def get():
                self.the_n_c = entry.get()
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
        return float(eval(self.the_n_c))

    def rec(self):
        if self.PictureMode == False:
            self.width()
            self.height()
        else:
            root = tkinter.Tk()
            root.iconbitmap("S_calc_logo.ico")
            root.title("Rectangle")
            root.geometry("500x200")
            e1 = tkinter.Entry(root, width=5)
            e1.grid(row=0, column=0)
            e1.insert("end", "long")
            l1 = tkinter.Label(root, text="------------------------")
            l1.grid(row=1, column=0)
            l2 = tkinter.Label(root, text="|                                 |")
            l2.grid(row=2, column=0)
            e2 = tkinter.Entry(root, width=5)
            e2.grid(row=2, column=1)
            e2.insert("end", "long")
            l3 = tkinter.Label(root, text="------------------------")
            l3.grid(row=3, column=0)
            def get():
                self.shape_width = float(e1.get())
                self.shape_height = float(e2.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=4, column=0)
            root.mainloop()
        return self.shape_width * self.shape_height
        
    def square(self):
        if self.PictureMode == False:
            self.width()
        else:
            root = tkinter.Tk()
            root.iconbitmap("S_calc_logo.ico")
            root.title("Square")
            root.geometry("500x200")
            l1 = tkinter.Label(root, text="-------")
            l1.grid(row=0, column=0)
            l2 = tkinter.Label(root, text="|        |")
            l2.grid(row=1, column=0)
            l3 = tkinter.Label(root, text="|        |")
            l3.grid(row=2, column=0)
            e1 = tkinter.Entry(root, width=5)
            e1.grid(row=2, column=1)
            e1.insert("end", "long")
            l4 = tkinter.Label(root ,text="-------")
            l4.grid(row=3, column=0)
            def get():
                self.shape_width = float(e1.get())
                root.destroy()
            b1 = tkinter.Button(root, text="submit", command=get)
            b1.grid(row=5, column=0)
            root.mainloop()
        return self.shape_width ** 2

    def qua(self):
        if self.PictureMode == False:
            self.long_diagonal()
            self.short_diagonal()
            self.d_angle()
        else:
            root = tkinter.Tk()
            root.title("quadrilateral")
            root.geometry("500x500")
            root.iconbitmap("S_calc_logo.ico")
            l1 = tkinter.Label(root, text="      /|\\")
            l2 = tkinter.Label(root, text="     / | \\")
            l3 = tkinter.Label(root, text="    /  |  \\")
            l4 = tkinter.Label(root, text="  /    |    \\")
            l5 = tkinter.Label(root, text="  --------")
            l6 = tkinter.Label(root, text="  \\    |   /")
            l7 = tkinter.Label(root, text="   \\   |  /")
            l8 = tkinter.Label(root, text="     \\ | /")
            l9 = tkinter.Label(root, text="      \\|/")
            l10 = tkinter.Label(root, text="Two diagonals' included angle:")
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            l4.grid(row=3, column=0)
            l5.grid(row=4, column=0)
            l6.grid(row=5, column=0)
            l7.grid(row=6, column=0)
            l8.grid(row=7, column=0)
            l9.grid(row=8, column=0)
            l10.grid(row=10, column=0)
            e1 = tkinter.Entry(root, width=20)
            e1.grid(row=4, column=1)
            e1.insert("end", "diagonal's long")
            e2 = tkinter.Entry(root, width=20)
            e2.grid(row=9, column=0)
            e2.insert("end", "diagonal's long")
            e3 = tkinter.Entry(root, width=5)
            e3.grid(row=10, column=1)
            e3.insert("end", "angle")
            def get():  
                self.shape_l_d = float(e1.get())
                self.shape_s_d = float(e2.get())
                self.shape_d_angle = float(e3.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=11, column=0)
            root.mainloop()
        return float(self.shape_l_d * self.shape_s_d * self.sin(self.shape_d_angle) / 2)

    def dia(self):
        if self.PictureMode == False:
            self.long_diagonal()
            self.short_diagonal()
        else:
            root = tkinter.Tk()
            root.title("diamond")
            root.geometry("500x500")
            root.iconbitmap("S_calc_logo.ico")
            l1 = tkinter.Label(root, text="      /|\\")
            l2 = tkinter.Label(root, text="     / | \\")
            l3 = tkinter.Label(root, text="    /  |  \\")
            l4 = tkinter.Label(root, text="  /    |    \\")
            l5 = tkinter.Label(root, text="  --------")
            l6 = tkinter.Label(root, text="  \\    |   /")
            l7 = tkinter.Label(root, text="   \\   |  /")
            l8 = tkinter.Label(root, text="     \\ | /")
            l9 = tkinter.Label(root, text="      \\|/")
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            l4.grid(row=3, column=0)
            l5.grid(row=4, column=0)
            l6.grid(row=5, column=0)
            l7.grid(row=6, column=0)
            l8.grid(row=7, column=0)
            l9.grid(row=8, column=0)
            e1 = tkinter.Entry(root, width=20)
            e1.grid(row=4, column=1)
            e1.insert("end", "diagonal's long")
            e2 = tkinter.Entry(root, width=20)
            e2.grid(row=9, column=0)
            e2.insert("end", "diagonal's long")
            def get():
                self.shape_l_d = float(e1.get())
                self.shape_s_d = float(e2.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=10, column=0)
            root.mainloop()
        return self.shape_l_d * self.shape_s_d / 2
        
    def dia_a2sina(self):
        if self.PictureMode == False:
            self.dia_length()
            self.dia_angle()
        else:
            root = tkinter.Tk()
            root.title("diamond")
            root.geometry("500x500")
            root.iconbitmap("S_calc_logo.ico")
            l1 = tkinter.Label(root, text="      /|\\")
            l2 = tkinter.Label(root, text="     / | \\")
            l3 = tkinter.Label(root, text="    /  |  \\")
            l4 = tkinter.Label(root, text="  /    |    \\")
            l5 = tkinter.Label(root, text="  --------")
            l6 = tkinter.Label(root, text="  \\    |   /")
            l7 = tkinter.Label(root, text="   \\   |  /")
            l8 = tkinter.Label(root, text="     \\ | /")
            l9 = tkinter.Label(root, text="      \\|/")
            l10 = tkinter.Label(root, text="two edges' included angle:")
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            l4.grid(row=3, column=0)
            l5.grid(row=4, column=0)
            l6.grid(row=5, column=0)
            l7.grid(row=6, column=0)
            l8.grid(row=7, column=0)
            l9.grid(row=8, column=0)
            l10.grid(row=9, column=0)
            e1 = tkinter.Entry(root, width=5)
            e1.grid(row=2, column=1)
            e1.insert("end", "long")
            e2 = tkinter.Entry(root, width=5)
            e2.grid(row=9, column=1)
            e2.insert("end", "angle")
            def get():
                self.shape_dia_length = float(e1.get())
                self.shape_dia_angle = float(e2.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=10, column=0)
            root.mainloop()
        return float(self.shape_dia_length ** 2 * self.sin(self.shape_dia_angle))

    def tri(self):
        if self.PictureMode == False:
            self.width()
            self.height()
        else:
            root = tkinter.Tk()
            root.title("triangle")
            root.iconbitmap("S_calc_logo.ico")
            root.geometry("500x500")
            l1 = tkinter.Label(root, text="height:")
            l2 = tkinter.Label(root, text="       / |\\")
            l3 = tkinter.Label(root, text="      /  |  \\")
            l4 = tkinter.Label(root, text="     /   |    \\")
            l5 = tkinter.Label(root, text="    /    |     \\")
            l6 = tkinter.Label(root, text="  /      |       \\")
            l7 = tkinter.Label(root, text="/_____ |______\\")
            l8 = tkinter.Label(root, text="")
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            l4.grid(row=3, column=0)
            l5.grid(row=4, column=0)
            l6.grid(row=5, column=0)
            l7.grid(row=6, column=0)
            l8.grid(row=7, column=0)
            e1 = tkinter.Entry(root, width=5)
            e1.grid(row=0, column=1)
            e1.insert("end", "long")
            e2 = tkinter.Entry(root, width=5)
            e2.grid(row=8, column=0)
            e2.insert("end", "long")
            def get():
                self.shape_height = float(e1.get())
                self.shape_width = float(e2.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=9, column=0)
            root.mainloop()
        return self.shape_width * self.shape_height / 2
        
    def circle(self):
        if self.PictureMode == False:
            self.radius()
        else:
            root = tkinter.Tk()
            root.title("circle")
            root.geometry("500x500")
            root.iconbitmap("S_calc_logo.ico")
            l1 = tkinter.Label(root, text="     ___")
            l2 = tkinter.Label(root, text="    /     \\")
            l3 = tkinter.Label(root, text="   |   ----|")
            l4 = tkinter.Label(root, text="    \___/")
            e1 = tkinter.Entry(root, width=10)
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            l4.grid(row=3, column=0)
            e1.grid(row=2, column=1)
            e1.insert("end", "radius long")
            def get():
                self.shape_radius = float(e1.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=4, column=0)
            root.mainloop()
        return float(self.shape_radius * self.shape_radius * self.PI)
        
    def trap(self):
        if self.PictureMode == False:
            self.up_length()
            self.down_length()
            self.height()
        else:
            root = tkinter.Tk()
            root.title("trapezium")
            root.iconbitmap("S_calc_logo.ico")

            l1 = tkinter.Label(root, text="   /---------\\")
            l2 = tkinter.Label(root, text="/___________\\")
            e1 = tkinter.Entry(root)
            e2 = tkinter.Entry(root)
            e3 = tkinter.Entry(root)

            e1.grid(row=0, column=0)
            e1.insert("end", "long")
            e2.grid(row=3, column=0)
            e2.insert("end", "long")
            e3.grid(row=2, column=1)
            e3.insert("end", "height")
            l1.grid(row=1, column=0)
            l2.grid(row=2, column=0)

            def get():
                self.shape_up_length = float(e1.get())
                self.shape_down_length = float(e2.get())
                self.shape_height = float(e3.get())
                root.destroy()

            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=4, column=0)

            root.mainloop()
        return (self.shape_up_length + self.shape_down_length) * self.shape_height / 2
        
    def para(self):
        if self.PictureMode == False:
            self.width()
            self.height()
        else:
            root = tkinter.Tk()
            root.title("parallelogram")
            root.geometry("500x500")
            root.iconbitmap("S_calc_logo.ico")
            l1 = tkinter.Label(root, text="   _____________________")
            l2 = tkinter.Label(root, text="  /                        /")
            l3 = tkinter.Label(root, text="/--------------------/")
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            e1 = tkinter.Entry(root)
            e1.grid(row=3, column=0)
            e1.insert("end", "long")
            e2 = tkinter.Entry(root)
            e2.grid(row=2, column=1)
            e2.insert("end", "height")
            def get():
                self.shape_width = float(e1.get())
                self.shape_height = float(e2.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=4, column=0)
            root.mainloop()
        return self.shape_width * self.shape_height

    def para_absina(self):
        if self.PictureMode == False:
            self.edge_length_1()
            self.edge_length_2()
            self.angle()
        else:
            root = tkinter.Tk()
            root.title("parallelogram")
            root.geometry("500x500")
            root.iconbitmap("S_calc_logo.ico")
            l1 = tkinter.Label(root, text="   _____________________")
            l2 = tkinter.Label(root, text="  /                        /")
            l3 = tkinter.Label(root, text="/--------------------/")
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            e1 = tkinter.Entry(root)
            e1.grid(row=3, column=0)
            e1.insert("end", "long")
            e2 = tkinter.Entry(root)
            e2.grid(row=2, column=1)
            e2.insert("end", "long")
            e3 = tkinter.Entry(root)
            e3.grid(row=3, column=1)
            e3.insert("end", "angle")
            def get():
                self.shape_e_l_1 = float(e1.get())
                self.shape_e_l_2 = float(e2.get())
                self.shape_angle = float(e3.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=4, column=0)
            root.mainloop()
        return float(self.shape_e_l_1 * self.shape_e_l_2 * self.sin(self.shape_angle))
        
    def elli(self):
        if self.PictureMode == False:
            self.long_diameter()
            self.short_diameter()
        else:
            root = tkinter.Tk()
            root.title("ellipse")
            root.geometry("500x500")
            root.iconbitmap("S_calc_logo.ico")
            l1 = tkinter.Label(root, text="  ________________________")
            l2 = tkinter.Label(root, text="/                |                 \\")
            l3 = tkinter.Label(root, text="|-------------|--------------|")
            l4 = tkinter.Label(root, text="\\___________ |____________/")
            e1 = tkinter.Entry(root)
            e2 = tkinter.Entry(root)
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            l4.grid(row=3, column=0)
            e1.grid(row=2, column=1)
            e2.grid(row=4, column=0)
            e1.insert("end", "diameter's long")
            e2.insert("end", "diameter's long")
            def get():
                self.shape_long_diameter = float(e1.get())
                self.shape_short_diameter = float(e2.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=5, column=0)
            root.mainloop()
        return float(self.shape_long_diameter * self.shape_short_diameter * self.PI / 4)
    
    def fan(self):
        if self.PictureMode == False:
            self.central_angle()
            self.radius()
        else:
            root = tkinter.Tk()
            root.title("fan")
            root.geometry("500x500")
            root.iconbitmap("S_calc_logo.ico")
            l1 = tkinter.Label(root, text="  _____")
            l2 = tkinter.Label(root, text="/         \\")
            l3 = tkinter.Label(root, text="\\         /")
            l4 = tkinter.Label(root, text="  \\     /   ")
            l5 = tkinter.Label(root, text="  \\  /")
            e1 = tkinter.Entry(root)
            e2 = tkinter.Entry(root)
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            l4.grid(row=3, column=0)
            l5.grid(row=4, column=0)
            e1.grid(row=3, column=1)
            e2.grid(row=5, column=0)
            e1.insert("end", "long")
            e2.insert("end", "angle")
            def get():
                self.shape_radius = float(e1.get())
                self.shape_c_a = float(e2.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=6, column=0)
            root.mainloop()
        if self.shape_c_a != 0:
            return float(self.shape_c_a / 360 * self.shape_radius * self.shape_radius * self.PI)
        else:pass

    def arch(self):
        if self.PictureMode == False:
            self.central_angle()
            self.radius()
        else:
            root = tkinter.Tk()
            root.title("arch")
            root.geometry("500x500")
            root.iconbitmap("S_calc_logo.ico")
            l1 = tkinter.Label(root, text="/-----------\\")
            l2 = tkinter.Label(root, text="-------------")
            l3 = tkinter.Label(root, text="\\           /")
            l4 = tkinter.Label(root, text="  \\       /")
            l5 = tkinter.Label(root, text="   \\  /")
            l6 = tkinter.Label(root, text="(the lines in the\nlower part of the\npicture are not real)")
            e1 = tkinter.Entry(root)
            e2 = tkinter.Entry(root)
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            l4.grid(row=3, column=0)
            l5.grid(row=4, column=0)
            l6.grid(row=2, column=1)
            e1.grid(row=3, column=1)
            e2.grid(row=5, column=0)
            e1.insert("end", "long")
            e2.insert("end", "angle")
            def get():
                self.shape_radius = float(e1.get())
                self.shape_c_a = float(e2.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=6, column=0)
            root.mainloop()
        if self.shape_c_a != 0:
            return float(self.shape_radius * self.shape_radius * self.shape_c_a * self.PI / 360 - self.shape_radius * self.shape_radius * self.sin(self.shape_c_a) / 2)
        else:pass

    def tri_Helen(self):
        if self.PictureMode == False:
            self.edge_length_1()
            self.edge_length_2()
            self.edge_length_3()
        else:
            root = tkinter.Tk()
            root.title("triangle")
            root.iconbitmap("S_calc_logo.ico")
            root.geometry("500x500")
            l2 = tkinter.Label(root, text="       / |\\")
            l3 = tkinter.Label(root, text="      /  |  \\")
            l4 = tkinter.Label(root, text="     /   |    \\")
            l5 = tkinter.Label(root, text="    /    |     \\")
            l6 = tkinter.Label(root, text="  /      |       \\")
            l7 = tkinter.Label(root, text="/_____|______\\")
            l8 = tkinter.Label(root, text="")
            l2.grid(row=0, column=1)
            l3.grid(row=1, column=1)
            l4.grid(row=2, column=1)
            l5.grid(row=3, column=1)
            l6.grid(row=4, column=1)
            l7.grid(row=5, column=1)
            l8.grid(row=6, column=1)
            e1 = tkinter.Entry(root, width=5)
            e1.grid(row=3, column=0)
            e1.insert("end", "long")
            e2 = tkinter.Entry(root, width=5)
            e2.grid(row=3, column=2)
            e2.insert("end", "long")
            e3 = tkinter.Entry(root, width=5)
            e3.grid(row=7, column=1)
            e3.insert("end", "long")
            def get():
                self.shape_e_l_1 = float(e1.get())
                self.shape_e_l_2 = float(e2.get())
                self.shape_e_l_3 = float(e3.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=8, column=0)
            root.mainloop()
        s = (self.shape_e_l_1 + self.shape_e_l_2 + self.shape_e_l_3) / 2
        return (s * (s - self.shape_e_l_1) * (s - self.shape_e_l_2) * (s - self.shape_e_l_3)) ** 0.5

    def tri_absinc(self):
        if self.PictureMode == False:
            self.edge_length_1()
            self.edge_length_2()
            self.angle()
        else:
            root = tkinter.Tk()
            root.title("triangle")
            root.iconbitmap("S_calc_logo.ico")
            root.geometry("500x500")
            l2 = tkinter.Label(root, text="       / |\\")
            l3 = tkinter.Label(root, text="      /  |  \\")
            l4 = tkinter.Label(root, text="     /   |    \\")
            l5 = tkinter.Label(root, text="    /    |     \\")
            l6 = tkinter.Label(root, text="  /      |       \\")
            l7 = tkinter.Label(root, text="/_____|______\\")
            l8 = tkinter.Label(root, text="")
            l2.grid(row=0, column=1)
            l3.grid(row=1, column=1)
            l4.grid(row=2, column=1)
            l5.grid(row=3, column=1)
            l6.grid(row=4, column=1)
            l7.grid(row=5, column=1)
            l8.grid(row=6, column=1)
            e1 = tkinter.Entry(root, width=5)
            e1.grid(row=3, column=0)
            e1.insert("end", "long")
            e2 = tkinter.Entry(root, width=5)
            e2.grid(row=7, column=0)
            e2.insert("end", "angle")
            e3 = tkinter.Entry(root, width=5)
            e3.grid(row=7, column=1)
            e3.insert("end", "long")
            def get():
                self.shape_e_l_1 = float(e1.get())
                self.shape_e_l_2 = float(e3.get())
                self.shape_angle = float(e2.get())
                root.destroy()
            b1 = tkinter.Button(root, text="Submit", command=get)
            b1.grid(row=8, column=0)
            root.mainloop()
        return float(self.shape_e_l_1 * self.shape_e_l_2 * self.sin(self.shape_angle) / 2)

    def d_i_get(self):
        root = tkinter.Tk()
        root.title("definite_integral")
        root.iconbitmap("S_calc_logo.ico")
        root.geometry("500x100")
        label1 = tkinter.Label(root, text="     /\\")
        label1.grid(row=0, column=0)
        label2 = tkinter.Label(root, text="   /")
        label2.grid(row=1, column=0)
        label3 = tkinter.Label(root, text="\\/")
        label3.grid(row=2, column=0)
        e1 = tkinter.Entry(root)
        e1.grid(row=0, column=1)
        e2 = tkinter.Entry(root)
        e2.grid(row=2, column=1)
        e3 = tkinter.Entry(root)
        e3.grid(row=1, column=1)
        label4 = tkinter.Label(root, text="d")
        label4.grid(row=1, column=2)
        new_e = tkinter.Entry(root)
        new_e.grid(row=1, column=3)
        def submit():
            self.e1get = tools.get_num(e1)
            self.e2get = tools.get_num(e2)
            self.e3get = e3.get()
            self.symbol1 = new_e.get()
            root.destroy()
        btn = tkinter.Button(root, text="submit", command=submit)
        btn.grid()
        root.mainloop()

    def d_i(self):
        self.d_i_get()
        return sympy.integrate(self.e3get, (self.symbol1, self.e2get, self.e1get))

    def i_i_get(self):
        root = tkinter.Tk()
        root.title("indefinite_integral")
        root.iconbitmap("S_calc_logo.ico")
        root.geometry("500x100")
        label5 = tkinter.Label(root, text="     /\\")
        label5.grid(row=0, column=0)
        label6 = tkinter.Label(root, text="   /")
        label6.grid(row=1, column=0)
        label7 = tkinter.Label(root, text="\\/")
        label7.grid(row=2, column=0)
        e4 = tkinter.Entry(root)
        e4.grid(row=1, column=1)
        label8 = tkinter.Label(root, text="d")
        label8.grid(row=1, column=2)
        e5 = tkinter.Entry(root)
        e5.grid(row=1, column=3) 
        def submit():
            self.e4get = e4.get()
            self.symbol2 = e5.get()
            root.destroy()
        btn = tkinter.Button(root, text="submit", command=submit)
        btn.grid()
        root.mainloop()

    def i_i(self):
        self.i_i_get()
        return sympy.integrate(self.e4get, (self.symbol2,))

    def function(self):
        if use_tkinter == True:
            root = tkinter.Tk()
            root.title("function")
            root.iconbitmap("S_calc_logo.ico")
            root.geometry("500x100")
            entry = tkinter.Entry(root)
            entry.grid(row=0, column=0)
            def submit():
                self.func = entry.get()
                root.destroy()
            btn = tkinter.Button(root, text="submit", command=submit)
            btn.grid(row=0, column=1)
            root.mainloop()
        else:
            self.func = input("function:")

    def diff(self):
        self.function()
        return sympy.diff(self.func)

    def get_l_n(self):
        root = tkinter.Tk()
        root.title("log")
        root.geometry("500x100")
        root.iconbitmap("S_calc_logo.ico")
        Label1 = tkinter.Label(root, text="Log")
        Label1.grid(row=0, column=0)
        Entry1 = tkinter.Entry(root)
        Entry1.grid(row=1, column=1)
        Label2 = tkinter.Label(root, text="                  ")
        Label2.grid(row=0, column=1)
        Entry2 = tkinter.Entry(root)
        Entry2.grid(row=0, column=2)
        def get():
            self.fir_num = float(Entry1.get())
            self.fin_num = float(Entry2.get())
            root.destroy()
        btn = tkinter.Button(root, text="submit", command=get)
        btn.grid(row=2, column=0)
        root.mainloop()

    def log(self):
        self.get_l_n()
        return sympy.log(self.fin_num, self.fir_num)

    def simp(self):
        self.function()
        return sympy.simplify(self.func)

    def lim_get(self):
        root = tkinter.Tk()
        root.geometry("500x500")
        root.title("limit")
        root.iconbitmap("S_calc_logo.ico")
        lbl1 = tkinter.Label(root, text="lim")
        lbl1.grid(row=0, column=0)
        ety1 = tkinter.Entry(root)
        ety1.grid(row=0, column=1)
        ety2 = tkinter.Entry(root)
        ety2.grid(row=1, column=0)
        lbl2 = tkinter.Label(root, text="->")
        lbl2.grid(row=1, column=1)
        ety3 = tkinter.Entry(root)
        ety3.grid(row=1, column=2)
        def get():
            self.func = ety1.get()
            self.e2get = ety2.get()
            self.e3get = tools.get_num(ety3)
            root.destroy()
        btn1 = tkinter.Button(root, text="Submit", command=get)
        btn1.grid(row=2, column=0)
        root.mainloop()

    def lim(self):
        self.lim_get()
        return sympy.limit(self.func, self.e2get, self.e3get)

    def welcome(self, help_text, ABOUT, HISTORY):
        if use_tkinter == False:
            self.type_text = input("Welcome to Square Calculator! Hit [ENTER] to start. PS:Don't know English about shapes? Type help:")
        else:
            wel_win = tkinter.Tk()
            wel_win.title("Welcome to Square Calculator")
            wel_win.geometry("500x50")
            wel_win.iconbitmap("S_calc_logo.ico")
            combo = ttk.Combobox(wel_win)
            combo['values'] = ("start", "about", "help", "history", "version", "set")
            combo.current(0)
            combo.grid(row=0, column=0)
            def get():
                self.type_text = combo.get()
                if self.type_text == 'start':
                    def start_th():
                        while True:
                            self.main()
                            self.next()
                    _thread.start_new_thread(start_th, ())

                elif self.type_text =='set':
                    self.set()
                   
                elif self.type_text == 'help':
                    if use_tkinter == True:
                        root = tkinter.Tk()
                        root.title("help")
                        root.geometry("200x800")
                        root.iconbitmap("S_calc_logo.ico")
                        label = tkinter.Label(root, text=help_text)
                        label.grid(row=0, column=0)
                        root.mainloop()
                    else:
                        print(help_text)
                elif self.type_text == 'about':
                    about_win = tkinter.Tk()
                    about_win.title("about")
                    about_win.iconbitmap("S_calc_logo.ico")
                    about_text = ABOUT
                    about_label = tkinter.Label(about_win, text=about_text)
                    about_label.grid(row=0, column=0)
                elif self.type_text == 'history':
                    history_win = tkinter.Tk()
                    history_win.title("history")
                    history_win.iconbitmap("S_calc_logo.ico")
                    history_text = HISTORY
                    history_label = tkinter.Label(history_win, text=history_text)
                    history_label.grid(row=0, column=0)
                elif self.type_text == 'version':
                    if use_sympy == True:
                        math_library_version = "sympy version:" + str(str(sympy.__version__))
                    else:
                        import platform
                        math_library_version = "math version:" + str(str(platform.python_version()))
                    if use_tkinter == True:
                        version_str = math_library_version + "\n" + "tk version:" + str(tkinter.TkVersion)
                    else:
                        version_str = math_library_version
                    version_str += "\nSquare Calculator version:" + str(8.15)
                    version_win = tkinter.Tk()
                    version_win.title("version")
                    version_win.geometry("500x100")
                    version_win.iconbitmap("S_calc_logo.ico")
                    version_label = tkinter.Label(version_win, text=version_str)
                    version_label.grid()
                    version_win.mainloop()  

            button = tkinter.Button(wel_win, text="submit", command=get)
            button.grid(row=0, column=1)
            def close():
                sys.exit()
            button1 = tkinter.Button(wel_win, text="close", command=close)
            button1.grid(row=0, column=2)
            wel_win.mainloop()

    def exit(self):
        raise SystemExit()

    def next(self):
        if use_tkinter == False:
            next = input("\\ncalculate again?(y/n)")
            if next != 'y':
                self.exit()
        else:
            root = tkinter.Tk()
            root.title("calculate again?")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            combo = ttk.Combobox(root)
            combo['values'] = ("y", "n")
            combo.current(0)
            combo.grid(row=0, column=0)
            def get():
                self.again = combo.get()
                root.destroy()
            button = tkinter.Button(root, text="submit", command=get)
            button.grid(row=0, column=1)
            root.mainloop()
            if self.again != 'y':
                self.exit()

    def main(self):
        #获取选项
        self.to_do = self.ask_mode()
        
        #计算答案
        
        if self.to_do == 'normal_calculation':
            self.answer = self.n_c()
        elif self.to_do == 'log' and use_tkinter == True:
            self.answer = self.log()
        elif self.to_do == 'sin':
            self.answer = self.sin_calc()
        elif self.to_do == 'cos':
            self.answer = self.cos_calc()
        elif self.to_do == 'tan':
            self.answer = self.tan_calc()
        elif self.to_do == 'gcd':
            self.answer = self.gcd_calc()
        elif self.to_do == 'rectangle':
            self.answer = self.rec()
        elif self.to_do == 'square':
            self.answer = self.square()
        elif self.to_do == 'quadrilateral':
            self.answer = self.qua()
        elif self.to_do == 'diamond':
            self.answer = self.dia()
        elif self.to_do == 'diamond(a*a*sina)':
            self.answer = self.dia_a2sina()
        elif self.to_do == 'triangle':
            self.answer = self.tri()
        elif self.to_do == 'circle':
            self.answer = self.circle()
        elif self.to_do == 'trapezium':
            self.answer = self.trap()
        elif self.to_do == 'parallelogram':
            self.answer = self.para()
        elif self.to_do == 'parallelogram(absina)':
            self.answer = self.para_absina()
        elif self.to_do == 'ellipse':
            self.answer = self.elli()
        elif self.to_do == 'fan':
            self.answer = self.fan()
        elif self.to_do == 'arch':
            self.answer = self.arch()
        elif self.to_do == 'triangle(Helen)':
          	self.answer = self.tri_Helen()
        elif self.to_do == 'triangle(1/2absinC)':
            self.answer = self.tri_absinc() 
        elif self.to_do == 'definite_integral' and use_tkinter == True and use_sympy == True:
            self.answer = self.d_i()
        elif self.to_do == 'indefinite_integral' and use_tkinter == True and use_sympy == True:
            self.answer = self.i_i()
        elif self.to_do == 'differentiation' and use_sympy == True:
            self.answer = self.diff() 
        elif self.to_do == 'simplify' and use_sympy == True:
            self.answer = self.simp()
        elif self.to_do == 'solve equations' and use_tkinter == True and use_sympy == True:
            self.answer = solve.sol(self)
        elif self.to_do == 'limit' and use_tkinter == True and use_sympy == True:
            self.answer = self.lim()

        #显示答案
        if use_tkinter == True:
            root = tkinter.Tk()
            root.title("answer")
            root.geometry("500x50")
            root.iconbitmap("S_calc_logo.ico")
            label = tkinter.Label(root, text=str(self.answer))
            label.grid(row=0, column=0)
            root.mainloop()
        else:
            print("The answer is:" + str(self.answer) + ". ")