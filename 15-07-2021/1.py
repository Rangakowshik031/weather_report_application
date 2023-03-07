import re 
flag=0

import tkinter
from tkinter import messagebox

#print(dir(tkinter))
m=tkinter.Tk()
m.title("REGISTRATION FORM")
m['bg']="yellow"
m.geometry("400x400")
x=tkinter.StringVar()
y=tkinter.StringVar()
z=tkinter.StringVar()
z1=tkinter.StringVar()
w=tkinter.StringVar()
t=tkinter.IntVar()
t1=tkinter.IntVar()
w1=tkinter.IntVar()

def check():
    plo=t1.get()
    password=w.get()
    pat="[\w]+@[\w]+[\.]+[\w]{2,}"
    mail=z1.get()
    num=y.get()
    pat1=r"[6789]{1}[0-9]{9}"
    while True:
        if (len(password)<8):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        elif not re.search(pat,mail):
            flag = -2
            break
        elif not re.search(pat1,num):
            flag=-3
            break
        elif plo!=3:
            flag=-4
            break
        else:
            #checkmail()
            flag = 0
            print("NAME:",x.get())
            print("PHONE NUMBER",y.get())
            print("AGE=",z.get())
            print("MAIL ID",z1.get())
            print("PASSWORD ENTERED:",w.get())
            if(t.get()==1):
                print("male")
            else:
                print("female")
            print("Registered Successfully...")
            aa=tkinter.Label(m,text="Registered Successfully").grid(row=15,column=1)
            break
    if flag ==-1:
        return messagebox.showerror('Error','Password should contain atleast one digit,one symbol,one lowercase letter,one upper case letter and minimum of 8 characters should be entered')
    if flag==-2:
        return messagebox.showerror('Error',"enter a valid mail id")
    if flag==-3:
        return messagebox.showerror('Error',"enter a valid phone number")
    if flag==-4:
        return messagebox.showerror('Error',"Please click the checkbox to Agree our policy")
def show():
    if(w1.get()==9):
        password=w.get()
        h=tkinter.Entry(m,text=w)
        h.grid(row=5,column=1)
    else:
        password=w.get()
        h=tkinter.Entry(m,text=w,show="*")
        h.grid(row=5,column=1)
   
a=tkinter.Label(m,text="ENTER YOUR NAME",fg="blue",bg="yellow").grid(row=1,column=0)
b=tkinter.Entry(m,text=x)
b.grid(row=1,column=1)

zz=tkinter.Entry(m,width=5)
zz.insert(5,"+91")
zz.place(x=168,y=23)


c=tkinter.Label(m,text="ENTER YOUR PHONE NUMBER",fg="blue",bg="yellow").grid(row=2,column=0)
d=tkinter.Entry(m,text=y)
d.place(x=210,y=23)

e=tkinter.Label(m,text="ENTER YOUR AGE",fg="blue",bg="yellow").grid(row=3,column=0)
f=tkinter.Entry(m,text=z)
f.grid(row=3,column=1)

e1=tkinter.Label(m,text="ENTER YOUR MAIL ID",fg="blue",bg="yellow").grid(row=4,column=0)
f1=tkinter.Entry(m,text=z1)
f1.grid(row=4,column=1)


g=tkinter.Label(m,text="ENTER PASSWORD",fg="blue",bg="yellow").grid(row=5,column=0)
h=tkinter.Entry(m,text=w,show="*")
h.grid(row=5,column=1)

aab=tkinter.Radiobutton(m, text="Male",padx = 5, variable=t, value=1).grid(row=6,column=1)
abb=tkinter.Radiobutton(m, text="Female",padx = 20, variable=t, value=2).grid(row=6,column=2)

zxc=tkinter.Checkbutton(m,text="I agree to policy ",variable=t1,onvalue=3,fg='blue').grid(row=11,column=0)


cc=tkinter.Button(m,text="Submit",command=check).grid(row=13,column=1)


xcv=tkinter.Checkbutton(m,text="Show password",command=show,variable=w1,onvalue=9).grid(row=10,column=0)
#print(x.get())
m.mainloop()
