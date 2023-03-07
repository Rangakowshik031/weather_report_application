
'''import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()'''


'''import tkinter as k
m=k.Tk()

x=k.StringVar()
y=k.StringVar()'''

'''def sample():
    l1=k.Label(m,text="u clicked on button")
    l1.pack()
    return'''


'''def sample1():
    t=x.get()
    s=y.get()
    print(t,s)'''


'''m.title("REGISTRATION FORM")
l2=k.Label(m,text="hello").grid(row=1,column=30)
#l2.pack()
l=k.Label(m,text="enter your name",font="40").grid(row=2,column=3)
p=k.Entry(m,text=x).grid(row=2,column=4)
l1=k.Label(m,text="enter your mail").grid(row=3,column=3)
p1=k.Entry(m,text=y).grid(row=3,column=4)
p3=k.Button(m,text="click me",command=sample1).grid(row=4,column=4)


#p.pack()
#l.pack()
#q.pack()'''
'''import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#Create an instance of tkinter window
win =Tk()

#Define the geometry of the window
win.geometry("600x400")

#Initialize the file name in a variable
path = "file.png"

#Create an object of tkinter ImageTk
ima=Image.open(path)
resize_image = ima.resize((200,100))
img = ImageTk.PhotoImage(resize_image)
#Create a Label Widget to display the text or Image
label = tk.Label(win, image = img)
label.pack(fill = "both", expand = "yes")
label.grid(row=1,column=2)
win.mainloop()
'''


'''import tkinter
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

import re 
flag=0

    
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
            aa=tkinter.Label(m,text="Registered Successfully").grid(row=13,column=1)
            break
    if flag ==-1:
        return messagebox.showerror('Error','Password should contain atleast one digit,one symbol,one lowercase letter,one upper case letter and minimum of 8 characters should be entered')
    if flag==-2:
        return messagebox.showerror('Error',"enter a valid mail id")
    if flag==-3:
        return messagebox.showerror('Error',"enter a valid phone number")
    if flag==-4:
        return messagebox.showerror('Error',"Please click the checkbox to Agree our policy")


   
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

zxc=tkinter.Checkbutton(m,text="I agree to policy ",variable=t1,onvalue=3,fg='blue').grid(row=10,column=0)


cc=tkinter.Button(m,text="submit",command=check).grid(row=11,column=1)

#print(x.get())
m.mainloop()'''




'''import tkinter
m=tkinter.Tk()
def sample():
    b=tkinter.Entry(m)
    b.insert(10,"hello")
    b.grid(row=2,column=1)
    e=tkinter.Label(m,text="hello")
    e.grid(row=3,column=1)

a=tkinter.Button(m,text="press here",command=sample)
a.grid(row=1,column=0)
'''

try:
    raise NameError
except:
    print('name not defined')
    raise





































