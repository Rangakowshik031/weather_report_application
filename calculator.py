'''import tkinter
from tkinter import *
from tkinter import messagebox
 
val=""
A = 0
operator=""
 
def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)
 
def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)
 
def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)
 
def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)
 
def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)
 
def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)
 
def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)
 
def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)
 
def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)
 
def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)
 
def btn_add_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)
 
def btn_sub_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)
 
def btn_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)
 
def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)
 
def btn_equal_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "="
    val = val + "="
    data.set(val)
 
def C_pressed():
    global A
    global operator
    global val
    val = ""
    A=0
    operator=""
    data.set(val)
 
 
def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x=int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val=str(c)
    elif operator == "-":
        x=int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val=str(c)
    elif operator == "*":
        x=int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val=str(c)
    elif operator == "/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.show("Error","Division by 0 Not Allowed")
            A==""
            val=""
            data.set(val)
        else:
            c=int(A/x)
            data.set(c)
            val=str(c)

#create a root window
root = tkinter.Tk()
#set geometry
root.geometry("250x400+300+300")
#disable the resize option for better UI
root.resizable(0,0)
#Give the tiltle to your calculator window
root.title("AskPython-Cal")
data= StringVar()
lbl=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana",20),
    textvariable=data,
    background="#ffffff",
    fg="#000000",
)
#expand option deals with the expansion of parent widget.
lbl.pack(expand=True,fill="both",)
#Frame Coding for Buttons
#Frame for root window
#Frame 1
btnrow1=Frame(root,bg="#000000")
#If frame gets some space it can expand
btnrow1.pack(expand=True,fill="both",)
 
#Frame 2
btnrow2=Frame(root)
btnrow2.pack(expand=True,fill="both",)
 
#Frame 3
btnrow3=Frame(root)
btnrow3.pack(expand=True,fill="both",)
 
#Frame 4
btnrow4=Frame(root)
btnrow4.pack(expand=True,fill="both",)
#Button row One
#Button 1
btn1=Button(btnrow1,text = "1",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_1_isclicked,
)
#Buttons will be side by side
btn1.pack(side=LEFT,expand=True,fill="both",)
 
#Button 2
btn2=Button(
    btnrow1,
    text = "2",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_2_isclicked,
)
#Buttons will be side by side
btn2.pack(side=LEFT,expand=True,fill="both",)
 
#Button 3
btn3=Button(
    btnrow1,
    text = "3",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_3_isclicked,
)
#Buttons will be side by side
btn3.pack(side=LEFT,expand=True,fill="both",)
 
#Button add
btnadd=Button(
    btnrow1,
    text = "+",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_add_clicked,
)
#Buttons will be side by side
btnadd.pack(side=LEFT,expand=True,fill="both",)
 
#Button row Two
#Button 4
btn4=Button(
    btnrow2,
    text = "4",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_4_isclicked,
)
#Buttons will be side by side
btn4.pack(side=LEFT,expand=True,fill="both",)
 
#Button 5
btn5=Button(
    btnrow2,
    text = "5",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_5_isclicked,
)
#Buttons will be side by side
btn5.pack(side=LEFT,expand=True,fill="both",)
 
#Button 6
btn6=Button(
    btnrow2,
    text = "6",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_6_isclicked,
)
#Buttons will be side by side
btn6.pack(side=LEFT,expand=True,fill="both",)
 
#Button Subtraction
btnsub=Button(
    btnrow2,
    text = "-",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_sub_clicked,
)
#Buttons will be side by side
btnsub.pack(side=LEFT,expand=True,fill="both",)
 
#Button row Three
#Button 7
btn7=Button(
    btnrow3,
    text = "7",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_7_isclicked,
)
#Buttons will be side by side
btn7.pack(side=LEFT,expand=True,fill="both",)
 
#Button 8
btn8=Button(
    btnrow3,
    text = "8",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_8_isclicked,
)
#Buttons will be side by side
btn8.pack(side=LEFT,expand=True,fill="both",)
 
#Button 9
btn9=Button(
    btnrow3,
    text = "9",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_9_isclicked,
)
#Buttons will be side by side
btn9.pack(side=LEFT,expand=True,fill="both",)
 
#Button Multiply
btnmul=Button(
    btnrow3,
    text = "*",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_mul_clicked,
)
#Buttons will be side by side
btnmul.pack(side=LEFT,expand=True,fill="both",)
 
#Button row Four
#Button C
btnC=Button(
    btnrow4,
    text = "C",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = C_pressed,
)
#Buttons will be side by side
btnC.pack(side=LEFT,expand=True,fill="both",)
 
#Button 0
btn0=Button(
    btnrow4,
    text = "0",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_0_isclicked,
)
#Buttons will be side by side
btn0.pack(side=LEFT,expand=True,fill="both",)
 
#Button Equal to
btnequal=Button(
    btnrow4,
    text = "=",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command=result,
)
#Buttons will be side by side
btnequal.pack(side=LEFT,expand=True,fill="both",)
 
#Button Divide
btndiv=Button(
    btnrow4,
    text = "/",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_div_clicked,
     
)
#Buttons will be side by side
btndiv.pack(side=LEFT,expand=True,fill="both",)
 
 
root.mainloop()


import tkinter
from tkinter import *
m=tkinter.Tk()
m.geometry("300x300")
a=tkinter.Entry(m)
a.grid(row=1,column=1)

#x=IntVar()
def samp():
    my=b.cget("text")
    a.insert(10,my)
def samp1():
    my1=b1.cget("text")
    a.insert(10,my1)
def samp2():
    my2=b2.cget("text")
    a.insert(10,my2)
def samp3():
    my3=b3.cget("text")
    a.insert(10,my3)
def samp4():
    my4=b4.cget("text")
    a.insert(10,my4)
def samp5():
    my5=b5.cget("text")
    a.insert(10,my5)
def samp6():
    my6=b6.cget("text")
    a.insert(10,my6)
def samp7():
    my7=b7.cget("text")
    a.insert(10,my7)
def samp8():
    my8=b8.cget("text")
    a.insert(10,my8)
def samp9():
    my9=b9.cget("text")
    a.insert(10,my9)
def samp10():
    my10=b10.cget("text")
    a.insert(10,my10)
def samp11():
    my11=b11.cget("text")
    a.insert(10,my11)
def samp12():
    my12=b12.cget("text")
    a.insert(10,my12)


    

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

b13=tkinter.Button(m,text="=",command=samp13)
b13.grid(row=6,column=3)

#my=b.cget("text")
#ax=tkinter.Label(m,text=my).grid(row=3,column=1)
#print(x)'''

from tkinter import *

wind = Tk()
wind.title("Calculator")
wind.geometry("300x300")

text = Entry(wind,font=("calibri", 16))
text.pack(fill=X,padx=5,pady=5,ipadx=5,ipady=5)

def addToText(n):
    text.insert(END,n)

def calculate():
    result = eval(text.get())
    text.delete(0,END)
    text.insert(0,result)


frame = Frame(wind)
frame.pack(side=TOP,anchor=NW)

rightFrame = Frame(frame)
rightFrame.pack(side=RIGHT)

frame1 = Frame(frame)
frame1.pack()

#btn 1 to 3
btn1 = Button(frame1,text="1",width=9,height=3, command=lambda:addToText("1"),bg="white")
btn1.pack(side=LEFT)
btn2 = Button(frame1,text="2",width=9,height=3, command=lambda:addToText("2"),bg="white")
btn2.pack(side=LEFT)
btn3 = Button(frame1,text="3",width=9,height=3, command=lambda:addToText("3"),bg="white")
btn3.pack(side=LEFT)


frame2 = Frame(frame)
frame2.pack()

#btn 4 to 6
btn4 = Button(frame2,text="4",width=9,height=3, command=lambda:addToText("4"),bg="white")
btn4.pack(side=LEFT)
btn5 = Button(frame2,text="5",width=9,height=3, command=lambda:addToText("5"),bg="white")
btn5.pack(side=LEFT)
btn6 = Button(frame2,text="6",width=9,height=3, command=lambda:addToText("6"),bg="white")
btn6.pack(side=LEFT)


frame3 = Frame(frame)
frame3.pack()

#btn 7 to 9
btn7 = Button(frame3,text="7",width=9,height=3, command=lambda:addToText("7"),bg="white")
btn7.pack(side=LEFT)
btn8 = Button(frame3,text="8",width=9,height=3, command=lambda:addToText("8"),bg="white")
btn8.pack(side=LEFT)
btn9 = Button(frame3,text="9",width=9,height=3, command=lambda:addToText("9"),bg="white")
btn9.pack(side=LEFT)


frame4 = Frame(frame)
frame4.pack()

#btn 1 to 3
btnpoint = Button(frame4,text=".",width=9,height=3, command=lambda:addToText("."),bg="white")
btnpoint.pack(side=LEFT)
btnzero = Button(frame4,text="0",width=9,height=3, command=lambda:addToText("0"),bg="white")
btnzero.pack(side=LEFT)
btneq = Button(frame4,text="=",width=9,height=3, command=lambda:calculate(),bg="white")
btneq.pack(side=LEFT)

#operators
btndiv = Button(rightFrame,text="/",width=9,height=3, command=lambda:addToText("/"),bg="white")
btndiv.pack()
btnmul = Button(rightFrame,text="x",width=9,height=3, command=lambda:addToText("*"),bg="white")
btnmul.pack()
btndif = Button(rightFrame,text="-",width=9,height=3, command=lambda:addToText("-"),bg="white")
btndif.pack()
btnplus = Button(rightFrame,text="+",width=9,height=3, command=lambda:addToText("+"),bg="white")
btnplus.pack()


wind.mainloop()








































