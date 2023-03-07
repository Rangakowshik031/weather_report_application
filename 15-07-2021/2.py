'''import tkinter
from tkinter import *
m=tkinter.Tk()
m.geometry("300x300")
a=tkinter.Entry(m)
a.grid(row=1,column=1)
l=[]
#x=IntVar()
def samp():
    my=b.cget("text")
    a.insert(10,my)
    l.append(my)
def samp1():
    my1=b1.cget("text")
    a.insert(10,my1)
    l.append(my1)
def samp2():
    my2=b2.cget("text")
    a.insert(10,my2)
    l.append(my2)
def samp3():
    my3=b3.cget("text")
    a.insert(10,my3)
    l.append(my3)
def samp4():
    my4=b4.cget("text")
    a.insert(10,my4)
    l.append(my4)
def samp5():
    my5=b5.cget("text")
    a.insert(10,my5)
    l.append(my5)
def samp6():
    my6=b6.cget("text")
    a.insert(10,my6)
    l.append(my6)
def samp7():
    my7=b7.cget("text")
    a.insert(10,my7)
    l.append(my7)
def samp8():
    my8=b8.cget("text")
    a.insert(10,my8)
    l.append(my8)
def samp9():
    my9=b9.cget("text")
    a.insert(10,my9)
    l.append(my9)
def samp10():
    my10=b10.cget("text")
    a.insert(10,my10)
    l.append(my10)
def samp11():
    my11=b11.cget("text")
    a.insert(10,my11)
    l.append(my11)
def samp12():
    my12=b12.cget("text")
    a.insert(10,my12)
    l.append(my12)
def samp13():
    my13=b13.cget("text")
    a.insert(10,my13)
    l.append(my13)
def samp14():
    my14=b14.cget("text")
    a.insert(10,my14)
    l.append(my14)
def samp15():
    my15=b15.cget("text")
    a.insert(10,my15)
    l.append(my15)

def samp16():
    a.delete(0,END)
    l.clear()

def displ():
    if '+' in l:
        s=int(l[0])+int(l[2])
        a.delete(0,END)
        a.insert(10,str(s))
    if '-' in l:
        s=int(l[0])-int(l[2])
        a.delete(0,END)
        a.insert(10,str(s))
    if '*' in l:
        s=int(l[0])*int(l[2])
        a.delete(0,END)
        a.insert(10,str(s))
    if '/' in l:
        s=int(l[0])/int(l[2])
        a.delete(0,END)
        a.insert(10,str(s))

b=tkinter.Button(m,text="1",command=samp)
b.grid(row=2,column=0)

b1=tkinter.Button(m,text="2",command=samp1)
b1.grid(row=2,column=1)

b2=tkinter.Button(m,text="3",command=samp2)
b2.grid(row=2,column=2)

b3=tkinter.Button(m,text="4",command=samp3)
b3.grid(row=3,column=0)

b4=tkinter.Button(m,text="5",command=samp4)
b4.grid(row=3,column=1)

b5=tkinter.Button(m,text="6",command=samp5)
b5.grid(row=3,column=2)

b6=tkinter.Button(m,text="7",command=samp6)
b6.grid(row=4,column=0)

b7=tkinter.Button(m,text="8",command=samp7)
b7.grid(row=4,column=1)

b8=tkinter.Button(m,text="9",command=samp8)
b8.grid(row=4,column=2)

b9=tkinter.Button(m,text="%",command=samp9)
b9.grid(row=5,column=0)

b10=tkinter.Button(m,text="0",command=samp10)
b10.grid(row=5,column=1)

b11=tkinter.Button(m,text=".",command=samp11)
b11.grid(row=5,column=2)

b12=tkinter.Button(m,text="+",command=samp12)
b12.grid(row=5,column=3)

b13=tkinter.Button(m,text="*",command=samp13)
b13.grid(row=4,column=3)

b14=tkinter.Button(m,text="-",command=samp14)
b14.grid(row=3,column=3)

b15=tkinter.Button(m,text="/",command=samp15)
b15.grid(row=2,column=3)

b16=tkinter.Button(m,text="Clear",command=samp16)
b16.grid(row=7,column=0)


b17=tkinter.Button(m,text="=",command=displ)
b17.grid(row=7,column=1)
#my=b.cget("text")
#ax=tkinter.Label(m,text=my).grid(row=3,column=1)
#print(x)'''
import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()








































